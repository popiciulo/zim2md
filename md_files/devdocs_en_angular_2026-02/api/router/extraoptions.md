# ExtraOptions

ExtraOptions



# ExtraOptions

A set of configuration options for a router module, provided in the `forRoot()` method.

[forRoot](routermodule#forRoot)

## API

```
interface ExtraOptions extends InMemoryScrollingOptions, RouterConfigOptions {
  enableTracing?: boolean | undefined;
  useHash?: boolean | undefined;
  initialNavigation?: InitialNavigation | undefined;
  bindToComponentInputs?: boolean | undefined;
  enableViewTransitions?: boolean | undefined;
  errorHandler?: ((error: any) => any) | undefined;
  preloadingStrategy?: any;
  scrollOffset?: [number, number] | (() => [number, number]) | undefined;
  override anchorScrolling?: "disabled" | "enabled" | undefined;
  override scrollPositionRestoration?: "disabled" | "enabled" | "top" | undefined;
  override canceledNavigationResolution?: "replace" | "computed" | undefined;
  override onSameUrlNavigation?: OnSameUrlNavigation | undefined;
  override paramsInheritanceStrategy?: "emptyOnly" | "always" | undefined;
  override urlUpdateStrategy?: "deferred" | "eager" | undefined;
  override defaultQueryParamsHandling?: QueryParamsHandling | undefined;
  override resolveNavigationPromiseOnError?: boolean | undefined;
}
```

### enableTracing

`boolean | undefined`

When true, log all internal navigation events to the console. Use for debugging.

### useHash

`boolean | undefined`

When true, enable the location strategy that uses the URL fragment instead of the history API.

### initialNavigation

`InitialNavigation | undefined`

One of `enabled`, `enabledBlocking`, `enabledNonBlocking` or `disabled`. When set to `enabled` or `enabledBlocking`, the initial navigation starts before the root component is created. The bootstrap is blocked until the initial navigation is complete. This value should be set in case you use [server-side rendering](../../guide/ssr), but do not enable [hydration](../../guide/hydration) for your application. When set to `enabledNonBlocking`, the initial navigation starts after the root component has been created. The bootstrap is not blocked on the completion of the initial navigation. When set to `disabled`, the initial navigation is not performed. The location listener is set up before the root component gets created. Use if there is a reason to have more control over when the router starts its initial navigation due to some complex initialization logic.

### bindToComponentInputs

`boolean | undefined`

When true, enables binding information from the [`Router`](router) state directly to the inputs of the component in [`Route`](route) configurations.

### enableViewTransitions

`boolean | undefined`

@experimental

When true, enables view transitions in the Router by running the route activation and deactivation inside of `document.startViewTransition`.

### errorHandler

`((error: any) => any) | undefined`

A custom error handler for failed navigations. If the handler returns a value, the navigation Promise is resolved with this value. If the handler throws an exception, the navigation Promise is rejected with the exception.

### preloadingStrategy

`any`

Configures a preloading strategy. One of [`PreloadAllModules`](preloadallmodules) or [`NoPreloading`](nopreloading) (the default).

### scrollOffset

`[number, number] | (() => [number, number]) | undefined`

Configures the scroll offset the router will use when scrolling to an element.

When given a tuple with x and y position value, the router uses that offset each time it scrolls. When given a function, the router invokes the function every time it restores scroll position.

### anchorScrolling

`"disabled" | "enabled" | undefined`

When set to 'enabled', scrolls to the anchor element when the URL has a fragment. Anchor scrolling is disabled by default.

Anchor scrolling does not happen on 'popstate'. Instead, we restore the position that we stored or scroll to the top.

### scrollPositionRestoration

`"disabled" | "enabled" | "top" | undefined`

Configures if the scroll position needs to be restored when navigating back.

- 'disabled'- (Default) Does nothing. Scroll position is maintained on navigation.
- 'top'- Sets the scroll position to x = 0, y = 0 on all navigation.
- 'enabled'- Restores the previous scroll position on backward navigation, else sets the position to the anchor if one is provided, or sets the scroll position to [0, 0] (forward navigation). This option will be the default in the future.

You can implement custom scroll restoration behavior by adapting the enabled behavior as in the following example.

```
class AppComponent {
  movieData: any;

  constructor(private router: Router, private viewportScroller: ViewportScroller,
changeDetectorRef: ChangeDetectorRef) {
  router.events.pipe(filter((event: Event): event is Scroll => event instanceof Scroll)
    ).subscribe(e => {
      fetch('http://example.com/movies.json').then(response => {
        this.movieData = response.json();
        // update the template with the data before restoring scroll
        changeDetectorRef.detectChanges();

        if (e.position) {
          viewportScroller.scrollToPosition(e.position);
        }
      });
    });
  }
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
<https://angular.dev/api/router/ExtraOptions>
