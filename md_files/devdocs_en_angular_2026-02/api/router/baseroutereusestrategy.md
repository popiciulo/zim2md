# BaseRouteReuseStrategy

BaseRouteReuseStrategy



# BaseRouteReuseStrategy

This base route reuse strategy only reuses routes when the matched router configs are identical. This prevents components from being destroyed and recreated when just the route parameters, query parameters or fragment change (that is, the existing component is *reused*).

## API

```
abstract class BaseRouteReuseStrategy implements RouteReuseStrategy {
  shouldDetach(route: ActivatedRouteSnapshot): boolean;
  store(route: ActivatedRouteSnapshot, detachedTree: DetachedRouteHandle): void;
  shouldAttach(route: ActivatedRouteSnapshot): boolean;
  retrieve(route: ActivatedRouteSnapshot): DetachedRouteHandle | null;
  shouldReuseRoute(future: ActivatedRouteSnapshot, curr: ActivatedRouteSnapshot): boolean;
}
```

### shouldDetach

`boolean`

Whether the given route should detach for later reuse. Always returns false for [`BaseRouteReuseStrategy`](baseroutereusestrategy).

@paramroute`ActivatedRouteSnapshot`

@returns`boolean`

### store

`void`

A no-op; the route is never stored since this strategy never detaches routes for later re-use.

@paramroute`ActivatedRouteSnapshot`

@paramdetachedTree`DetachedRouteHandle`

@returns`void`

### shouldAttach

`boolean`

Returns `false`, meaning the route (and its subtree) is never reattached

@paramroute`ActivatedRouteSnapshot`

@returns`boolean`

### retrieve

`DetachedRouteHandle | null`

Returns `null` because this strategy does not store routes for later re-use.

@paramroute`ActivatedRouteSnapshot`

@returns`DetachedRouteHandle | null`

### shouldReuseRoute

`boolean`

Determines if a route should be reused. This strategy returns `true` when the future route config and current route config are identical.

@paramfuture`ActivatedRouteSnapshot`

@paramcurr`ActivatedRouteSnapshot`

@returns`boolean`

## Description

This base route reuse strategy only reuses routes when the matched router configs are identical. This prevents components from being destroyed and recreated when just the route parameters, query parameters or fragment change (that is, the existing component is *reused*).

This strategy does not store any routes for later reuse.

Angular uses this strategy by default.

It can be used as a base class for custom route reuse strategies, i.e. you can create your own class that extends the [`BaseRouteReuseStrategy`](baseroutereusestrategy) one.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/BaseRouteReuseStrategy>
