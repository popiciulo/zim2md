# RoutesRecognized

RoutesRecognized



# RoutesRecognized

An event triggered when routes are recognized.

## API

```
class RoutesRecognized extends RouterEvent {
  constructor(id: number, url: string, urlAfterRedirects: string, state: RouterStateSnapshot): RoutesRecognized;
  readonly type: EventType.RoutesRecognized;
  override urlAfterRedirects: string;
  override state: RouterStateSnapshot;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`RoutesRecognized`

@paramid`number`

@paramurl`string`

@paramurlAfterRedirects`string`

@paramstate`RouterStateSnapshot`

@returns`RoutesRecognized`

### type

`EventType.RoutesRecognized`

### urlAfterRedirects

`string`

### state

`RouterStateSnapshot`

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
<https://angular.dev/api/router/RoutesRecognized>
