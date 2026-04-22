# MockPlatformLocation

MockPlatformLocation



# MockPlatformLocation

Mock implementation of URL state.

## API

```
class MockPlatformLocation implements PlatformLocation {
  constructor(config?: MockPlatformLocationConfig | undefined): MockPlatformLocation;
  readonly hostname: string;
  readonly protocol: string;
  readonly port: string;
  readonly pathname: string;
  readonly search: string;
  readonly hash: string;
  readonly state: unknown;
  getBaseHrefFromDOM(): string;
  onPopState(fn: LocationChangeListener): VoidFunction;
  onHashChange(fn: LocationChangeListener): VoidFunction;
  readonly href: string;
  readonly url: string;
  replaceState(state: any, title: string, newUrl: string): void;
  pushState(state: any, title: string, newUrl: string): void;
  forward(): void;
  back(): void;
  historyGo(relativePosition?: number): void;
  getState(): unknown;
}
```

### constructor

`MockPlatformLocation`

@paramconfig`MockPlatformLocationConfig | undefined`

@returns`MockPlatformLocation`

### hostname

`string`

### protocol

`string`

### port

`string`

### pathname

`string`

### search

`string`

### hash

`string`

### state

`unknown`

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

### url

`string`

### replaceState

`void`

@paramstate`any`

@paramtitle`string`

@paramnewUrl`string`

@returns`void`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@paramnewUrl`string`

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
<https://angular.dev/api/common/testing/MockPlatformLocation>
