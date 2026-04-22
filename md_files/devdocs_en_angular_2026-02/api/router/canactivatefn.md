# CanActivateFn

CanActivateFn



# CanActivateFn

The signature of a function used as a `canActivate` guard on a [`Route`](route).

[Route](route)[CanActivate](../../guide/routing/route-guards#canactivate)

## API

```
type CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => MaybeAsync<GuardResult>
```

## Description

The signature of a function used as a `canActivate` guard on a [`Route`](route).

If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), the current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements and uses a [`CanActivateFn`](canactivatefn) that checks whether the current user has permission to activate the requested route.

```
@Injectable()
class UserToken {}

@Injectable()
class PermissionsService {
  canActivate(currentUser: UserToken, userId: string): boolean {
    return true;
  }
  canMatch(currentUser: UserToken): boolean {
    return true;
  }
}

const canActivateTeam: CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => {
  return inject(PermissionsService).canActivate(inject(UserToken), route.params['id']);
};
```

Here, the defined guard function is provided as part of the [`Route`](route) object in the router configuration:

```
bootstrapApplication(App, {
   providers: [
     provideRouter([
       {
         path: 'team/:id',
         component: TeamComponent,
         canActivate: [canActivateTeam],
       },
     ]),
   ],
 });
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanActivateFn>
