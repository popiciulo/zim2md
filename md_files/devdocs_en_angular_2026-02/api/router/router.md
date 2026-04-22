# Router

Router



# Router

A service that facilitates navigation among views and URL manipulation capabilities. This service is provided in the root scope and configured with [provideRouter](providerouter).

[Route](route)[provideRouter](providerouter)[Routing and Navigation Guide](../../guide/routing/common-router-tasks)

## API

```
class Router {
  readonly events: Observable<Event>;
  readonly routerState: RouterState;
  navigated: boolean;
  routeReuseStrategy: RouteReuseStrategy;
  onSameUrlNavigation: OnSameUrlNavigation;
  config: Routes;
  readonly componentInputBindingEnabled: boolean;
  readonly currentNavigation: Signal<Navigation | null>;
  initialNavigation(): void;
  setUpLocationChangeListener(): void;
  readonly url: string;
  getCurrentNavigation(): Navigation | null;
  readonly lastSuccessfulNavigation: Signal<Navigation | null>;
  resetConfig(config: Routes): void;
  dispose(): void;
  createUrlTree(commands: readonly any[], navigationExtras?: UrlCreationOptions): UrlTree;
  navigateByUrl(url: string | UrlTree, extras?: NavigationBehaviorOptions): Promise<boolean>;
  navigate(commands: readonly any[], extras?: NavigationExtras): Promise<boolean>;
  serializeUrl(url: UrlTree): string;
  parseUrl(url: string): UrlTree;
  isActive(url: string | UrlTree, exact: boolean): boolean;
  isActive(url: string | UrlTree, matchOptions: IsActiveMatchOptions): boolean;
  isActive(url: string | UrlTree, matchOptions: boolean | IsActiveMatchOptions): boolean;
}
```

### events

`Observable<Event>`

An event stream for routing events.

### routerState

`RouterState`

The current state of routing in this NgModule.

### navigated

`boolean`

True if at least one navigation event has occurred, false otherwise.

### routeReuseStrategy

`RouteReuseStrategy`

@deprecated

Configure using `providers` instead: `{provide: RouteReuseStrategy, useClass: MyStrategy}`.

A strategy for re-using routes.

### onSameUrlNavigation

`OnSameUrlNavigation`

@deprecated

