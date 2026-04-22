# withViewTransitions

withViewTransitions



# withViewTransitions

Enables view transitions in the Router by running the route activation and deactivation inside of `document.startViewTransition`.

[Route transition animations](../../guide/routing/route-transition-animations)

## API

```
function withViewTransitions(
  options?: ViewTransitionsFeatureOptions | undefined,
): ViewTransitionsFeature;
```

### withViewTransitions

`ViewTransitionsFeature`

Enables view transitions in the Router by running the route activation and deactivation inside of `document.startViewTransition`.

Note: The View Transitions API is not available in all browsers. If the browser does not support view transitions, the Router will not attempt to start a view transition and continue processing the navigation as usual.

@paramoptions`ViewTransitionsFeatureOptions | undefined`

@returns`ViewTransitionsFeature`

Usage notes

Basic example of how you can enable the feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withViewTransitions())
    ]
  }
);
```

## Description

Enables view transitions in the Router by running the route activation and deactivation inside of `document.startViewTransition`.

Note: The View Transitions API is not available in all browsers. If the browser does not support view transitions, the Router will not attempt to start a view transition and continue processing the navigation as usual.

## Usage Notes

Basic example of how you can enable the feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withViewTransitions())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withViewTransitions>
