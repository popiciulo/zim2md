# CanMatchFn

CanMatchFn



# CanMatchFn

The signature of a function used as a `canMatch` guard on a [`Route`](route).

[Route](route)[CanMatch](../../guide/routing/route-guards#canmatch)

## API

```
type CanMatchFn = (route: Route, segments: UrlSegment[]) => MaybeAsync<GuardResult>
```

## Description

The signature of a function used as a `canMatch` guard on a [`Route`](route).

If all guards return `true`, navigation continues and the [`Router`](router) will use the [`Route`](route) during activation. If any guard returns `false`, the [`Route`](route) is skipped for matching and other [`Route`](route) configurations are processed instead.

The following example implements and uses a [`CanMatchFn`](canmatchfn) that checks whether the current user has permission to access the team page.

```
const canMatchTeam: CanMatchFn = (route: Route, segments: UrlSegment[]) => {
  return inject(PermissionsService).canMatch(inject(UserToken));
};

bootstrapApplication(App, {
  providers: [
    provideRouter([
      {
        path: 'team/:id',
        component: TeamComponent,
        canMatch: [canMatchTeam],
      },
    ]),
  ],
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanMatchFn>
