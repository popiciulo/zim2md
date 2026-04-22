# PreloadAllModules

PreloadAllModules



# PreloadAllModules

Provides a preloading strategy that preloads all modules as quickly as possible.

[Preloading strategy](../../guide/routing/customizing-route-behavior#preloading-strategy)

## API

```
class PreloadAllModules implements PreloadingStrategy {
  preload(route: Route, fn: () => Observable<any>): Observable<any>;
}
```

### preload

`Observable<any>`

@paramroute`Route`

@paramfn`() => Observable<any>`

@returns`Observable<any>`

## Description

Provides a preloading strategy that preloads all modules as quickly as possible.

```
RouterModule.forRoot(ROUTES, {preloadingStrategy: PreloadAllModules})
```

```
export const appConfig: ApplicationConfig = {
providers: [
  provideRouter(
    routes,
    withPreloading(PreloadAllModules)
  )
]
};
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/PreloadAllModules>
