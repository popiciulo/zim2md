# withRouterConfig

withRouterConfig



# withRouterConfig

Allows to provide extra parameters to configure Router.

[provideRouter](providerouter)[Router configuration options](../../guide/routing/customizing-route-behavior#router-configuration-options)

## API

```
function withRouterConfig(
  options: RouterConfigOptions,
): RouterConfigurationFeature;
```

### withRouterConfig

`RouterConfigurationFeature`

Allows to provide extra parameters to configure Router.

@paramoptions`RouterConfigOptions`

A set of parameters to configure Router, see [`RouterConfigOptions`](routerconfigoptions) for additional information.

@returns`RouterConfigurationFeature`

Usage notes

Basic example of how you can provide extra configuration options:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withRouterConfig({
         onSameUrlNavigation: 'reload'
      }))
    ]
  }
);
```

## Usage Notes

Basic example of how you can provide extra configuration options:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withRouterConfig({
         onSameUrlNavigation: 'reload'
      }))
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withRouterConfig>
