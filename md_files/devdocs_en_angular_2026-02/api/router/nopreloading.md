# NoPreloading

NoPreloading



# NoPreloading

Provides a preloading strategy that does not preload any modules.

[Preloading strategy](../../guide/routing/customizing-route-behavior#preloading-strategy)

## API

```
class NoPreloading implements PreloadingStrategy {
  preload(route: Route, fn: () => Observable<any>): Observable<any>;
}
```

### preload

`Observable<any>`

@paramroute`Route`

@paramfn`() => Observable<any>`

@returns`Observable<any>`

## Description

Provides a preloading strategy that does not preload any modules.

This strategy is enabled by default.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NoPreloading>
