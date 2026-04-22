# withPreloading

withPreloading



# withPreloading

Allows to configure a preloading strategy to use. The strategy is configured by providing a reference to a class that implements a [`PreloadingStrategy`](preloadingstrategy).

[provideRouter](providerouter)[Preloading strategy](../../guide/routing/customizing-route-behavior#preloading-strategy)

## API

```
function withPreloading(
  preloadingStrategy: Type<PreloadingStrategy>,
): PreloadingFeature;
```

### withPreloading

`PreloadingFeature`

Allows to configure a preloading strategy to use. The strategy is configured by providing a reference to a class that implements a [`PreloadingStrategy`](preloadingstrategy).

@parampreloadingStrategy`Type<PreloadingStrategy>`

A reference to a class that implements a [`PreloadingStrategy`](preloadingstrategy) that should be used.

@returns`PreloadingFeature`

Usage notes

Basic example of how you can configure preloading:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withPreloading(PreloadAllModules))
    ]
  }
);
```

## Usage Notes

Basic example of how you can configure preloading:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withPreloading(PreloadAllModules))
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withPreloading>
