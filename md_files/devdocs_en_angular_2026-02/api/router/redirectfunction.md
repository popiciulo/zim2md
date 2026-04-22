# RedirectFunction

RedirectFunction



# RedirectFunction

The type for the function that can be used to handle redirects when the path matches a [`Route`](route) config.

[Route#redirectTo](route#redirectTo)

## API

```
type RedirectFunction = (
  redirectData: Pick<
    ActivatedRouteSnapshot,
    'routeConfig' | 'url' | 'params' | 'queryParams' | 'fragment' | 'data' | 'outlet' | 'title'
  >,
) => MaybeAsync<string | UrlTree>
```

## Description

The type for the function that can be used to handle redirects when the path matches a [`Route`](route) config.

The [`RedirectFunction`](redirectfunction) does *not* have access to the full [`ActivatedRouteSnapshot`](activatedroutesnapshot) interface. Some data are not accurately known at the route matching phase. For example, resolvers are not run until later, so any resolved title would not be populated. The same goes for lazy loaded components. This is also true for all the snapshots up to the root, so properties that include parents (root, parent, pathFromRoot) are also excluded. And naturally, the full route matching hasn't yet happened so firstChild and children are not available either.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RedirectFunction>
