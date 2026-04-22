# NavigationError

NavigationError



# NavigationError

An event triggered when a navigation fails due to an unexpected error.

[NavigationStart](navigationstart)[NavigationEnd](navigationend)[NavigationCancel](navigationcancel)

## API

```
class NavigationError extends RouterEvent {
  constructor(id: number, url: string, error: any, target?: RouterStateSnapshot | undefined): NavigationError;
  readonly type: EventType.NavigationError;
  override error: any;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`NavigationError`

@paramid`number`

@paramurl`string`

@paramerror`any`

@paramtarget`RouterStateSnapshot | undefined`

The target of the navigation when the error occurred.

Note that this can be `undefined` because an error could have occurred before the [`RouterStateSnapshot`](routerstatesnapshot) was created for the navigation.

@returns`NavigationError`

### type

`EventType.NavigationError`

### error

`any`

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
<https://angular.dev/api/router/NavigationError>
