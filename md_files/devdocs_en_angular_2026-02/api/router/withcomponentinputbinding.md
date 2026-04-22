# withComponentInputBinding

withComponentInputBinding



# withComponentInputBinding

Enables binding information from the [`Router`](router) state directly to the inputs of the component in [`Route`](route) configurations.

[Input Transforms](../../guide/components/inputs#input-transforms)

## API

```
function withComponentInputBinding(): ComponentInputBindingFeature;
```

### withComponentInputBinding

`ComponentInputBindingFeature`

Enables binding information from the [`Router`](router) state directly to the inputs of the component in [`Route`](route) configurations.

@returns`ComponentInputBindingFeature`

Usage notes

Basic example of how you can enable the feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withComponentInputBinding())
    ]
  }
);
```

The router bindings information from any of the following sources:

- query parameters
- path and matrix parameters
- static route data
- data from resolvers

Duplicate keys are resolved in the same order from above, from least to greatest, meaning that resolvers have the highest precedence and override any of the other information from the route.

Importantly, when an input does not have an item in the route data with a matching key, this input is set to `undefined`. This prevents previous information from being retained if the data got removed from the route (i.e. if a query parameter is removed). Default values can be provided with a resolver on the route to ensure the value is always present or an input and use an input transform in the component.

## Usage Notes

Basic example of how you can enable the feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withComponentInputBinding())
    ]
  }
);
```

The router bindings information from any of the following sources:

- query parameters
- path and matrix parameters
- static route data
- data from resolvers

Duplicate keys are resolved in the same order from above, from least to greatest, meaning that resolvers have the highest precedence and override any of the other information from the route.

Importantly, when an input does not have an item in the route data with a matching key, this input is set to `undefined`. This prevents previous information from being retained if the data got removed from the route (i.e. if a query parameter is removed). Default values can be provided with a resolver on the route to ensure the value is always present or an input and use an input transform in the component.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withComponentInputBinding>
