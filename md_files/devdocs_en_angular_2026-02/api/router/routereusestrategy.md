# RouteReuseStrategy

RouteReuseStrategy



# RouteReuseStrategy

Provides a way to customize when activated routes get reused.

## API

```
abstract class RouteReuseStrategy {
  abstract shouldDetach(route: ActivatedRouteSnapshot): boolean;
  abstract store(route: ActivatedRouteSnapshot, handle: DetachedRouteHandle | null): void;
  abstract shouldAttach(route: ActivatedRouteSnapshot): boolean;
  abstract retrieve(route: ActivatedRouteSnapshot): DetachedRouteHandle | null;
  abstract shouldReuseRoute(future: ActivatedRouteSnapshot, curr: ActivatedRouteSnapshot): boolean;
}
```

### shouldDetach

`boolean`

Determines if this route (and its subtree) should be detached to be reused later

@paramroute`ActivatedRouteSnapshot`

@returns`boolean`

### store

`void`

Stores the detached route.

Storing a `null` value should erase the previously stored value.

@paramroute`ActivatedRouteSnapshot`

@paramhandle`DetachedRouteHandle | null`

@returns`void`

### shouldAttach

`boolean`

Determines if this route (and its subtree) should be reattached

@paramroute`ActivatedRouteSnapshot`

@returns`boolean`

### retrieve

`DetachedRouteHandle | null`

Retrieves the previously stored route

@paramroute`ActivatedRouteSnapshot`

@returns`DetachedRouteHandle | null`

### shouldReuseRoute

`boolean`

Determines if a route should be reused

@paramfuture`ActivatedRouteSnapshot`

@paramcurr`ActivatedRouteSnapshot`

@returns`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouteReuseStrategy>
