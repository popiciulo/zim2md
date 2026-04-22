# Route

Route



# Route

A configuration object that defines a single route. A set of routes are collected in a [`Routes`](routes) array to define a [`Router`](router) configuration. The router attempts to match segments of a given URL against each route, using the configuration options defined in this object.

## API

```
interface Route {
  title?: string | Type<Resolve<string>> | ResolveFn<string> | undefined;
  path?: string | undefined;
  pathMatch?: "prefix" | "full" | undefined;
  matcher?: UrlMatcher | undefined;
  component?: Type<any> | undefined;
  loadComponent?: (() => any) | undefined;
  redirectTo?: string | RedirectFunction | undefined;
  outlet?: string | undefined;
  canActivate?: (CanActivateFn | DeprecatedGuard)[] | undefined;
  canMatch?: (CanMatchFn | DeprecatedGuard)[] | undefined;
  canActivateChild?: (CanActivateChildFn | DeprecatedGuard)[] | undefined;
  canDeactivate?: (DeprecatedGuard | CanDeactivateFn<any>)[] | undefined;
  canLoad?: (DeprecatedGuard | CanLoadFn)[] | undefined;
  data?: Data | undefined;
  resolve?: ResolveData | undefined;
  children?: Routes | undefined;
  loadChildren?: LoadChildrenCallback | undefined;
  runGuardsAndResolvers?: RunGuardsAndResolvers | undefined;
  providers?: (EnvironmentProviders | Provider)[] | undefined;
}
```

### title

`string | Type<Resolve<string>> | ResolveFn<string> | undefined`

Used to define a page title for the route. This can be a static string or an [`Injectable`](../core/injectable) that implements [`Resolve`](resolve).

### path

`string | undefined`

The path to match against. Cannot be used together with a custom `matcher` function. A URL string that uses router matching notation. Can be a wild card (`**`) that matches any URL (see Usage Notes below). Default is "/" (the root path).

### pathMatch

`"prefix" | "full" | undefined`

The path-matching strategy, one of 'prefix' or 'full'. Default is 'prefix'.

By default, the router checks URL elements from the left to see if the URL matches a given path and stops when there is a config match. Importantly there must still be a config match for each segment of the URL. For example, '/team/11/user' matches the prefix 'team/:id' if one of the route's children matches the segment 'user'. That is, the URL '/team/11/user' matches the config `{path: 'team/:id', children: [{path: ':user', component: User}]}` but does not match when there are no children as in `{path: 'team/:id', component: Team}`.

The path-match strategy 'full' matches against the entire URL. It is important to do this when redirecting empty-path routes. Otherwise, because an empty path is a prefix of any URL, the router would apply the redirect even when navigating to the redirect destination, creating an endless loop.

### matcher

`UrlMatcher | undefined`

A custom URL-matching function. Cannot be used together with `path`.

### component

`Type<any> | undefined`

The component to instantiate when the path matches. Can be empty if child routes specify components.

### loadComponent

`(() => any) | undefined`

An object specifying a lazy-loaded component.

### redirectTo

`string | RedirectFunction | undefined`

A URL or function that returns a URL to redirect to when the path matches.

Absolute if the URL begins with a slash (/) or the function returns a [`UrlTree`](urltree), otherwise relative to the path URL.

The [`RedirectFunction`](redirectfunction) is run in an injection context so it can call [`inject`](../core/inject) to get any required dependencies.

When not present, router does not redirect.

### outlet

`string | undefined`

Name of a [`RouterOutlet`](routeroutlet) object where the component can be placed when the path matches.

### canActivate

`(CanActivateFn | DeprecatedGuard)[] | undefined`

An array of [`CanActivateFn`](canactivatefn) or DI tokens used to look up [`CanActivate()`](canactivate) handlers, in order to determine if the current user is allowed to activate the component. By default, any user can activate.

When using a function rather than DI tokens, the function can call [`inject`](../core/inject) to get any required dependencies. This [`inject`](../core/inject) call must be done in a synchronous context.

### canMatch

`(CanMatchFn | DeprecatedGuard)[] | undefined`

An array of [`CanMatchFn`](canmatchfn) or DI tokens used to look up [`CanMatch()`](canmatch) handlers, in order to determine if the current user is allowed to match the [`Route`](route). By default, any route can match.

