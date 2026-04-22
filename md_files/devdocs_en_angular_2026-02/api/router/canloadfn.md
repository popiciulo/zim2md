# CanLoadFn

CanLoadFn



# CanLoadFn

The signature of a function used as a `canLoad` guard on a [`Route`](route).

[CanLoad](canload)[Route](route)[CanMatch](canmatch)

Deprecation warning

Use [`Route.canMatch`](route#canMatch) and [`CanMatchFn`](canmatchfn) instead

## API

```
type CanLoadFn = (route: Route, segments: UrlSegment[]) => MaybeAsync<GuardResult>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanLoadFn>