Configure this through [`provideRouter`](providerouter) or [`RouterModule.forRoot`](routermodule#forRoot) instead.

How to handle a navigation request to the current URL.

### config

`Routes`

### componentInputBindingEnabled

`boolean`

Indicates whether the application has opted in to binding Router data to component inputs.

This option is enabled by the [`withComponentInputBinding`](withcomponentinputbinding) feature of [`provideRouter`](providerouter) or `bindToComponentInputs` in the [`ExtraOptions`](extraoptions) of [`RouterModule.forRoot`](routermodule#forRoot).

### currentNavigation

`Signal<Navigation | null>`

Signal of the current [`Navigation`](navigation) object when the router is navigating, and `null` when idle.

Note: The current navigation becomes to null after the NavigationEnd event is emitted.

### initialNavigation

`void`

Sets up the location change listener and performs the initial navigation.

@returns`void`

### setUpLocationChangeListener

`void`

Sets up the location change listener. This listener detects navigations triggered from outside the Router (the browser back/forward buttons, for example) and schedules a corresponding Router navigation so that the correct events, guards, etc. are triggered.

@returns`void`

### url

`string`

The current URL.

### getCurrentNavigation

`Navigation | null`

Returns the current [`Navigation`](navigation) object when the router is navigating, and `null` when idle.

@deprecated

Use the `currentNavigation` signal instead.

@returns`Navigation | null`

### lastSuccessfulNavigation

`Signal<Navigation | null>`

The [`Navigation`](navigation) object of the most recent navigation to succeed and `null` if there has not been a successful navigation yet.

### resetConfig

`void`

Resets the route configuration used for navigation and generating links.

@paramconfig`Routes`

The route array for the new configuration.

@returns`void`

Usage notes

```
router.resetConfig([
 { path: 'team/:id', component: TeamCmp, children: [
   { path: 'simple', component: SimpleCmp },
   { path: 'user/:name', component: UserCmp }
 ]}
]);
```

### dispose

`void`

Disposes of the router.

@returns`void`

### createUrlTree

`UrlTree`

Appends URL segments to the current URL tree to create a new URL tree.

@paramcommands`readonly any[]`

An array of URL fragments with which to construct the new URL tree. If the path is static, can be the literal URL string. For a dynamic path, pass an array of path segments, followed by the parameters for each segment. The fragments are applied to the current URL tree or the one provided in the `relativeTo` property of the options object, if supplied.

@paramnavigationExtras`UrlCreationOptions`

Options that control the navigation strategy.

@returns`UrlTree`

Usage notes

```
// create /team/33/user/11
router.createUrlTree(['/team', 33, 'user', 11]);

// create /team/33;expand=true/user/11
router.createUrlTree(['/team', 33, {expand: true}, 'user', 11]);

// you can collapse static segments like this (this works only with the first passed-in value):
router.createUrlTree(['/team/33/user', userId]);

// If the first segment can contain slashes, and you do not want the router to split it,
// you can do the following:
router.createUrlTree([{segmentPath: '/one/two'}]);

// create /team/33/(user/11//right:chat)
router.createUrlTree(['/team', 33, {outlets: {primary: 'user/11', right: 'chat'}}]);

// remove the right secondary node
router.createUrlTree(['/team', 33, {outlets: {primary: 'user/11', right: null}}]);

// assuming the current url is `/team/33/user/11` and the route points to `user/11`

// navigate to /team/33/user/11/details
router.createUrlTree(['details'], {relativeTo: route});

// navigate to /team/33/user/22
router.createUrlTree(['../22'], {relativeTo: route});

// navigate to /team/44/user/22
router.createUrlTree(['../../team/44/user/22'], {relativeTo: route});
```

Note that a value of `null` or `undefined` for `relativeTo` indicates that the tree should be created relative to the root.

### navigateByUrl

`Promise<boolean>`

Navigates to a view using an absolute route path.

@paramurl`string | UrlTree`

An absolute path for a defined route. The function does not apply any delta to the current URL.

@paramextras`NavigationBehaviorOptions`

An object containing properties that modify the navigation strategy.

@returns`Promise<boolean>`

Usage notes

The following calls request navigation to an absolute path.

```
router.navigateByUrl("/team/33/user/11");

// Navigate without updating the URL
router.navigateByUrl("/team/33/user/11", { skipLocationChange: true });
```

### navigate

`Promise<boolean>`

Navigate based on the provided array of commands and a starting point. If no starting route is provided, the navigation is absolute.

@paramcommands`readonly any[]`

An array of URL fragments with which to construct the target URL. If the path is static, can be the literal URL string. For a dynamic path, pass an array of path segments, followed by the parameters for each segment. The fragments are applied to the current URL or the one provided in the `relativeTo` property of the options object, if supplied.

@paramextras`NavigationExtras`

An options object that determines how the URL should be constructed or interpreted.

@returns`Promise<boolean>`

Usage notes

The following calls request navigation to a dynamic route path relative to the current URL.

```
router.navigate(['team', 33, 'user', 11], {relativeTo: route});

// Navigate without updating the URL, overriding the default behavior
router.navigate(['team', 33, 'user', 11], {relativeTo: route, skipLocationChange: true});
```

### serializeUrl

`string`

Serializes a [`UrlTree`](urltree) into a string

@paramurl`UrlTree`

@returns`string`

### parseUrl

`UrlTree`

Parses a string into a [`UrlTree`](urltree)

@paramurl`string`

@returns`UrlTree`

### isActive

3 overloads

Returns whether the url is activated.

@deprecated

Use [`IsActiveMatchOptions`](isactivematchoptions) instead.

- The equivalent [`IsActiveMatchOptions`](isactivematchoptions) for `true` is `{paths: 'exact', queryParams: 'exact', fragment: 'ignored', matrixParams: 'ignored'}`.
- The equivalent for `false` is `{paths: 'subset', queryParams: 'subset', fragment: 'ignored', matrixParams: 'ignored'}`.

@paramurl`string | UrlTree`

@paramexact`boolean`

@returns`boolean`

Returns whether the url is activated.

@paramurl`string | UrlTree`

@parammatchOptions`IsActiveMatchOptions`

@returns`boolean`

@paramurl`string | UrlTree`

@parammatchOptions`boolean | IsActiveMatchOptions`

@returns`boolean`

## Description

A service that facilitates navigation among views and URL manipulation capabilities. This service is provided in the root scope and configured with [provideRouter](providerouter).

---

## Exported by

- `RouterModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/Router>
