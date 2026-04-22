# getNgModuleById

getNgModuleById



# getNgModuleById

Returns the NgModule class with the given id (specified using [@NgModule.id field](ngmodule#id)), if it exists and has been loaded. Classes for NgModules that do not specify an `id` cannot be retrieved. Throws if an NgModule cannot be found.

## API

```
function getNgModuleById<T>(id: string): Type<T>;
```

### getNgModuleById

`Type<T>`

Returns the NgModule class with the given id (specified using [@NgModule.id field](ngmodule#id)), if it exists and has been loaded. Classes for NgModules that do not specify an `id` cannot be retrieved. Throws if an NgModule cannot be found.

@paramid`string`

@returns`Type<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/getNgModuleById>
