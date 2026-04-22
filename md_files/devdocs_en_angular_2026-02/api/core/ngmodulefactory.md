# NgModuleFactory

NgModuleFactory



# NgModuleFactory

Deprecation warning

This class was mostly used as a part of ViewEngine-based JIT API and is no longer needed in Ivy JIT mode. Angular provides APIs that accept NgModule classes directly (such as [PlatformRef.bootstrapModule](platformref#bootstrapModule) and [createNgModule](createngmodule)), consider switching to those APIs instead of using factory-based ones.

## API

```
abstract class NgModuleFactory<T> {
  abstract readonly moduleType: Type<T>;
  abstract create(parentInjector: Injector | null): NgModuleRef<T>;
}
```

### moduleType

`Type<T>`

### create

`NgModuleRef<T>`

@paramparentInjector`Injector | null`

@returns`NgModuleRef<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/NgModuleFactory>
