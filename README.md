# zim2md

Convert Kiwix/OpenZIM archives (`.zim`) into Markdown files.

## Folder layout

- Put input ZIM archives in `zim_files/`
- Markdown output is written to `md_files/`

Each ZIM is extracted into its own subfolder:

- `md_files/<zim-file-name-without-extension>/...`

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python convert_zim_to_md.py
```

Optional flag:

```bash
python convert_zim_to_md.py --include-non-a-namespace
```

By default, only `A/` namespace entries (usually article content) are converted.
For newer namespaceless ZIMs, the converter automatically includes regular entries.

## Notes

- HTML entries are converted to Markdown.
- Non-HTML entries are skipped.
- If `markdownify` is not installed, a plain-text fallback converter is used.
