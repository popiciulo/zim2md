# DeprecatedResolve

DeprecatedResolve



# DeprecatedResolve

The [`InjectionToken`](../core/injectiontoken) and [`@Injectable`](../core/injectable) classes for resolvers are deprecated in favor of plain JavaScript functions instead. Dependency injection can still be achieved using the [`inject`](../core/inject) function from `@angular/core` and an injectable class can be used as a functional guard using [`inject`](../core/inject): `myResolvedData: () => inject(MyResolver).resolve()`.

[ResolveFn](resolvefn)[inject](../core/inject)

## API

```
type DeprecatedResolve = DeprecatedGuard | any
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/DeprecatedResolve>
