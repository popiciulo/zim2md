# EnvironmentProviders

EnvironmentProviders



# EnvironmentProviders

Encapsulated [`Provider`](provider)s that are only accepted during creation of an [`EnvironmentInjector`](environmentinjector) (e.g. in an [`NgModule`](ngmodule)).

[makeEnvironmentProviders](makeenvironmentproviders)[importProvidersFrom](importprovidersfrom)

## API

```
type EnvironmentProviders = {
  ɵbrand: 'EnvironmentProviders';
}
```

## Description

Encapsulated [`Provider`](provider)s that are only accepted during creation of an [`EnvironmentInjector`](environmentinjector) (e.g. in an [`NgModule`](ngmodule)).

Using this wrapper type prevents providers which are only designed to work in application/environment injectors from being accidentally included in [`@Component.providers`](component#providers) and ending up in a component injector.

This wrapper type prevents access to the [`Provider`](provider)s inside.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/EnvironmentProviders>
