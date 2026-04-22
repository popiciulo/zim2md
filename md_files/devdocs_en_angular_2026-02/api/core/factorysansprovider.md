# FactorySansProvider

FactorySansProvider



# FactorySansProvider

Configures the [`Injector`](injector) to return a value by invoking a `useFactory` function.

[FactoryProvider](factoryprovider)[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface FactorySansProvider {
  useFactory: Function;
  deps?: any[] | undefined;
}
```

### useFactory

`Function`

A function to invoke to create a value for this `token`. The function is invoked with resolved values of `token`s in the `deps` field.

### deps

`any[] | undefined`

A list of `token`s to be resolved by the injector. The list of values is then used as arguments to the `useFactory` function.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/FactorySansProvider>
