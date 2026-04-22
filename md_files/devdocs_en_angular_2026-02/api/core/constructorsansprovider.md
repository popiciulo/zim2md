# ConstructorSansProvider

ConstructorSansProvider



# ConstructorSansProvider

Configures the [`Injector`](injector) to return an instance of a token.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface ConstructorSansProvider {
  deps?: any[] | undefined;
}
```

### deps

`any[] | undefined`

A list of `token`s to be resolved by the injector.

## Usage Notes

```
@Injectable(SomeModule, {deps: []})
class MyService {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ConstructorSansProvider>
