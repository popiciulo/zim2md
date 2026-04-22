# RedirectCommand

RedirectCommand



# RedirectCommand

Can be returned by a [`Router`](router) guard to instruct the [`Router`](router) to redirect rather than continue processing the path of the in-flight navigation. The `redirectTo` indicates *where* the new navigation should go to and the optional `navigationBehaviorOptions` can provide more information about *how* to perform the navigation.

[Routing guide](../../guide/routing/common-router-tasks#preventing-unauthorized-access)

## API

```
class RedirectCommand {
  constructor(redirectTo: UrlTree, navigationBehaviorOptions?: NavigationBehaviorOptions | undefined): RedirectCommand;
}
```

### constructor

`RedirectCommand`

@paramredirectTo`UrlTree`

@paramnavigationBehaviorOptions`NavigationBehaviorOptions | undefined`

@returns`RedirectCommand`

## Description

Can be returned by a [`Router`](router) guard to instruct the [`Router`](router) to redirect rather than continue processing the path of the in-flight navigation. The `redirectTo` indicates *where* the new navigation should go to and the optional `navigationBehaviorOptions` can provide more information about *how* to perform the navigation.

```
const route: Route = {
  path: "user/:userId",
  component: User,
  canActivate: [
    () => {
      const router = inject(Router);
      const authService = inject(AuthenticationService);

      if (!authService.isLoggedIn()) {
        const loginPath = router.parseUrl("/login");
        return new RedirectCommand(loginPath, {
          skipLocationChange: true,
        });
      }

      return true;
    },
  ],
};
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RedirectCommand>
