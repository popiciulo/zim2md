# PreloadingStrategy

PreloadingStrategy



# PreloadingStrategy

Provides a preloading strategy.

[Preloading strategy](../../guide/routing/customizing-route-behavior#preloading-strategy)

## API

```
abstract class PreloadingStrategy {
  abstract preload(route: Route, fn: () => Observable<any>): Observable<any>;
}
```

### preload

`Observable<any>`

@paramroute`Route`

@paramfn`() => Observable<any>`

@returns`Observable<any>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/PreloadingStrategy>
