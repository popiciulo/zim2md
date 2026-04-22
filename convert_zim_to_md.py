#!/usr/bin/env python3
"""Convert Kiwix/OpenZIM archives in zim_files/ to Markdown in md_files/."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Iterator


def _load_libzim_archive(zim_path: Path) -> Any:
    try:
        from libzim.reader import Archive  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency: libzim. Install it with `pip install libzim`."
        ) from exc
    return Archive(str(zim_path))


def _html_to_markdown(html: str) -> str:
    try:
        from markdownify import markdownify as to_md  # type: ignore

        return to_md(html, heading_style="ATX", bullets="-")
    except ImportError:
        # Fallback converter: keep text if markdownify is unavailable.
        import html as html_module

        text = re.sub(r"<[^>]+>", "", html)
        text = html_module.unescape(text)
        lines = [line.rstrip() for line in text.splitlines()]
        cleaned = "\n".join(line for line in lines if line.strip())
        return cleaned + "\n" if cleaned else ""


def _call_or_value(obj: Any, name: str, default: Any = None) -> Any:
    if not hasattr(obj, name):
        return default
    value = getattr(obj, name)
    if callable(value):
        try:
            return value()
        except TypeError:
            return default
    return value


def _iter_entries(archive: Any) -> Iterator[Any]:
    for method_name in ("iter_by_path", "iterByPath"):
        method = getattr(archive, method_name, None)
        if callable(method):
            yield from method()
            return

    for method_name in ("find_by_path", "findByPath"):
        method = getattr(archive, method_name, None)
        if callable(method):
            yield from method("")
            return

    # python-libzim exposes private ID-based access in versions without iterator APIs.
    get_by_id = getattr(archive, "_get_entry_by_id", None)
    entry_count = getattr(archive, "entry_count", None)
    if callable(get_by_id) and isinstance(entry_count, int):
        for entry_id in range(entry_count):
            try:
                yield get_by_id(entry_id)
            except Exception:
                # Skip rare invalid ids instead of aborting the whole conversion.
                continue
        return

    raise RuntimeError("Unable to iterate entries from archive with available libzim API.")


def _entry_path(entry: Any) -> str:
    for name in ("path", "get_path", "getPath"):
        value = _call_or_value(entry, name)
        if isinstance(value, str):
            return value
    return ""


def _entry_title(entry: Any) -> str:
    for name in ("title", "get_title", "getTitle"):
        value = _call_or_value(entry, name)
        if isinstance(value, str) and value.strip():
            return value
    return ""


def _entry_item(entry: Any) -> Any:
    for name in ("get_item", "getItem"):
        method = getattr(entry, name, None)
        if callable(method):
            return method()
    return None


def _item_mimetype(item: Any) -> str:
    for name in ("mimetype", "mime_type", "get_mimetype", "getMimeType"):
        value = _call_or_value(item, name)
        if isinstance(value, str):
            return value.lower()
    return ""


def _item_content_bytes(item: Any) -> bytes:
    content = _call_or_value(item, "content")
    if content is None:
        content = _call_or_value(item, "get_data")
    if content is None:
        content = _call_or_value(item, "getData")

    if content is None:
        return b""
    if isinstance(content, bytes):
        return content
    return bytes(content)


def _safe_rel_output_path(entry_path: str, title: str) -> Path:
    raw = entry_path
    if raw.startswith("A/"):
        raw = raw[2:]
    raw = raw.strip("/")
    if not raw:
        raw = title or "untitled"

    raw = raw.replace("\\", "/")
    raw = re.sub(r"[^a-zA-Z0-9._/\- ]", "_", raw)
    parts = [part.strip() for part in raw.split("/") if part.strip() and part not in (".", "..")]
    if not parts:
        parts = ["untitled"]

    path = Path(*parts)
    if path.suffix.lower() not in (".md", ".markdown"):
        path = path.with_suffix(".md")
    return path


def _write_markdown(out_path: Path, title: str, markdown: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    front = f"# {title}\n\n" if title else ""
    out_path.write_text(front + markdown.strip() + "\n", encoding="utf-8")


def convert_archive(zim_path: Path, output_root: Path, include_non_a_namespace: bool) -> tuple[int, int]:
    archive = _load_libzim_archive(zim_path)
    written = 0
    skipped = 0

    has_new_namespace_scheme = bool(getattr(archive, "has_new_namespace_scheme", False))

    per_zim_out = output_root / zim_path.stem
    per_zim_out.mkdir(parents=True, exist_ok=True)

    for entry in _iter_entries(archive):
        path = _entry_path(entry)
        if not path:
            skipped += 1
            continue

        # Old ZIMs commonly use A/ for articles; new scheme archives are namespaceless.
        if (
            not include_non_a_namespace
            and not has_new_namespace_scheme
            and not path.startswith("A/")
        ):
            skipped += 1
            continue

        item = _entry_item(entry)
        if item is None:
            skipped += 1
            continue

        mimetype = _item_mimetype(item)
        if "html" not in mimetype and "xhtml" not in mimetype:
            skipped += 1
            continue

        content = _item_content_bytes(item)
        if not content:
            skipped += 1
            continue

        html = content.decode("utf-8", errors="replace")
        markdown = _html_to_markdown(html)
        if not markdown.strip():
            skipped += 1
            continue

        title = _entry_title(entry)
        rel = _safe_rel_output_path(path, title)
        out_path = per_zim_out / rel
        _write_markdown(out_path, title, markdown)
        written += 1

    return written, skipped


def _find_zim_files(directory: Path) -> Iterable[Path]:
    return sorted(p for p in directory.glob("*.zim") if p.is_file())


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Kiwix/OpenZIM archives from zim_files/ into Markdown in md_files/."
    )
    parser.add_argument(
        "--zim-dir",
        type=Path,
        default=Path("zim_files"),
        help="Directory containing .zim files (default: zim_files)",
    )
    parser.add_argument(
        "--md-dir",
        type=Path,
        default=Path("md_files"),
        help="Directory where Markdown files are written (default: md_files)",
    )
    parser.add_argument(
        "--include-non-a-namespace",
        action="store_true",
        help="Also include entries outside the A/ namespace.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    zim_dir = args.zim_dir
    md_dir = args.md_dir

    if not zim_dir.exists() or not zim_dir.is_dir():
        print(f"ERROR: zim directory not found: {zim_dir}", file=sys.stderr)
        return 1

    md_dir.mkdir(parents=True, exist_ok=True)

    zim_files = list(_find_zim_files(zim_dir))
    if not zim_files:
        print(f"No .zim files found in {zim_dir}")
        return 0

    total_written = 0
    total_skipped = 0
    for zim_path in zim_files:
        print(f"Processing: {zim_path.name}")
        written, skipped = convert_archive(
            zim_path=zim_path,
            output_root=md_dir,
            include_non_a_namespace=args.include_non_a_namespace,
        )
        print(f"  written={written} skipped={skipped}")
        total_written += written
        total_skipped += skipped

    print("Done.")
    print(f"Total written: {total_written}")
    print(f"Total skipped: {total_skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
