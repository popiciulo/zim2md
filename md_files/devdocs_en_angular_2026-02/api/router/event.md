# Event

Event



# Event

Router events that allow you to track the lifecycle of the router.

## API

```
type Event = | NavigationStart
  | NavigationEnd
  | NavigationCancel
  | NavigationError
  | RoutesRecognized
  | GuardsCheckStart
  | GuardsCheckEnd
  | RouteConfigLoadStart
  | RouteConfigLoadEnd
  | ChildActivationStart
  | ChildActivationEnd
  | ActivationStart
  | ActivationEnd
  | Scroll
  | ResolveStart
  | ResolveEnd
  | NavigationSkipped
```

## Description

Router events that allow you to track the lifecycle of the router.

The events occur in the following sequence:

- [NavigationStart](navigationstart): Navigation starts.
- [RouteConfigLoadStart](routeconfigloadstart): Before the router [lazy loads](../../guide/routing/common-router-tasks#lazy-loading) a route configuration.
- [RouteConfigLoadEnd](routeconfigloadend): After a route has been lazy loaded.
- [RoutesRecognized](routesrecognized): When the router parses the URL and the routes are recognized.
- [GuardsCheckStart](guardscheckstart): When the router begins the *guards* phase of routing.
- [ChildActivationStart](childactivationstart): When the router begins activating a route's children.
- [ActivationStart](activationstart): When the router begins activating a route.
- [GuardsCheckEnd](guardscheckend): When the router finishes the *guards* phase of routing successfully.
- [ResolveStart](resolvestart): When the router begins the *resolve* phase of routing.
- [ResolveEnd](resolveend): When the router finishes the *resolve* phase of routing successfully.
- [ChildActivationEnd](childactivationend): When the router finishes activating a route's children.
- [ActivationEnd](activationend): When the router finishes activating a route.
- [NavigationEnd](navigationend): When navigation ends successfully.
- [NavigationCancel](navigationcancel): When navigation is canceled.
- [NavigationError](navigationerror): When navigation fails due to an unexpected error.
- [Scroll](scroll): When the user scrolls.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/Event>
