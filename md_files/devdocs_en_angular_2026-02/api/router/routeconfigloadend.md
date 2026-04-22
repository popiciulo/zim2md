# RouteConfigLoadEnd

RouteConfigLoadEnd



# RouteConfigLoadEnd

An event triggered when a route has been lazy loaded.

[RouteConfigLoadStart](routeconfigloadstart)

## API

```
class RouteConfigLoadEnd {
  constructor(route: Route): RouteConfigLoadEnd;
  readonly type: EventType.RouteConfigLoadEnd;
  override route: Route;
  toString(): string;
}
```

### constructor

`RouteConfigLoadEnd`

@paramroute`Route`

@returns`RouteConfigLoadEnd`

### type

`EventType.RouteConfigLoadEnd`

### route

`Route`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouteConfigLoadEnd>
