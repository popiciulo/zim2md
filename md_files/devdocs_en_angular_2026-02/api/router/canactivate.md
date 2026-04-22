# CanActivate

CanActivate



# CanActivate

Interface that a class can implement to be a guard deciding if a route can be activated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), the current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

[CanActivate](../../guide/routing/route-guards#canactivate)

## API

```
interface CanActivate {
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): any;
}
```

### canActivate

`any`

@paramroute`ActivatedRouteSnapshot`

@paramstate`RouterStateSnapshot`

@returns`any`

## Description

Interface that a class can implement to be a guard deciding if a route can be activated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), the current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements a [`CanActivate`](canactivate) function that checks whether the current user has permission to activate the requested route.

```
class UserToken {}
class Permissions {
  canActivate(): boolean {
    return true;
  }
}

@Injectable()
class CanActivateTeam implements CanActivate {
  constructor(private permissions: Permissions, private currentUser: UserToken) {}

  canActivate(
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
        path: 'team/:id',
        component: TeamComponent,
        canActivate: [CanActivateTeam]
      }
    ])
  ],
  providers: [CanActivateTeam, UserToken, Permissions]
})
class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanActivate>
