# createNgModule

createNgModule



# createNgModule

Returns a new NgModuleRef instance based on the NgModule class and parent injector provided.

## API

```
function createNgModule<T>(
  ngModule: Type<T>,
  parentInjector?: Injector | undefined,
): NgModuleRef<T>;
```

### createNgModule

`NgModuleRef<T>`

Returns a new NgModuleRef instance based on the NgModule class and parent injector provided.

@paramngModule`Type<T>`

NgModule class.

@paramparentInjector`Injector | undefined`

Optional injector instance to use as a parent for the module injector. If not provided, `NullInjector` will be used instead.

@returns`NgModuleRef<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/createNgModule>
