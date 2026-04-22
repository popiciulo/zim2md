# LocationStrategy

LocationStrategy



# LocationStrategy

Enables the [`Location`](location) service to read route state from the browser's URL. Angular provides two strategies: [`HashLocationStrategy`](hashlocationstrategy) and [`PathLocationStrategy`](pathlocationstrategy).

## API

```
abstract class LocationStrategy {
  abstract path(includeHash?: boolean | undefined): string;
  abstract prepareExternalUrl(internal: string): string;
  abstract getState(): unknown;
  abstract pushState(state: any, title: string, url: string, queryParams: string): void;
  abstract replaceState(state: any, title: string, url: string, queryParams: string): void;
  abstract forward(): void;
  abstract back(): void;
  optional historyGo(relativePosition: number): void;
  abstract onPopState(fn: LocationChangeListener): void;
  abstract getBaseHref(): string;
}
```

### path

`string`

@paramincludeHash`boolean | undefined`

@returns`string`

### prepareExternalUrl

`string`

@paraminternal`string`

@returns`string`

### getState

`unknown`

@returns`unknown`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

@paramqueryParams`string`

@returns`void`

### replaceState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

@paramqueryParams`string`

@returns`void`

### forward

`void`

@returns`void`

### back

`void`

@returns`void`

### historyGo

`void`

@paramrelativePosition`number`

@returns`void`

### onPopState

`void`

@paramfn`LocationChangeListener`

@returns`void`

### getBaseHref

`string`

@returns`string`

## Description

Enables the [`Location`](location) service to read route state from the browser's URL. Angular provides two strategies: [`HashLocationStrategy`](hashlocationstrategy) and [`PathLocationStrategy`](pathlocationstrategy).

Applications should use the `Router` or [`Location`](location) services to interact with application route state.

For instance, [`HashLocationStrategy`](hashlocationstrategy) produces URLs like `http://example.com/#/foo`, and [`PathLocationStrategy`](pathlocationstrategy) produces `http://example.com/foo` as an equivalent URL.

See these two classes for more.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/LocationStrategy>
