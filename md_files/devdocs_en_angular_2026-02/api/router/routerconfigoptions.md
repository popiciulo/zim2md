# RouterConfigOptions

RouterConfigOptions



# RouterConfigOptions

Extra configuration options that can be used with the [`withRouterConfig`](withrouterconfig) function.

[Router configuration options](../../guide/routing/customizing-route-behavior#router-configuration-options)

## API

```
interface RouterConfigOptions {
  canceledNavigationResolution?: "replace" | "computed" | undefined;
  onSameUrlNavigation?: OnSameUrlNavigation | undefined;
  paramsInheritanceStrategy?: "emptyOnly" | "always" | undefined;
  urlUpdateStrategy?: "deferred" | "eager" | undefined;
  defaultQueryParamsHandling?: QueryParamsHandling | undefined;
  resolveNavigationPromiseOnError?: boolean | undefined;
}
```

### canceledNavigationResolution

`"replace" | "computed" | undefined`

Configures how the Router attempts to restore state when a navigation is cancelled.

'replace' - Always uses `location.replaceState` to set the browser state to the state of the router before the navigation started. This means that if the URL of the browser is updated *before* the navigation is canceled, the Router will simply replace the item in history rather than trying to restore to the previous location in the session history. This happens most frequently with `urlUpdateStrategy: 'eager'` and navigations with the browser back/forward buttons.

'computed' - Will attempt to return to the same index in the session history that corresponds to the Angular route when the navigation gets cancelled. For example, if the browser back button is clicked and the navigation is cancelled, the Router will trigger a forward navigation and vice versa.

Note: the 'computed' option is incompatible with any [`UrlHandlingStrategy`](urlhandlingstrategy) which only handles a portion of the URL because the history restoration navigates to the previous place in the browser history rather than simply resetting a portion of the URL.

The default value is `replace` when not set.

### onSameUrlNavigation

`OnSameUrlNavigation | undefined`

Configures the default for handling a navigation request to the current URL.

If unset, the [`Router`](router) will use `'ignore'`.

### paramsInheritanceStrategy

`"emptyOnly" | "always" | undefined`

Defines how the router merges parameters, data, and resolved data from parent to child routes.

By default ('emptyOnly'), a route inherits the parent route's parameters when the route itself has an empty path (meaning its configured with path: '') or when the parent route doesn't have any component set.

Set to 'always' to enable unconditional inheritance of parent parameters.

Note that when dealing with matrix parameters, "parent" refers to the parent [`Route`](route) config which does not necessarily mean the "URL segment to the left". When the [`Route`](route) `path` contains multiple segments, the matrix parameters must appear on the last segment. For example, matrix parameters for `{path: 'a/b', component: MyComp}` should appear as `a/b;foo=bar` and not `a;foo=bar/b`.

### urlUpdateStrategy

`"deferred" | "eager" | undefined`

Defines when the router updates the browser URL. By default ('deferred'), update after successful navigation. Set to 'eager' if prefer to update the URL at the beginning of navigation. Updating the URL early allows you to handle a failure of navigation by showing an error message with the URL that failed.

### defaultQueryParamsHandling

`QueryParamsHandling | undefined`

The default strategy to use for handling query params in [`Router.createUrlTree`](router#createUrlTree) when one is not provided.

The `createUrlTree` method is used internally by [`Router.navigate`](router#navigate) and [`RouterLink`](routerlink). Note that [`QueryParamsHandling`](queryparamshandling) does not apply to [`Router.navigateByUrl`](router#navigateByUrl).

When neither the default nor the queryParamsHandling option is specified in the call to `createUrlTree`, the current parameters will be replaced by new parameters.

### resolveNavigationPromiseOnError

`boolean | undefined`

When `true`, the `Promise` will instead resolve with `false`, as it does with other failed navigations (for example, when guards are rejected).

Otherwise the `Promise` returned by the Router's navigation with be rejected if an error occurs.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterConfigOptions>
