# CanMatch

CanMatch



# CanMatch

Interface that a class can implement to be a guard deciding if a [`Route`](route) can be matched. If all guards return `true`, navigation continues and the [`Router`](router) will use the [`Route`](route) during activation. If any guard returns `false`, the [`Route`](route) is skipped for matching and other [`Route`](route) configurations are processed instead.

[CanMatch](../../guide/routing/route-guards#canmatch)

## API

```
interface CanMatch {
  canMatch(route: Route, segments: UrlSegment[]): any;
}
```

### canMatch

`any`

@paramroute`Route`

@paramsegments`UrlSegment[]`

@returns`any`

## Description

Interface that a class can implement to be a guard deciding if a [`Route`](route) can be matched. If all guards return `true`, navigation continues and the [`Router`](router) will use the [`Route`](route) during activation. If any guard returns `false`, the [`Route`](route) is skipped for matching and other [`Route`](route) configurations are processed instead.

The following example implements a [`CanMatch`](canmatch) function that decides whether the current user has permission to access the users page.

```
class UserToken {}
class Permissions {
  canAccess(user: UserToken, route: Route, segments: UrlSegment[]): boolean {
    return true;
  }
}

@Injectable()
class CanMatchTeamSection implements CanMatch {
  constructor(private permissions: Permissions, private currentUser: UserToken) {}

  canMatch(route: Route, segments: UrlSegment[]): Observable<boolean>|Promise<boolean>|boolean {
    return this.permissions.canAccess(this.currentUser, route, segments);
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
        canMatch: [CanMatchTeamSection]
      },
      {
        path: '**',
        component: NotFoundComponent
      }
    ])
  ],
  providers: [CanMatchTeamSection, UserToken, Permissions]
})
class AppModule {}
```

If the `CanMatchTeamSection` were to return `false`, the router would continue navigating to the `team/:id` URL, but would load the `NotFoundComponent` because the [`Route`](route) for `'team/:id'` could not be used for a URL match but the catch-all `**` [`Route`](route) did instead.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanMatch>
