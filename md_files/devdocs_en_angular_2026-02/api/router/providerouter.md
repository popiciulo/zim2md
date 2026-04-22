# provideRouter

provideRouter



# provideRouter

Sets up providers necessary to enable [`Router`](router) functionality for the application. Allows to configure a set of routes as well as extra features that should be enabled.

[Router](../../guide/routing)[RouterFeatures](routerfeatures)

## API

```
function provideRouter(
  routes: Routes,
  ...features: RouterFeatures[]
): EnvironmentProviders;
```

### provideRouter

`EnvironmentProviders`

Sets up providers necessary to enable [`Router`](router) functionality for the application. Allows to configure a set of routes as well as extra features that should be enabled.

@paramroutes`Routes`

A set of [`Route`](route)s to use for the application routing table.

@paramfeatures`RouterFeatures[]`

Optional features to configure additional router behaviors.

@returns`EnvironmentProviders`

Usage notes

Basic example of how you can add a Router to your application:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent, {
  providers: [provideRouter(appRoutes)]
});
```

You can also enable optional features in the Router by adding functions from the [`RouterFeatures`](routerfeatures) type:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes,
        withDebugTracing(),
        withRouterConfig({paramsInheritanceStrategy: 'always'}))
    ]
  }
);
```

## Usage Notes

Basic example of how you can add a Router to your application:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent, {
  providers: [provideRouter(appRoutes)]
});
```

You can also enable optional features in the Router by adding functions from the [`RouterFeatures`](routerfeatures) type:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes,
        withDebugTracing(),
        withRouterConfig({paramsInheritanceStrategy: 'always'}))
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/provideRouter>
