# withDisabledInitialNavigation

withDisabledInitialNavigation



# withDisabledInitialNavigation

Disables initial navigation.

[provideRouter](providerouter)

## API

```
function withDisabledInitialNavigation(): DisabledInitialNavigationFeature;
```

### withDisabledInitialNavigation

`DisabledInitialNavigationFeature`

Disables initial navigation.

Use if there is a reason to have more control over when the router starts its initial navigation due to some complex initialization logic.

@returns`DisabledInitialNavigationFeature`

Usage notes

Basic example of how you can disable initial navigation:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withDisabledInitialNavigation())
    ]
  }
);
```

## Description

Disables initial navigation.

Use if there is a reason to have more control over when the router starts its initial navigation due to some complex initialization logic.

## Usage Notes

Basic example of how you can disable initial navigation:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withDisabledInitialNavigation())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withDisabledInitialNavigation>
