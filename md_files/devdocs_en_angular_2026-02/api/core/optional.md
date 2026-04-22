# Optional

Optional



# Optional

Parameter decorator to be used on constructor parameters, which marks the parameter as being an optional dependency. The DI framework provides `null` if the dependency is not found.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
@Optional();
```

## Description

Parameter decorator to be used on constructor parameters, which marks the parameter as being an optional dependency. The DI framework provides `null` if the dependency is not found.

Can be used together with other parameter decorators that modify how dependency injection operates.

## Usage Notes

The following code allows the possibility of a `null` result:

```
class Engine {}

        @Injectable()
        class Car {
          constructor(@Optional() public engine: Engine) {}
        }

        const injector = Injector.create({
          providers: [{provide: Car, deps: [[new Optional(), Engine]]}],
        });
        expect(injector.get(Car).engine).toBeNull();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Optional>
