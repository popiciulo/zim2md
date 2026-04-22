# Router reference

Router reference



# Router reference

  

The following sections highlight some core router concepts and terminology.

## Router events

During each navigation, the [`Router`](../../api/router/router) emits navigation events through the [`Router.events`](../../api/router/router#events) property. These events are shown in the following table.

| Router event | Details |
| --- | --- |
| [`NavigationStart`](../../api/router/navigationstart) | Triggered when navigation starts. |
| [`RouteConfigLoadStart`](../../api/router/routeconfigloadstart) | Triggered before the [`Router`](../../api/router/router) lazy loads a route configuration. |
| [`RouteConfigLoadEnd`](../../api/router/routeconfigloadend) | Triggered after a route has been lazy loaded. |
| [`RoutesRecognized`](../../api/router/routesrecognized) | Triggered when the Router parses the URL and the routes are recognized. |
| [`GuardsCheckStart`](../../api/router/guardscheckstart) | Triggered when the Router begins the Guards phase of routing. |
| [`ChildActivationStart`](../../api/router/childactivationstart) | Triggered when the Router begins activating a route's children. |
| [`ActivationStart`](../../api/router/activationstart) | Triggered when the Router begins activating a route. |
| [`GuardsCheckEnd`](../../api/router/guardscheckend) | Triggered when the Router finishes the Guards phase of routing successfully. |
| [`ResolveStart`](../../api/router/resolvestart) | Triggered when the Router begins the Resolve phase of routing. |
| [`ResolveEnd`](../../api/router/resolveend) | Triggered when the Router finishes the Resolve phase of routing successfully. |
| [`ChildActivationEnd`](../../api/router/childactivationend) | Triggered when the Router finishes activating a route's children. |
| [`ActivationEnd`](../../api/router/activationend) | Triggered when the Router finishes activating a route. |
| [`NavigationEnd`](../../api/router/navigationend) | Triggered when navigation ends successfully. |
| [`NavigationCancel`](../../api/router/navigationcancel) | Triggered when navigation is canceled. This can happen when a Route Guard returns false during navigation, or redirects by returning a [`UrlTree`](../../api/router/urltree) or [`RedirectCommand`](../../api/router/redirectcommand). |
| [`NavigationError`](../../api/router/navigationerror) | Triggered when navigation fails due to an unexpected error. |
| [`Scroll`](../../api/router/scroll) | Represents a scrolling event. |

When you enable the [`withDebugTracing`](../../api/router/withdebugtracing) feature, Angular logs these events to the console.

## Router terminology

Here are the key [`Router`](../../api/router/router) terms and their meanings:

| Router part | Details |
| --- | --- |
| [`Router`](../../api/router/router) | Displays the application component for the active URL. Manages navigation from one component to the next. |
| [`provideRouter`](../../api/router/providerouter) | provides the necessary service providers for navigating through application views. |
| [`RouterModule`](../../api/router/routermodule) | A separate NgModule that provides the necessary service providers and directives for navigating through application views. |
| [`Routes`](../../api/router/routes) | Defines an array of Routes, each mapping a URL path to a component. |
| [`Route`](../../api/router/route) | Defines how the router should navigate to a component based on a URL pattern. Most routes consist of a path and a component type. |
| [`RouterOutlet`](../../api/router/routeroutlet) | The directive (`<router-outlet>`) that marks where the router displays a view. |
| [`RouterLink`](../../api/router/routerlink) | The directive for binding a clickable HTML element to a route. Clicking an element with a `routerLink` directive that's bound to a *string* or a *link parameters array* triggers a navigation. |
| [`RouterLinkActive`](../../api/router/routerlinkactive) | The directive for adding/removing classes from an HTML element when an associated `routerLink` contained on or inside the element becomes active/inactive. It can also set the `aria-current` of an active link for better accessibility. |
| [`ActivatedRoute`](../../api/router/activatedroute) | A service that's provided to each route component that contains route specific information such as route parameters, static data, resolve data, global query parameters, and the global fragment. |
| [`RouterState`](../../api/router/routerstate) | The current state of the router including a tree of the currently activated routes together with convenience methods for traversing the route tree. |
| Link parameters array | An array that the router interprets as a routing instruction. You can bind that array to a [`RouterLink`](../../api/router/routerlink) or pass the array as an argument to the [`Router.navigate`](../../api/router/router#navigate) method. |
| Routing component | An Angular component with a [`RouterOutlet`](../../api/router/routeroutlet) that displays views based on router navigations. |

## <base href>

The router uses the browser's [history.pushState](https://developer.mozilla.org/docs/Web/API/History_API/Working_with_the_History_API#adding_and_modifying_history_entries "HTML5 browser history push-state") for navigation. `pushState` lets you customize in-application URL paths; for example, `localhost:4200/crisis-center`. The in-application URLs can be indistinguishable from server URLs.

Modern HTML5 browsers were the first to support `pushState` which is why many people refer to these URLs as "HTML5 style" URLs.

**HELPFUL:** HTML5 style navigation is the router default. In the [LocationStrategy and browser URL styles](https://angular.dev/common-router-tasks#locationstrategy-and-browser-url-styles) section, learn why HTML5 style is preferable, how to adjust its behavior, and how to switch to the older hash (`#`) style, if necessary.

You must add a [`<base href>` element](https://developer.mozilla.org/docs/Web/HTML/Element/base "base href") to the application's `index.html` for `pushState` routing to work. The browser uses the `<base href>` value to prefix relative URLs when referencing CSS files, scripts, and images.

Add the `<base>` element just after the `<head>` tag. If the `app` folder is the application root, as it is for this application, set the `href` value in `index.html` as shown here.

```
<base href="/">
```

### HTML5 URLs and the <base href>

The guidelines that follow will refer to different parts of a URL. This diagram outlines what those parts refer to:

```
foo://example.com:8042/over/there?name=ferret#nose
\_/   \______________/\_________/ \_________/ \__/
 |           |            |            |        |
scheme    authority      path        query   fragment
```

While the router uses the [HTML5 pushState](https://developer.mozilla.org/docs/Web/API/History_API#Adding_and_modifying_history_entries "Browser history push-state") style by default, you must configure that strategy with a `<base href>`.

The preferred way to configure the strategy is to add a [`<base href>` element](https://developer.mozilla.org/docs/Web/HTML/Element/base "base href") tag in the `<head>` of the `index.html`.

```
<base href="/">
```

Without that tag, the browser might not be able to load resources (images, CSS, scripts) when "deep linking" into the application.

Some developers might not be able to add the `<base>` element, perhaps because they don't have access to `<head>` or the `index.html`.

Those developers can still use HTML5 URLs by taking the following two steps:

1. Provide the router with an appropriate [`APP_BASE_HREF`](../../api/common/app_base_href) value.
2. Use root URLs (URLs with an `authority`) for all web resources: CSS, images, scripts, and template HTML files.
   - The `<base href>` `path` should end with a "/", as browsers ignore characters in the `path` that follow the right-most "`/`"
   - If the `<base href>` includes a [`query`](../../api/animations/query) part, the [`query`](../../api/animations/query) is only used if the `path` of a link in the page is empty and has no [`query`](../../api/animations/query). This means that a [`query`](../../api/animations/query) in the `<base href>` is only included when using [`HashLocationStrategy`](../../api/common/hashlocationstrategy).
   - If a link in the page is a root URL (has an `authority`), the `<base href>` is not used. In this way, an [`APP_BASE_HREF`](../../api/common/app_base_href) with an authority will cause all links created by Angular to ignore the `<base href>` value.
   - A fragment in the `<base href>` is *never* persisted

For more complete information on how `<base href>` is used to construct target URIs, see the [RFC](https://tools.ietf.org/html/rfc3986#section-5.2.2) section on transforming references.

### HashLocationStrategy

Use [`HashLocationStrategy`](../../api/common/hashlocationstrategy) by providing the `useHash: true` in an object as the second argument of the [`RouterModule.forRoot()`](../../api/router/routermodule#forRoot) in the `AppModule`.

```
providers: [
  provideRouter(appRoutes, withHashLocation())
]
```

When using [`RouterModule.forRoot`](../../api/router/routermodule#forRoot), this is configured with the `useHash: true` in the second argument: [`RouterModule.forRoot(routes, {useHash: true})`](#).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/routing/router-reference>
