# PlatformLocation

PlatformLocation



# PlatformLocation

This class should not be used directly by an application developer. Instead, use [`Location`](location).

## API

```
abstract class PlatformLocation {
  abstract getBaseHrefFromDOM(): string;
  abstract getState(): unknown;
  abstract onPopState(fn: LocationChangeListener): VoidFunction;
  abstract onHashChange(fn: LocationChangeListener): VoidFunction;
  abstract readonly href: string;
  abstract readonly protocol: string;
  abstract readonly hostname: string;
  abstract readonly port: string;
  abstract readonly pathname: string;
  abstract readonly search: string;
  abstract readonly hash: string;
  abstract replaceState(state: any, title: string, url: string): void;
  abstract pushState(state: any, title: string, url: string): void;
  abstract forward(): void;
  abstract back(): void;
  optional historyGo(relativePosition: number): void;
}
```

### getBaseHrefFromDOM

`string`

@returns`string`

### getState

`unknown`

@returns`unknown`

### onPopState

`VoidFunction`

Returns a function that, when executed, removes the `popstate` event handler.

@paramfn`LocationChangeListener`

@returns`VoidFunction`

### onHashChange

`VoidFunction`

Returns a function that, when executed, removes the `hashchange` event handler.

@paramfn`LocationChangeListener`

@returns`VoidFunction`

### href

`string`

### protocol

`string`

### hostname

`string`

### port

`string`

### pathname

`string`

### search

`string`

### hash

`string`

### replaceState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

@returns`void`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

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

## Description

This class should not be used directly by an application developer. Instead, use [`Location`](location).

[`PlatformLocation`](platformlocation) encapsulates all calls to DOM APIs, which allows the Router to be platform-agnostic. This means that we can have different implementation of [`PlatformLocation`](platformlocation) for the different platforms that Angular supports. For example, `@angular/platform-browser` provides an implementation specific to the browser environment, while `@angular/platform-server` provides one suitable for use with server-side rendering.

The [`PlatformLocation`](platformlocation) class is used directly by all implementations of [`LocationStrategy`](locationstrategy) when they need to interact with the DOM APIs like pushState, popState, etc.

[`LocationStrategy`](locationstrategy) in turn is used by the [`Location`](location) service which is used directly by the [`Router`](../router/router) in order to navigate between routes. Since all interactions between [`Router`](../router/router) / [`Location`](location) / [`LocationStrategy`](locationstrategy) and DOM APIs flow through the [`PlatformLocation`](platformlocation) class, they are all platform-agnostic.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/PlatformLocation>
