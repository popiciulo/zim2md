# PlatformNavigation

PlatformNavigation



# PlatformNavigation

This class wraps the platform Navigation API which allows server-specific and test implementations.

## API

```
abstract class PlatformNavigation implements Navigation {
  abstract entries(): NavigationHistoryEntry[];
  abstract currentEntry: any;
  abstract updateCurrentEntry(options: NavigationUpdateCurrentEntryOptions): void;
  abstract transition: any;
  abstract canGoBack: boolean;
  abstract canGoForward: boolean;
  abstract navigate(url: string, options?: any): NavigationResult;
  abstract reload(options?: any): NavigationResult;
  abstract traverseTo(key: string, options?: any): NavigationResult;
  abstract back(options?: any): NavigationResult;
  abstract forward(options?: any): NavigationResult;
  abstract onnavigate: ((this: Navigation, ev: NavigateEvent) => any) | null;
  abstract onnavigatesuccess: ((this: Navigation, ev: Event) => any) | null;
  abstract onnavigateerror: ((this: Navigation, ev: ErrorEvent) => any) | null;
  abstract oncurrententrychange: ((this: Navigation, ev: NavigationCurrentEntryChangeEvent) => any) | null;
  abstract addEventListener(type: unknown, listener: unknown, options?: unknown): void;
  abstract removeEventListener(type: unknown, listener: unknown, options?: unknown): void;
  abstract dispatchEvent(event: Event): boolean;
}
```

### entries

`NavigationHistoryEntry[]`

@returns`NavigationHistoryEntry[]`

### currentEntry

`any`

### updateCurrentEntry

`void`

@paramoptions`NavigationUpdateCurrentEntryOptions`

@returns`void`

### transition

`any`

### canGoBack

`boolean`

### canGoForward

`boolean`

### navigate

`NavigationResult`

@paramurl`string`

@paramoptions`any`

@returns`NavigationResult`

### reload

`NavigationResult`

@paramoptions`any`

@returns`NavigationResult`

### traverseTo

`NavigationResult`

@paramkey`string`

@paramoptions`any`

@returns`NavigationResult`

### back

`NavigationResult`

@paramoptions`any`

@returns`NavigationResult`

### forward

`NavigationResult`

@paramoptions`any`

@returns`NavigationResult`

### onnavigate

`((this: Navigation, ev: NavigateEvent) => any) | null`

### onnavigatesuccess

`((this: Navigation, ev: Event) => any) | null`

### onnavigateerror

`((this: Navigation, ev: ErrorEvent) => any) | null`

### oncurrententrychange

`((this: Navigation, ev: NavigationCurrentEntryChangeEvent) => any) | null`

### addEventListener

`void`

@paramtype`unknown`

@paramlistener`unknown`

@paramoptions`unknown`

@returns`void`

### removeEventListener

`void`

@paramtype`unknown`

@paramlistener`unknown`

@paramoptions`unknown`

@returns`void`

### dispatchEvent

`boolean`

@paramevent`Event`

@returns`boolean`

## Description

This class wraps the platform Navigation API which allows server-specific and test implementations.

Browser support is limited, so this API may not be available in all environments, may contain bugs, and is experimental.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/PlatformNavigation>
