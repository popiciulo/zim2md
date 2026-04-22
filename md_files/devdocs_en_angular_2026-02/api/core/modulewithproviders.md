# ModuleWithProviders

ModuleWithProviders



# ModuleWithProviders

A wrapper around an NgModule that associates it with providers Usage without a generic type is deprecated.

## API

```
interface ModuleWithProviders<T> {
  ngModule: Type<T>;
  providers?: (Provider | EnvironmentProviders)[] | undefined;
}
```

### ngModule

`Type<T>`

### providers

`(Provider | EnvironmentProviders)[] | undefined`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ModuleWithProviders>
