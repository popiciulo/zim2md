# RunGuardsAndResolvers

RunGuardsAndResolvers



# RunGuardsAndResolvers

A policy for when to run guards and resolvers on a route.

[Route#runGuardsAndResolvers](route#runGuardsAndResolvers)[Control when guards and resolvers execute](../../guide/routing/customizing-route-behavior#control-when-guards-and-resolvers-execute)

## API

```
type RunGuardsAndResolvers = | 'pathParamsChange'
  | 'pathParamsOrQueryParamsChange'
  | 'paramsChange'
  | 'paramsOrQueryParamsChange'
  | 'always'
  | ((from: ActivatedRouteSnapshot, to: ActivatedRouteSnapshot) => boolean)
```

## Description

A policy for when to run guards and resolvers on a route.

Guards and/or resolvers will always run when a route is activated or deactivated. When a route is unchanged, the default behavior is the same as `paramsChange`.

`paramsChange` : Rerun the guards and resolvers when path or path param changes. This does not include query parameters. This option is the default.

- `always` : Run on every execution.
- `pathParamsChange` : Rerun guards and resolvers when the path params change. This does not compare matrix or query parameters.
- `paramsOrQueryParamsChange` : Run when path, matrix, or query parameters change.
- `pathParamsOrQueryParamsChange` : Rerun guards and resolvers when the path params change or query params have changed. This does not include matrix parameters.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RunGuardsAndResolvers>
