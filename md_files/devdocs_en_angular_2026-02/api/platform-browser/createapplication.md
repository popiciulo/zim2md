# createApplication

createApplication



# createApplication

Create an instance of an Angular application without bootstrapping any components. This is useful for the situation where one wants to decouple application environment creation (a platform and associated injectors) from rendering components on a screen. Components can be subsequently bootstrapped on the returned [`ApplicationRef`](../core/applicationref).

## API

```
function createApplication(
  options?: ApplicationConfig | undefined,
): Promise<ApplicationRef>;
```

### createApplication

`Promise<ApplicationRef>`

Create an instance of an Angular application without bootstrapping any components. This is useful for the situation where one wants to decouple application environment creation (a platform and associated injectors) from rendering components on a screen. Components can be subsequently bootstrapped on the returned [`ApplicationRef`](../core/applicationref).

@paramoptions`ApplicationConfig | undefined`

Extra configuration for the application environment, see [`ApplicationConfig`](../core/applicationconfig) for additional info.

@returns`Promise<ApplicationRef>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/createApplication>
