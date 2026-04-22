# CanActivateChildFn

CanActivateChildFn



# CanActivateChildFn

The signature of a function used as a `canActivateChild` guard on a [`Route`](route).

[Route](route)[CanActivateChild](../../guide/routing/route-guards#canactivatechild)

## API

```
type CanActivateChildFn = (
  childRoute: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => MaybeAsync<GuardResult>
```

## Description

The signature of a function used as a `canActivateChild` guard on a [`Route`](route).

If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), the current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements a `canActivate` function that checks whether the current user has permission to activate the requested route.

```
const canActivateChildExample: CanActivateChildFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => {
  return inject(PermissionsService).canActivate(inject(UserToken), route.params['id']);
};

bootstrapApplication(App, {
  providers: [
    provideRouter([
      {
        path: 'team/:id',
        component: TeamComponent,
        canActivateChild: [canActivateChildExample],
        children: [],
      },
    ]),
  ],
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanActivateChildFn>
