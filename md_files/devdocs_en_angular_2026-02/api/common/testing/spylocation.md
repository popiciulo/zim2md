# SpyLocation

SpyLocation



# SpyLocation

A spy for [`Location`](../location) that allows tests to fire simulated location events.

## API

```
class SpyLocation implements Location {
  urlChanges: string[];
  setInitialPath(url: string): void;
  setBaseHref(url: string): void;
  path(): string;
  getState(): unknown;
  isCurrentPathEqualTo(path: string, query?: string): boolean;
  simulateUrlPop(pathname: string): void;
  simulateHashChange(pathname: string): void;
  prepareExternalUrl(url: string): string;
  go(path: string, query?: string, state?: any): void;
  replaceState(path: string, query?: string, state?: any): void;
  forward(): void;
  back(): void;
  historyGo(relativePosition?: number): void;
  onUrlChange(fn: (url: string, state: unknown) => void): VoidFunction;
  subscribe(onNext: (value: any) => void, onThrow?: ((error: any) => void) | null | undefined, onReturn?: (() => void) | null | undefined): SubscriptionLike;
  normalize(url: string): string;
}
```

### urlChanges

`string[]`

### setInitialPath

`void`

@paramurl`string`

@returns`void`

### setBaseHref

`void`

@paramurl`string`

@returns`void`

### path

`string`

@returns`string`

### getState

`unknown`

@returns`unknown`

### isCurrentPathEqualTo

`boolean`

@parampath`string`

@paramquery`string`

@returns`boolean`

### simulateUrlPop

`void`

@parampathname`string`

@returns`void`

### simulateHashChange

`void`

@parampathname`string`

@returns`void`

### prepareExternalUrl

`string`

@paramurl`string`

@returns`string`

### go

`void`

@parampath`string`

@paramquery`string`

@paramstate`any`

@returns`void`

### replaceState

`void`

@parampath`string`

@paramquery`string`

@paramstate`any`

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

### onUrlChange

`VoidFunction`

@paramfn`(url: string, state: unknown) => void`

@returns`VoidFunction`

### subscribe

`SubscriptionLike`

@paramonNext`(value: any) => void`

@paramonThrow`((error: any) => void) | null | undefined`

@paramonReturn`(() => void) | null | undefined`

@returns`SubscriptionLike`

### normalize

`string`

@paramurl`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/testing/SpyLocation>
