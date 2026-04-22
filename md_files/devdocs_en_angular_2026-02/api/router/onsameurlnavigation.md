# OnSameUrlNavigation

OnSameUrlNavigation



# OnSameUrlNavigation

How to handle a navigation request to the current URL. One of:

[RouteReuseStrategy](routereusestrategy)[RunGuardsAndResolvers](runguardsandresolvers)[NavigationBehaviorOptions](navigationbehavioroptions)[RouterConfigOptions](routerconfigoptions)

## API

```
type OnSameUrlNavigation = 'reload' | 'ignore'
```

## Description

How to handle a navigation request to the current URL. One of:

- `'ignore'` : The router ignores the request if it is the same as the current state.
- `'reload'` : The router processes the URL even if it is not different from the current state. One example of when you might want to use this option is if a `canMatch` guard depends on the application state and initially rejects navigation to a route. After fixing the state, you want to re-navigate to the same URL so that the route with the `canMatch` guard can activate.

Note that this only configures whether or not the Route reprocesses the URL and triggers related actions and events like redirects, guards, and resolvers. By default, the router re-uses a component instance when it re-navigates to the same component type without visiting a different component first. This behavior is configured by the [`RouteReuseStrategy`](routereusestrategy). In order to reload routed components on same url navigation, you need to set `onSameUrlNavigation` to `'reload'` *and* provide a [`RouteReuseStrategy`](routereusestrategy) which returns `false` for `shouldReuseRoute`. Additionally, resolvers and most guards for routes do not run unless the path or path params have changed (configured by `runGuardsAndResolvers`).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/OnSameUrlNavigation>
