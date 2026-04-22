# RouterModule

RouterModule



# RouterModule

Adds directives and providers for in-app navigation among views defined in an application. Use the Angular [`Router`](router) service to declaratively specify application states and manage state transitions.

[Routing and Navigation guide](../../guide/routing/common-router-tasks)

## API

```
class RouterModule {
  static forRoot(routes: Routes, config?: ExtraOptions | undefined): ModuleWithProviders<RouterModule>;
  static forChild(routes: Routes): ModuleWithProviders<RouterModule>;
}
```

### forRoot

`ModuleWithProviders<RouterModule>`

Creates and configures a module with all the router providers and directives. Optionally sets up an application listener to perform an initial navigation.

When registering the NgModule at the root, import as follows:

```
@NgModule({
  imports: [RouterModule.forRoot(ROUTES)]
})
class MyNgModule {}
```

@paramroutes`Routes`

An array of [`Route`](route) objects that define the navigation paths for the application.

@paramconfig`ExtraOptions | undefined`

An [`ExtraOptions`](extraoptions) configuration object that controls how navigation is performed.

@returns`ModuleWithProviders<RouterModule>`

### forChild

`ModuleWithProviders<RouterModule>`

Creates a module with all the router directives and a provider registering routes, without creating a new Router service. When registering for submodules and lazy-loaded submodules, create the NgModule as follows:

```
@NgModule({
  imports: [RouterModule.forChild(ROUTES)]
})
class MyNgModule {}
```

@paramroutes`Routes`

An array of [`Route`](route) objects that define the navigation paths for the submodule.

@returns`ModuleWithProviders<RouterModule>`

## Description

Adds directives and providers for in-app navigation among views defined in an application. Use the Angular [`Router`](router) service to declaratively specify application states and manage state transitions.

You can import this NgModule multiple times, once for each lazy-loaded bundle. However, only one [`Router`](router) service can be active. To ensure this, there are two ways to register routes when importing this module:

- The `forRoot()` method creates an [`NgModule`](../core/ngmodule) that contains all the directives, the given routes, and the [`Router`](router) service itself.
- The `forChild()` method creates an [`NgModule`](../core/ngmodule) that contains all the directives and the given routes, but does not include the [`Router`](router) service.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterModule>
