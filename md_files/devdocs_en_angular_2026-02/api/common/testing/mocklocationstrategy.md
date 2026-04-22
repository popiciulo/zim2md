# MockLocationStrategy

MockLocationStrategy



# MockLocationStrategy

A mock implementation of [`LocationStrategy`](../locationstrategy) that allows tests to fire simulated location events.

## API

```
class MockLocationStrategy extends LocationStrategy {
  internalBaseHref: string;
  internalPath: string;
  internalTitle: string;
  urlChanges: string[];
  simulatePopState(url: string): void;
  path(includeHash?: boolean): string;
  prepareExternalUrl(internal: string): string;
  pushState(ctx: any, title: string, path: string, query: string): void;
  replaceState(ctx: any, title: string, path: string, query: string): void;
  onPopState(fn: (value: any) => void): void;
  getBaseHref(): string;
  back(): void;
  forward(): void;
  getState(): unknown;
  optional override historyGo(relativePosition: number): void;
}
```

### internalBaseHref

`string`

### internalPath

`string`

### internalTitle

`string`

### urlChanges

`string[]`

### simulatePopState

`void`

@paramurl`string`

@returns`void`

### path

`string`

@paramincludeHash`boolean`

@returns`string`

### prepareExternalUrl

`string`

@paraminternal`string`

@returns`string`

### pushState

`void`

@paramctx`any`

@paramtitle`string`

@parampath`string`

@paramquery`string`

@returns`void`

### replaceState

`void`

@paramctx`any`

@paramtitle`string`

@parampath`string`

@paramquery`string`

@returns`void`

### onPopState

`void`

@paramfn`(value: any) => void`

@returns`void`

### getBaseHref

`string`

@returns`string`

### back

`void`

@returns`void`

### forward

`void`

@returns`void`

### getState

`unknown`

@returns`unknown`

### historyGo

`void`

@paramrelativePosition`number`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/testing/MockLocationStrategy>
