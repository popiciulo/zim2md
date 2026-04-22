# ActivatedRoute

ActivatedRoute



# ActivatedRoute

Provides access to information about a route associated with a component that is loaded in an outlet. Use to traverse the [`RouterState`](routerstate) tree and extract information from nodes.

[Getting route information](../../guide/routing/common-router-tasks#getting-route-information)

## API

```
class ActivatedRoute {
  constructor(urlSubject: BehaviorSubject<UrlSegment[]>, paramsSubject: BehaviorSubject<Params>, queryParamsSubject: BehaviorSubject<Params>, fragmentSubject: BehaviorSubject<string | null>, dataSubject: BehaviorSubject<Data>, outlet: string, component: Type<any> | null, futureSnapshot: ActivatedRouteSnapshot): ActivatedRoute;
  snapshot: ActivatedRouteSnapshot;
  readonly title: Observable<string | undefined>;
  url: Observable<UrlSegment[]>;
  params: Observable<Params>;
  queryParams: Observable<Params>;
  fragment: Observable<string | null>;
  data: Observable<Data>;
  override outlet: string;
  override component: Type<any> | null;
  readonly routeConfig: Route | null;
  readonly root: ActivatedRoute;
  readonly parent: ActivatedRoute | null;
  readonly firstChild: ActivatedRoute | null;
  readonly children: ActivatedRoute[];
  readonly pathFromRoot: ActivatedRoute[];
  readonly paramMap: Observable<ParamMap>;
  readonly queryParamMap: Observable<ParamMap>;
  toString(): string;
}
```

### constructor

`ActivatedRoute`

@paramurlSubject`BehaviorSubject<UrlSegment[]>`

@paramparamsSubject`BehaviorSubject<Params>`

@paramqueryParamsSubject`BehaviorSubject<Params>`

@paramfragmentSubject`BehaviorSubject<string | null>`

@paramdataSubject`BehaviorSubject<Data>`

@paramoutlet`string`

The outlet name of the route, a constant.

@paramcomponent`Type<any> | null`

The component of the route, a constant.

@paramfutureSnapshot`ActivatedRouteSnapshot`

@returns`ActivatedRoute`

### snapshot

`ActivatedRouteSnapshot`

The current snapshot of this route

### title

`Observable<string | undefined>`

An Observable of the resolved route title

### url

`Observable<UrlSegment[]>`

An observable of the URL segments matched by this route.

### params

`Observable<Params>`

An observable of the matrix parameters scoped to this route.

### queryParams

`Observable<Params>`

An observable of the query parameters shared by all the routes.

### fragment

`Observable<string | null>`

An observable of the URL fragment shared by all the routes.

### data

`Observable<Data>`

An observable of the static and resolved data of this route.

### outlet

`string`

The outlet name of the route, a constant.

### component

`Type<any> | null`

The component of the route, a constant.

### routeConfig

`Route | null`

The configuration used to match this route.

### root

`ActivatedRoute`

The root of the router state.

### parent

`ActivatedRoute | null`

The parent of this route in the router state tree.

### firstChild

`ActivatedRoute | null`

The first child of this route in the router state tree.

### children

`ActivatedRoute[]`

The children of this route in the router state tree.

### pathFromRoot

`ActivatedRoute[]`

The path from the root of the router state tree to this route.

### paramMap

`Observable<ParamMap>`

An Observable that contains a map of the required and optional parameters specific to the route. The map supports retrieving single and multiple values from the same parameter.

### queryParamMap

`Observable<ParamMap>`

An Observable that contains a map of the query parameters available to all routes. The map supports retrieving single and multiple values from the query parameter.

### toString

`string`

@returns`string`

## Description

Provides access to information about a route associated with a component that is loaded in an outlet. Use to traverse the [`RouterState`](routerstate) tree and extract information from nodes.

The following example shows how to construct a component using information from a currently activated route.

Note: the observables in this class only emit when the current and previous values differ based on shallow equality. For example, changing deeply nested properties in resolved `data` will not cause the [`ActivatedRoute.data`](activatedroute#data) `Observable` to emit a new value.

```
import {Component} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';
@Component({
})
export class ActivatedRouteComponent {
  constructor(route: ActivatedRoute) {
    const id: Observable<string> = route.params.pipe(map((p) => p['id']));
    const url: Observable<string> = route.url.pipe(map((segments) => segments.join('')));
    // route.data includes both `data` and `resolve`
    const user = route.data.pipe(map((d) => d['user']));
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ActivatedRoute>
