# makeEnvironmentProviders

makeEnvironmentProviders



# makeEnvironmentProviders

Wrap an array of [`Provider`](provider)s into [`EnvironmentProviders`](environmentproviders), preventing them from being accidentally referenced in [`@Component`](component) in a component injector.

## API

```
function makeEnvironmentProviders(
  providers: (Provider | EnvironmentProviders)[],
): EnvironmentProviders;
```

### makeEnvironmentProviders

`EnvironmentProviders`

Wrap an array of [`Provider`](provider)s into [`EnvironmentProviders`](environmentproviders), preventing them from being accidentally referenced in [`@Component`](component) in a component injector.

@paramproviders`(Provider | EnvironmentProviders)[]`

@returns`EnvironmentProviders`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/makeEnvironmentProviders>
