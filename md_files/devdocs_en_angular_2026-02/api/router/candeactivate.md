# CanDeactivate

CanDeactivate



# CanDeactivate

Interface that a class can implement to be a guard deciding if a route can be deactivated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

[CanDeactivate](../../guide/routing/route-guards#candeactivate)

## API

```
interface CanDeactivate<T> {
  canDeactivate(component: T, currentRoute: ActivatedRouteSnapshot, currentState: RouterStateSnapshot, nextState: RouterStateSnapshot): any;
}
```

### canDeactivate

`any`

@paramcomponent`T`

@paramcurrentRoute`ActivatedRouteSnapshot`

@paramcurrentState`RouterStateSnapshot`

@paramnextState`RouterStateSnapshot`

@returns`any`

## Description

Interface that a class can implement to be a guard deciding if a route can be deactivated. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements a [`CanDeactivate`](candeactivate) function that checks whether the current user has permission to deactivate the requested route.

```
class UserToken {}
class Permissions {
  canDeactivate(user: UserToken, id: string): boolean {
    return true;
  }
}
```

Here, the defined guard function is provided as part of the [`Route`](route) object in the router configuration:

```
@Injectable()
class CanDeactivateTeam implements CanDeactivate<TeamComponent> {
  constructor(private permissions: Permissions, private currentUser: UserToken) {}

  canDeactivate(
    component: TeamComponent,
    currentRoute: ActivatedRouteSnapshot,
    currentState: RouterStateSnapshot,
    nextState: RouterStateSnapshot
  ): MaybeAsync<GuardResult> {
    return this.permissions.canDeactivate(this.currentUser, route.params.id);
  }
}

@NgModule({
  imports: [
    RouterModule.forRoot([
      {
        path: 'team/:id',
        component: TeamComponent,
        canDeactivate: [CanDeactivateTeam]
      }
    ])
  ],
  providers: [CanDeactivateTeam, UserToken, Permissions]
})
class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanDeactivate>
