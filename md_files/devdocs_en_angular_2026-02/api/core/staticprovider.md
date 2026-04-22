# StaticProvider

StaticProvider



# StaticProvider

Describes how an [`Injector`](injector) should be configured as static (that is, without reflection). A static provider provides tokens to an injector for various types of dependencies.

[Injector.create](injector#create)[Dependency Injection Guide](../../guide/di/dependency-injection-providers)

## API

```
type StaticProvider = | ValueProvider
  | ExistingProvider
  | StaticClassProvider
  | ConstructorProvider
  | FactoryProvider
  | any[]
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/StaticProvider>
