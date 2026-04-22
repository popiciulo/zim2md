# RouterPreloader

RouterPreloader



# RouterPreloader

The preloader optimistically loads all router configurations to make navigations into lazily-loaded sections of the application faster.

## API

```
class RouterPreloader implements OnDestroy {
  constructor(router: Router, injector: EnvironmentInjector, preloadingStrategy: PreloadingStrategy, loader: RouterConfigLoader): RouterPreloader;
  setUpPreloading(): void;
  preload(): Observable<any>;
}
```

### constructor

`RouterPreloader`

@paramrouter`Router`

@paraminjector`EnvironmentInjector`

@parampreloadingStrategy`PreloadingStrategy`

@paramloader`RouterConfigLoader`

@returns`RouterPreloader`

### setUpPreloading

`void`

@returns`void`

### preload

`Observable<any>`

@returns`Observable<any>`

## Description

The preloader optimistically loads all router configurations to make navigations into lazily-loaded sections of the application faster.

The preloader runs in the background. When the router bootstraps, the preloader starts listening to all navigation events. After every such event, the preloader will check if any configurations can be loaded lazily.

If a route is protected by `canLoad` guards, the preloaded will not load it.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterPreloader>
