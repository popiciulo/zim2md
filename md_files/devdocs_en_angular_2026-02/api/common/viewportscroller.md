# ViewportScroller

ViewportScroller



# ViewportScroller

Defines a scroll position manager. Implemented by `BrowserViewportScroller`.

## API

```
abstract class ViewportScroller {
  abstract setOffset(offset: [number, number] | (() => [number, number])): void;
  abstract getScrollPosition(): [number, number];
  abstract scrollToPosition(position: [number, number], options?: ScrollOptions | undefined): void;
  abstract scrollToAnchor(anchor: string, options?: ScrollOptions | undefined): void;
  abstract setHistoryScrollRestoration(scrollRestoration: "auto" | "manual"): void;
}
```

### setOffset

`void`

Configures the top offset used when scrolling to an anchor.

@paramoffset`[number, number] | (() => [number, number])`

A position in screen coordinates (a tuple with x and y values) or a function that returns the top offset position.

@returns`void`

### getScrollPosition

`[number, number]`

Retrieves the current scroll position.

@returns`[number, number]`

### scrollToPosition

`void`

Scrolls to a specified position.

@paramposition`[number, number]`

A position in screen coordinates (a tuple with x and y values).

@paramoptions`ScrollOptions | undefined`

@returns`void`

### scrollToAnchor

`void`

Scrolls to an anchor element.

@paramanchor`string`

The ID of the anchor element.

@paramoptions`ScrollOptions | undefined`

@returns`void`

### setHistoryScrollRestoration

`void`

Disables automatic scroll restoration provided by the browser. See also [window.history.scrollRestoration info](https://developers.google.com/web/updates/2015/09/history-api-scroll-restoration).

@paramscrollRestoration`"auto" | "manual"`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/ViewportScroller>