When using a function rather than DI tokens, the function can call [`inject`](../core/inject) to get any required dependencies. This [`inject`](../core/inject) call must be done in a synchronous context.

### canActivateChild

`(CanActivateChildFn | DeprecatedGuard)[] | undefined`

An array of [`CanActivateChildFn`](canactivatechildfn) or DI tokens used to look up [`CanActivateChild()`](canactivatechild) handlers, in order to determine if the current user is allowed to activate a child of the component. By default, any user can activate a child.

When using a function rather than DI tokens, the function can call [`inject`](../core/inject) to get any required dependencies. This [`inject`](../core/inject) call must be done in a synchronous context.

### canDeactivate

`(DeprecatedGuard | CanDeactivateFn<any>)[] | undefined`

An array of [`CanDeactivateFn`](candeactivatefn) or DI tokens used to look up [`CanDeactivate()`](candeactivate) handlers, in order to determine if the current user is allowed to deactivate the component. By default, any user can deactivate.

When using a function rather than DI tokens, the function can call [`inject`](../core/inject) to get any required dependencies. This [`inject`](../core/inject) call must be done in a synchronous context.

### canLoad

`(DeprecatedGuard | CanLoadFn)[] | undefined`

@deprecated

Use `canMatch` instead

An array of [`CanLoadFn`](canloadfn) or DI tokens used to look up [`CanLoad()`](canload) handlers, in order to determine if the current user is allowed to load the component. By default, any user can load.

When using a function rather than DI tokens, the function can call [`inject`](../core/inject) to get any required dependencies. This [`inject`](../core/inject) call must be done in a synchronous context.

### data

`Data | undefined`

Additional developer-defined data provided to the component via [`ActivatedRoute`](activatedroute). By default, no additional data is passed.

### resolve

`ResolveData | undefined`

A map of DI tokens used to look up data resolvers. See [`Resolve`](resolve).

### children

`Routes | undefined`

An array of child [`Route`](route) objects that specifies a nested route configuration.

### loadChildren

`LoadChildrenCallback | undefined`

An object specifying lazy-loaded child routes.

### runGuardsAndResolvers

`RunGuardsAndResolvers | undefined`

A policy for when to run guards and resolvers on a route.

Guards and/or resolvers will always run when a route is activated or deactivated. When a route is unchanged, the default behavior is the same as `paramsChange`.

`paramsChange` : Rerun the guards and resolvers when path or path param changes. This does not include query parameters. This option is the default.

- `always` : Run on every execution.
- `pathParamsChange` : Rerun guards and resolvers when the path params change. This does not compare matrix or query parameters.
- `paramsOrQueryParamsChange` : Run when path, matrix, or query parameters change.
- `pathParamsOrQueryParamsChange` : Rerun guards and resolvers when the path params change or query params have changed. This does not include matrix parameters.

### providers

`(EnvironmentProviders | Provider)[] | undefined`

A [`Provider`](../core/provider) array to use for this [`Route`](route) and its `children`.

The [`Router`](router) will create a new [`EnvironmentInjector`](../core/environmentinjector) for this [`Route`](route) and use it for this [`Route`](route) and its `children`. If this route also has a `loadChildren` function which returns an `NgModuleRef`, this injector will be used as the parent of the lazy loaded module.

## Description

A configuration object that defines a single route. A set of routes are collected in a [`Routes`](routes) array to define a [`Router`](router) configuration. The router attempts to match segments of a given URL against each route, using the configuration options defined in this object.

Supports static, parameterized, redirect, and wildcard routes, as well as custom route data and resolve methods.

For detailed usage information, see the [Routing Guide](../../guide/routing/common-router-tasks).

## Usage Notes

### Simple Configuration

The following route specifies that when navigating to, for example, `/team/11/user/bob`, the router creates the 'Team' component with the 'User' child component in it.

```
[{
  path: 'team/:id',
 component: Team,
  children: [{
    path: 'user/:name',
    component: User
  }]
}]
```

### Multiple Outlets

The following route creates sibling components with multiple outlets. When navigating to `/team/11(aux:chat/jim)`, the router creates the 'Team' component next to the 'Chat' component. The 'Chat' component is placed into the 'aux' outlet.

