# SkipSelf

SkipSelf



# SkipSelf

Parameter decorator to be used on constructor parameters, which tells the DI framework to start dependency resolution from the parent injector. Resolution works upward through the injector hierarchy, so the local injector is not checked for a provider.

[Dependency Injection guide](../../guide/di/di-in-action#skip)[Self](self)[Optional](optional)

## API

```
@SkipSelf();
```

## Usage Notes

In the following example, the dependency can be resolved when instantiating a child, but not when instantiating the class itself.

```
class Dependency {}

        @Injectable()
        class NeedsDependency {
          constructor(@SkipSelf() public dependency: Dependency) {}
        }

        const parent = Injector.create({providers: [{provide: Dependency, deps: []}]});
        const child = Injector.create({
          providers: [{provide: NeedsDependency, deps: [Dependency]}],
          parent,
        });
        expect(child.get(NeedsDependency).dependency instanceof Dependency).toBe(true);

        const inj = Injector.create({
          providers: [{provide: NeedsDependency, deps: [[new Self(), Dependency]]}],
        });
        expect(() => inj.get(NeedsDependency)).toThrowError();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/SkipSelf>
