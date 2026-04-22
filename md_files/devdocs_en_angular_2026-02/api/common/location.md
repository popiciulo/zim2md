# Location

Location



# Location

A service that applications can use to interact with a browser's URL.

## API

```
class Location implements OnDestroy {
  constructor(locationStrategy: LocationStrategy): Location;
  path(includeHash?: boolean): string;
  getState(): unknown;
  isCurrentPathEqualTo(path: string, query?: string): boolean;
  normalize(url: string): string;
  prepareExternalUrl(url: string): string;
  go(path: string, query?: string, state?: any): void;
  replaceState(path: string, query?: string, state?: any): void;
  forward(): void;
  back(): void;
  historyGo(relativePosition?: number): void;
  onUrlChange(fn: (url: string, state: unknown) => void): VoidFunction;
  subscribe(onNext: (value: PopStateEvent) => void, onThrow?: ((exception: any) => void) | null | undefined, onReturn?: (() => void) | null | undefined): SubscriptionLike;
  static normalizeQueryParams: (params: string) => string;
  static joinWithSlash: (start: string, end: string) => string;
  static stripTrailingSlash: (url: string) => string;
}
```

### constructor

`Location`

@paramlocationStrategy`LocationStrategy`

@returns`Location`

### path

`string`

Normalizes the URL path for this location.

@paramincludeHash`boolean`

True to include an anchor fragment in the path.

@returns`string`

### getState

`unknown`

Reports the current state of the location history.

@returns`unknown`

### isCurrentPathEqualTo

`boolean`

Normalizes the given path and compares to the current normalized path.

@parampath`string`

The given URL path.

@paramquery`string`

Query parameters.

@returns`boolean`

### normalize

`string`

Normalizes a URL path by stripping any trailing slashes.

@paramurl`string`

String representing a URL.

@returns`string`

### prepareExternalUrl

`string`

Normalizes an external URL path. If the given URL doesn't begin with a leading slash (`'/'`), adds one before normalizing. Adds a hash if [`HashLocationStrategy`](hashlocationstrategy) is in use, or the [`APP_BASE_HREF`](app_base_href) if the [`PathLocationStrategy`](pathlocationstrategy) is in use.

@paramurl`string`

String representing a URL.

@returns`string`

### go

`void`

Changes the browser's URL to a normalized version of a given URL, and pushes a new item onto the platform's history.

@parampath`string`

URL path to normalize.

@paramquery`string`

Query parameters.

@paramstate`any`

Location history state.

@returns`void`

### replaceState

`void`

Changes the browser's URL to a normalized version of the given URL, and replaces the top item on the platform's history stack.

@parampath`string`

URL path to normalize.

@paramquery`string`

Query parameters.

@paramstate`any`

Location history state.

@returns`void`

### forward

`void`

Navigates forward in the platform's history.

@returns`void`

### back

`void`

Navigates back in the platform's history.

@returns`void`

### historyGo

`void`

Navigate to a specific page from session history, identified by its relative position to the current page.

@paramrelativePosition`number`

Position of the target page in the history relative to the current page. A negative value moves backwards, a positive value moves forwards, e.g. `location.historyGo(2)` moves forward two pages and `location.historyGo(-2)` moves back two pages. When we try to go beyond what's stored in the history session, we stay in the current page. Same behaviour occurs when `relativePosition` equals 0.

@returns`void`

### onUrlChange

`VoidFunction`

Registers a URL change listener. Use to catch updates performed by the Angular framework that are not detectible through "popstate" or "hashchange" events.

@paramfn`(url: string, state: unknown) => void`

The change handler function, which take a URL and a location history state.

@returns`VoidFunction`

### subscribe

`SubscriptionLike`

Subscribes to the platform's `popState` events.

Note: [`Location.go()`](location#go) does not trigger the `popState` event in the browser. Use [`Location.onUrlChange()`](location#onUrlChange) to subscribe to URL changes instead.

@paramonNext`(value: PopStateEvent) => void`

@paramonThrow`((exception: any) => void) | null | undefined`

@paramonReturn`(() => void) | null | undefined`

@returns`SubscriptionLike`

### normalizeQueryParams

`(params: string) => string`

Normalizes URL parameters by prepending with `?` if needed.

### joinWithSlash

`(start: string, end: string) => string`

Joins two parts of a URL with a slash if needed.

### stripTrailingSlash

`(url: string) => string`

Removes a trailing slash from a URL string if needed. Looks for the first occurrence of either `#`, `?`, or the end of the line as `/` characters and removes the trailing slash if one exists.

## Description

A service that applications can use to interact with a browser's URL.

Depending on the [`LocationStrategy`](locationstrategy) used, [`Location`](location) persists to the URL's path or the URL's hash segment.

## Usage Notes

It's better to use the `Router.navigate()` service to trigger route changes. Use [`Location`](location) only if you need to interact with or create normalized URLs outside of routing.

[`Location`](location) is responsible for normalizing the URL against the application's base href. A normalized URL is absolute from the URL host, includes the application's base href, and has no trailing slash:

- `/my/app/user/123` is normalized
- `my/app/user/123` **is not** normalized
- `/my/app/user/123/` **is not** normalized

### Example

```
import {Location, LocationStrategy, PathLocationStrategy} from '@angular/common';
import {Component} from '@angular/core';

@Component({
  selector: 'path-location',
  providers: [Location, {provide: LocationStrategy, useClass: PathLocationStrategy}],
  template: `
    <h1>PathLocationStrategy</h1>
    Current URL is: <code>{{ location.path() }}</code
    ><br />
    Normalize: <code>/foo/bar/</code> is: <code>{{ location.normalize('foo/bar') }}</code
    ><br />
  `,
  standalone: false,
})
export class PathLocationComponent {
  location: Location;
  constructor(location: Location) {
    this.location = location;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/Location>
