# CanActivateChild

CanActivateChild



# CanActivateChild

Interface that a class can implement to be a guard deciding if a child route can be activated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

[CanActivateChild](../../guide/routing/route-guards#canactivatechild)

## API

```
interface CanActivateChild {
  canActivateChild(childRoute: ActivatedRouteSnapshot, state: RouterStateSnapshot): any;
}
```

### canActivateChild

`any`

@paramchildRoute`ActivatedRouteSnapshot`

@paramstate`RouterStateSnapshot`

@returns`any`

## Description

Interface that a class can implement to be a guard deciding if a child route can be activated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements a [`CanActivateChild`](canactivatechild) function that checks whether the current user has permission to activate the requested child route.

```
class UserToken {}
class Permissions {
  canActivate(user: UserToken, id: string): boolean {
    return true;
  }
}

@Injectable()
class CanActivateTeam implements CanActivateChild {
  constructor(private permissions: Permissions, private currentUser: UserToken) {}

  canActivateChild(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): MaybeAsync<GuardResult> {
    return this.permissions.canActivate(this.currentUser, route.params.id);
  }
}
```

Here, the defined guard function is provided as part of the [`Route`](route) object in the router configuration:

```
@NgModule({
  imports: [
    RouterModule.forRoot([
      {
        path: 'root',
        canActivateChild: [CanActivateTeam],
        children: [
          {
             path: 'team/:id',
             component: TeamComponent
          }
        ]
      }
    ])
  ],
  providers: [CanActivateTeam, UserToken, Permissions]
})
class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanActivateChild>
