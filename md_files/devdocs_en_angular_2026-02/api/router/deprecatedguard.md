# DeprecatedGuard

DeprecatedGuard



# DeprecatedGuard

The [`InjectionToken`](../core/injectiontoken) and [`@Injectable`](../core/injectable) classes for guards are deprecated in favor of plain JavaScript functions instead. Dependency injection can still be achieved using the [`inject`](../core/inject) function from `@angular/core` and an injectable class can be used as a functional guard using [`inject`](../core/inject): `canActivate: [() => inject(myGuard).canActivate()]`.

[CanMatchFn](canmatchfn)[CanLoadFn](canloadfn)[CanActivateFn](canactivatefn)[CanActivateChildFn](canactivatechildfn)[CanDeactivateFn](candeactivatefn)[inject](../core/inject)

## API

```
type DeprecatedGuard = ProviderToken<any> | string
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/DeprecatedGuard>
