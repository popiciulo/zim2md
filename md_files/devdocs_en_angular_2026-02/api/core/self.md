# Self

Self



# Self

Parameter decorator to be used on constructor parameters, which tells the DI framework to start dependency resolution from the local injector.

[SkipSelf](skipself)[Optional](optional)

## API

```
@Self();
```

## Description

Parameter decorator to be used on constructor parameters, which tells the DI framework to start dependency resolution from the local injector.

Resolution works upward through the injector hierarchy, so the children of this class must configure their own providers or be prepared for a `null` result.

## Usage Notes

In the following example, the dependency can be resolved by the local injector when instantiating the class itself, but not when instantiating a child.

```
class Dependency {}

        @Injectable()
        class NeedsDependency {
          constructor(@Self() public dependency: Dependency) {}
        }

        let inj = Injector.create({
          providers: [
            {provide: Dependency, deps: []},
            {provide: NeedsDependency, deps: [[new Self(), Dependency]]},
          ],
        });
        const nd = inj.get(NeedsDependency);

        expect(nd.dependency instanceof Dependency).toBe(true);

        const child = Injector.create({
          providers: [{provide: NeedsDependency, deps: [[new Self(), Dependency]]}],
          parent: inj,
        });
        expect(() => child.get(NeedsDependency)).toThrowError();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Self>
