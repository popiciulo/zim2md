# NgModule

NgModule



# NgModule

Decorator that marks a class as an NgModule and supplies configuration metadata.

## API

```
@NgModule({
  providers?: (Provider | EnvironmentProviders)[] | undefined;
  declarations?: (any[] | Type<any>)[] | undefined;
  imports?: (any[] | Type<any> | ModuleWithProviders<{}>)[] | undefined;
  exports?: (any[] | Type<any>)[] | undefined;
  bootstrap?: (any[] | Type<any>)[] | undefined;
  schemas?: (any[] | SchemaMetadata)[] | undefined;
  id?: string | undefined;
  jit?: true | undefined;
})
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/NgModule>
