# BrowserPlatformLocation

BrowserPlatformLocation



# BrowserPlatformLocation

[`PlatformLocation`](platformlocation) encapsulates all of the direct calls to platform APIs. This class should not be used directly by an application developer. Instead, use [`Location`](location).

## API

```
class BrowserPlatformLocation extends PlatformLocation {
  getBaseHrefFromDOM(): string;
  onPopState(fn: LocationChangeListener): VoidFunction;
  onHashChange(fn: LocationChangeListener): VoidFunction;
  readonly href: string;
  readonly protocol: string;
  readonly hostname: string;
  readonly port: string;
   get pathname(): string;
  readonly search: string;
  readonly hash: string;
  pushState(state: any, title: string, url: string): void;
  replaceState(state: any, title: string, url: string): void;
  forward(): void;
  back(): void;
  historyGo(relativePosition?: number): void;
  getState(): unknown;
}
```

### getBaseHrefFromDOM

`string`

@returns`string`

### onPopState

`VoidFunction`

@paramfn`LocationChangeListener`

@returns`VoidFunction`

### onHashChange

`VoidFunction`

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

### pathname

`string`

### search

`string`

### hash

`string`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

@returns`void`

### replaceState

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

### getState

`unknown`

@returns`unknown`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/BrowserPlatformLocation>
