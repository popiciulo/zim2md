# RouteConfigLoadStart

RouteConfigLoadStart



# RouteConfigLoadStart

An event triggered before lazy loading a route configuration.

[RouteConfigLoadEnd](routeconfigloadend)

## API

```
class RouteConfigLoadStart {
  constructor(route: Route): RouteConfigLoadStart;
  readonly type: EventType.RouteConfigLoadStart;
  override route: Route;
  toString(): string;
}
```

### constructor

`RouteConfigLoadStart`

@paramroute`Route`

@returns`RouteConfigLoadStart`

### type

`EventType.RouteConfigLoadStart`

### route

`Route`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouteConfigLoadStart>
