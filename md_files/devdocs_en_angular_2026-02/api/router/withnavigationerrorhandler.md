# withNavigationErrorHandler

withNavigationErrorHandler



# withNavigationErrorHandler

Provides a function which is called when a navigation error occurs.

[NavigationError](navigationerror)[inject](../core/inject)[runInInjectionContext](../core/runininjectioncontext)[Centralize error handling in withNavigationErrorHandler](../../guide/routing/data-resolvers#centralize-error-handling-in-withnavigationerrorhandler)

## API

```
function withNavigationErrorHandler(
  handler: (error: NavigationError) => unknown,
): NavigationErrorHandlerFeature;
```

### withNavigationErrorHandler

`NavigationErrorHandlerFeature`

Provides a function which is called when a navigation error occurs.

This function is run inside application's [injection context](../../guide/di/dependency-injection-context) so you can use the [`inject`](../core/inject) function.

This function can return a [`RedirectCommand`](redirectcommand) to convert the error to a redirect, similar to returning a [`UrlTree`](urltree) or [`RedirectCommand`](redirectcommand) from a guard. This will also prevent the [`Router`](router) from emitting [`NavigationError`](navigationerror); it will instead emit [`NavigationCancel`](navigationcancel) with code NavigationCancellationCode.Redirect. Return values other than [`RedirectCommand`](redirectcommand) are ignored and do not change any behavior with respect to how the [`Router`](router) handles the error.

@paramhandler`(error: NavigationError) => unknown`

@returns`NavigationErrorHandlerFeature`

Usage notes

Basic example of how you can use the error handler option:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withNavigationErrorHandler((e: NavigationError) =>
inject(MyErrorTracker).trackError(e)))
    ]
  }
);
```

## Description

Provides a function which is called when a navigation error occurs.

This function is run inside application's [injection context](../../guide/di/dependency-injection-context) so you can use the [`inject`](../core/inject) function.

This function can return a [`RedirectCommand`](redirectcommand) to convert the error to a redirect, similar to returning a [`UrlTree`](urltree) or [`RedirectCommand`](redirectcommand) from a guard. This will also prevent the [`Router`](router) from emitting [`NavigationError`](navigationerror); it will instead emit [`NavigationCancel`](navigationcancel) with code NavigationCancellationCode.Redirect. Return values other than [`RedirectCommand`](redirectcommand) are ignored and do not change any behavior with respect to how the [`Router`](router) handles the error.

## Usage Notes

Basic example of how you can use the error handler option:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withNavigationErrorHandler((e: NavigationError) =>
inject(MyErrorTracker).trackError(e)))
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withNavigationErrorHandler>
