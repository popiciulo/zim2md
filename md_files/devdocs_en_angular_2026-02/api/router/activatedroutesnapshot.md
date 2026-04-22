# ActivatedRouteSnapshot

ActivatedRouteSnapshot



# ActivatedRouteSnapshot

Contains the information about a route associated with a component loaded in an outlet at a particular moment in time. ActivatedRouteSnapshot can also be used to traverse the router state tree.

[Understanding route snapshots](../../guide/routing/read-route-state#understanding-route-snapshots)

## API

```
class ActivatedRouteSnapshot {
  constructor(url: UrlSegment[], params: Params, queryParams: Params, fragment: string | null, data: Data, outlet: string, component: Type<any> | null, routeConfig: Route | null, resolve: ResolveData): ActivatedRouteSnapshot;
  readonly routeConfig: Route | null;
  readonly title: string | undefined;
  override url: UrlSegment[];
  override params: Params;
  override queryParams: Params;
  override fragment: string | null;
  override data: Data;
  override outlet: string;
  override component: Type<any> | null;
  readonly root: ActivatedRouteSnapshot;
  readonly parent: ActivatedRouteSnapshot | null;
  readonly firstChild: ActivatedRouteSnapshot | null;
  readonly children: ActivatedRouteSnapshot[];
  readonly pathFromRoot: ActivatedRouteSnapshot[];
  readonly paramMap: ParamMap;
  readonly queryParamMap: ParamMap;
  toString(): string;
}
```

### constructor

`ActivatedRouteSnapshot`

@paramurl`UrlSegment[]`

The URL segments matched by this route

@paramparams`Params`

The matrix parameters scoped to this route.

You can compute all params (or data) in the router state or to get params outside of an activated component by traversing the [`RouterState`](routerstate) tree as in the following example:

```
collectRouteParams(router: Router) {
  let params = {};
  let stack: ActivatedRouteSnapshot[] = [router.routerState.snapshot.root];
  while (stack.length > 0) {
    const route = stack.pop()!;
    params = {...params, ...route.params};
    stack.push(...route.children);
  }
  return params;
}
```

@paramqueryParams`Params`

The query parameters shared by all the routes

@paramfragment`string | null`

The URL fragment shared by all the routes

@paramdata`Data`

The static and resolved data of this route

@paramoutlet`string`

The outlet name of the route

@paramcomponent`Type<any> | null`

The component of the route

@paramrouteConfig`Route | null`

@paramresolve`ResolveData`

@returns`ActivatedRouteSnapshot`

### routeConfig

`Route | null`

The configuration used to match this route \*

### title

`string | undefined`

The resolved route title

### url

`UrlSegment[]`

The URL segments matched by this route

### params

`Params`

The matrix parameters scoped to this route.

You can compute all params (or data) in the router state or to get params outside of an activated component by traversing the [`RouterState`](routerstate) tree as in the following example:

```
collectRouteParams(router: Router) {
  let params = {};
  let stack: ActivatedRouteSnapshot[] = [router.routerState.snapshot.root];
  while (stack.length > 0) {
    const route = stack.pop()!;
    params = {...params, ...route.params};
    stack.push(...route.children);
  }
  return params;
}
```

### queryParams

`Params`

The query parameters shared by all the routes

### fragment

`string | null`

The URL fragment shared by all the routes

### data

`Data`

The static and resolved data of this route

### outlet

`string`

The outlet name of the route

### component

`Type<any> | null`

The component of the route

### root

`ActivatedRouteSnapshot`

The root of the router state

### parent

`ActivatedRouteSnapshot | null`

The parent of this route in the router state tree

### firstChild

`ActivatedRouteSnapshot | null`

The first child of this route in the router state tree

### children

`ActivatedRouteSnapshot[]`

The children of this route in the router state tree

### pathFromRoot

`ActivatedRouteSnapshot[]`

The path from the root of the router state tree to this route

### paramMap

`ParamMap`

### queryParamMap

`ParamMap`

### toString

`string`

@returns`string`

## Description

Contains the information about a route associated with a component loaded in an outlet at a particular moment in time. ActivatedRouteSnapshot can also be used to traverse the router state tree.

The following example initializes a component with route information extracted from the snapshot of the root node at the time of creation.

```
@Component({templateUrl:'./my-component.html'})
class MyComponent {
  constructor(route: ActivatedRoute) {
    const id: string = route.snapshot.params.id;
    const url: string = route.snapshot.url.join('');
    const user = route.snapshot.data.user;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ActivatedRouteSnapshot>
