# withEnabledBlockingInitialNavigation

withEnabledBlockingInitialNavigation



# withEnabledBlockingInitialNavigation

Configures initial navigation to start before the root component is created.

[provideRouter](providerouter)

## API

```
function withEnabledBlockingInitialNavigation(): EnabledBlockingInitialNavigationFeature;
```

### withEnabledBlockingInitialNavigation

`EnabledBlockingInitialNavigationFeature`

Configures initial navigation to start before the root component is created.

The bootstrap is blocked until the initial navigation is complete. This should be set in case you use [server-side rendering](../../guide/ssr), but do not enable [hydration](../../guide/hydration) for your application.

@returns`EnabledBlockingInitialNavigationFeature`

Usage notes

Basic example of how you can enable this navigation behavior:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withEnabledBlockingInitialNavigation())
    ]
  }
);
```

## Description

Configures initial navigation to start before the root component is created.

The bootstrap is blocked until the initial navigation is complete. This should be set in case you use [server-side rendering](../../guide/ssr), but do not enable [hydration](../../guide/hydration) for your application.

## Usage Notes

Basic example of how you can enable this navigation behavior:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withEnabledBlockingInitialNavigation())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withEnabledBlockingInitialNavigation>
