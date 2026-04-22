# CanDeactivateFn

CanDeactivateFn



# CanDeactivateFn

The signature of a function used as a `canDeactivate` guard on a [`Route`](route).

[Route](route)[CanDeactivate](../../guide/routing/route-guards#candeactivate)

## API

```
type CanDeactivateFn<T> = (
  component: T,
  currentRoute: ActivatedRouteSnapshot,
  currentState: RouterStateSnapshot,
  nextState: RouterStateSnapshot,
) => MaybeAsync<GuardResult>
```

## Description

The signature of a function used as a `canDeactivate` guard on a [`Route`](route).

If all guards return `true`, navigation continues. If any guard returns `false`, navigation is cancelled. If any guard returns a [`UrlTree`](urltree), the current navigation is cancelled and a new navigation begins to the [`UrlTree`](urltree) returned from the guard.

The following example implements and uses a [`CanDeactivateFn`](candeactivatefn) that checks whether the user component has unsaved changes before navigating away from the route.

```
@Component({
  template: '',
})
export class UserComponent {
  hasUnsavedChanges = true;
}

bootstrapApplication(App, {
  providers: [
    provideRouter([
      {
        path: 'user/:id',
        component: UserComponent,
        canDeactivate: [(component: UserComponent) => !component.hasUnsavedChanges],
      },
    ]),
  ],
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/CanDeactivateFn>
