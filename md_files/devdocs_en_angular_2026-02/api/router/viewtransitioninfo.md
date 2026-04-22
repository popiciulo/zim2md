# ViewTransitionInfo

ViewTransitionInfo



# ViewTransitionInfo

The information passed to the `onViewTransitionCreated` function provided in the [`withViewTransitions`](withviewtransitions) feature options.

## API

```
interface ViewTransitionInfo {
  transition: ViewTransition;
  from: ActivatedRouteSnapshot;
  to: ActivatedRouteSnapshot;
}
```

### transition

`ViewTransition`

The `ViewTransition` returned by the call to `startViewTransition`.

### from

`ActivatedRouteSnapshot`

The [`ActivatedRouteSnapshot`](activatedroutesnapshot) that the navigation is transitioning from.

### to

`ActivatedRouteSnapshot`

The [`ActivatedRouteSnapshot`](activatedroutesnapshot) that the navigation is transitioning to.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ViewTransitionInfo>
