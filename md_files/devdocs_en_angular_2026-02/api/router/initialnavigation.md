# InitialNavigation

InitialNavigation



# InitialNavigation

Allowed values in an [`ExtraOptions`](extraoptions) object that configure when the router performs the initial navigation operation.

[forRoot](routermodule#forRoot)

## API

```
type InitialNavigation = 'disabled' | 'enabledBlocking' | 'enabledNonBlocking'
```

## Description

Allowed values in an [`ExtraOptions`](extraoptions) object that configure when the router performs the initial navigation operation.

- 'enabledNonBlocking' - (default) The initial navigation starts after the root component has been created. The bootstrap is not blocked on the completion of the initial navigation.
- 'enabledBlocking' - The initial navigation starts before the root component is created. The bootstrap is blocked until the initial navigation is complete. This value should be set in case you use [server-side rendering](../../guide/ssr), but do not enable [hydration](../../guide/hydration) for your application.
- 'disabled' - The initial navigation is not performed. The location listener is set up before the root component gets created. Use if there is a reason to have more control over when the router starts its initial navigation due to some complex initialization logic.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/InitialNavigation>