```
[{
  path: 'team/:id',
  component: Team
}, {
  path: 'chat/:user',
  component: Chat
  outlet: 'aux'
}]
```

### Wild Cards

The following route uses wild-card notation to specify a component that is always instantiated regardless of where you navigate to.

```
[{
  path: '**',
  component: WildcardComponent
}]
```

### Redirects

The following route uses the `redirectTo` property to ignore a segment of a given URL when looking for a child path.

When navigating to '/team/11/legacy/user/jim', the router changes the URL segment '/team/11/legacy/user/jim' to '/team/11/user/jim', and then instantiates the Team component with the User child component in it.

```
[{
  path: 'team/:id',
  component: Team,
  children: [{
    path: 'legacy/user/:name',
    redirectTo: 'user/:name'
  }, {
    path: 'user/:name',
    component: User
  }]
}]
```

The redirect path can be relative, as shown in this example, or absolute. If we change the `redirectTo` value in the example to the absolute URL segment '/user/:name', the result URL is also absolute, '/user/jim'.

### Empty Path

Empty-path route configurations can be used to instantiate components that do not 'consume' any URL segments.

In the following configuration, when navigating to `/team/11`, the router instantiates the 'AllUsers' component.

```
[{
  path: 'team/:id',
  component: Team,
  children: [{
    path: '',
    component: AllUsers
  }, {
    path: 'user/:name',
    component: User
  }]
}]
```

Empty-path routes can have children. In the following example, when navigating to `/team/11/user/jim`, the router instantiates the wrapper component with the user component in it.

Note that an empty path route inherits its parent's parameters and data.

```
[{
  path: 'team/:id',
  component: Team,
  children: [{
    path: '',
    component: WrapperCmp,
    children: [{
      path: 'user/:name',
      component: User
    }]
  }]
}]
```

### Matching Strategy

The default path-match strategy is 'prefix', which means that the router checks URL elements from the left to see if the URL matches a specified path. For example, '/team/11/user' matches 'team/:id'.

```
[{
  path: '',
  pathMatch: 'prefix', //default
  redirectTo: 'main'
}, {
  path: 'main',
  component: Main
}]
```

You can specify the path-match strategy 'full' to make sure that the path covers the whole unconsumed URL. It is important to do this when redirecting empty-path routes. Otherwise, because an empty path is a prefix of any URL, the router would apply the redirect even when navigating to the redirect destination, creating an endless loop.

In the following example, supplying the 'full' `pathMatch` strategy ensures that the router applies the redirect if and only if navigating to '/'.

```
[{
  path: '',
  pathMatch: 'full',
  redirectTo: 'main'
}, {
  path: 'main',
  component: Main
}]
```

### Componentless Routes

You can share parameters between sibling components. For example, suppose that two sibling components should go next to each other, and both of them require an ID parameter. You can accomplish this using a route that does not specify a component at the top level.

In the following example, 'MainChild' and 'AuxChild' are siblings. When navigating to 'parent/10/(a//aux:b)', the route instantiates the main child and aux child components next to each other. For this to work, the application component must have the primary and aux outlets defined.

```
[{
   path: 'parent/:id',
   children: [
     { path: 'a', component: MainChild },
     { path: 'b', component: AuxChild, outlet: 'aux' }
   ]
}]
```

The router merges the parameters, data, and resolve of the componentless parent into the parameters, data, and resolve of the children.

This is especially useful when child components are defined with an empty path string, as in the following example. With this configuration, navigating to '/parent/10' creates the main child and aux components.

```
[{
   path: 'parent/:id',
   children: [
     { path: '', component: MainChild },
     { path: '', component: AuxChild, outlet: 'aux' }
   ]
}]
```

### Lazy Loading

Lazy loading speeds up application load time by splitting the application into multiple bundles and loading them on demand. To use lazy loading, provide the `loadChildren` property in the [`Route`](route) object, instead of the `children` property.

Given the following example route, the router will lazy load the associated module on demand using the browser native import system.

```
[{
  path: 'lazy',
  loadChildren: () => import('./lazy-route/lazy.module').then(mod => mod.LazyModule),
}];
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/Route>
