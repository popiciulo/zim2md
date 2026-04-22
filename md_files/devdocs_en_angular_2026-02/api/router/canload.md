# CanLoad

CanLoad



# CanLoad

Interface that a class can implement to be a guard deciding if children can be loaded. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation starts to the [`UrlTree`](urltree) returned from the guard.

Deprecation warning

Use [`CanMatch`](canmatch) instead

## API

```
interface CanLoad {
  canLoad(route: Route, segments: UrlSegment[]): any;
}
```

### canLoad

`any`

@paramroute`Route`

@paramsegments`UrlSegment[]`

@returns`any`

## Description

Interface that a class can implement to be a guard deciding if children can be loaded. If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), current navigation is cancelled and a new navigation starts to the [`UrlTree`](urltree) returned from the guard.

The following example implements a [`CanLoad`](canload) function that decides whether the current user has permission to load requested child routes.

```
class UserToken {}
class Permissions {
  canLoadChildren(user: UserToken, id: string, segments: UrlSegment[]): boolean {
    return true;
  }
}

@Injectable()
class CanLoadTeamSection implements CanLoad {
  constructor(private permissions: Permissions, private currentUser: UserToken) {}

  canLoad(route: Route, segments: UrlSegment[]): Observable<boolean>|Promise<boolean>|boolean {
    return this.permissions.canLoadChildren(this.currentUser, route, segments);
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
        loadChildren: () => import('./team').then(mod => mod.TeamModule),
        canLoad: [CanLoadTeamSection]
      }
    ])
  ],
  providers: [CanLoadTeamSection, UserToken, Permissions]
})
class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanLoad>
