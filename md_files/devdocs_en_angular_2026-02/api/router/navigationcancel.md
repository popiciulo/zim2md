# NavigationCancel

NavigationCancel



# NavigationCancel

An event triggered when a navigation is canceled, directly or indirectly. This can happen for several reasons including when a route guard returns `false` or initiates a redirect by returning a [`UrlTree`](urltree).

[NavigationStart](navigationstart)[NavigationEnd](navigationend)[NavigationError](navigationerror)

## API

```
class NavigationCancel extends RouterEvent {
  constructor(id: number, url: string, reason: string, code?: NavigationCancellationCode | undefined): NavigationCancel;
  readonly type: EventType.NavigationCancel;
  override reason: string;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`NavigationCancel`

@paramid`number`

@paramurl`string`

@paramreason`string`

A description of why the navigation was cancelled. For debug purposes only. Use `code` instead for a stable cancellation reason that can be used in production.

@paramcode`NavigationCancellationCode | undefined`

A code to indicate why the navigation was canceled. This cancellation code is stable for the reason and can be relied on whereas the `reason` string could change and should not be used in production.

@returns`NavigationCancel`

### type

`EventType.NavigationCancel`

### reason

`string`

A description of why the navigation was cancelled. For debug purposes only. Use `code` instead for a stable cancellation reason that can be used in production.

### toString

`string`

@returns`string`

### id

`number`

A unique ID that the router assigns to every router navigation.

### url

`string`

The URL that is the destination for this navigation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationCancel>
