# Injectable

Injectable



# Injectable

Decorator that marks a class as available to be provided and injected as a dependency.

[Introduction to Services and DI](../../guide/di)[Creating and using services](../../guide/di/creating-and-using-services)[Defining dependency providers](../../guide/di/defining-dependency-providers)

## API

```
@Injectable();
@Injectable(
  options?: {
    providedIn: Type<any> | 'root' | 'platform' | 'any' | null;
  } & InjectableProvider,
);
```

## Usage Notes

Marking a class with [`@Injectable`](injectable) ensures that the compiler will generate the necessary metadata to create the class's dependencies when the class is injected.

The following example shows how a service class is properly marked so that a supporting service can be injected upon creation.

```
@Injectable()
        class UsefulService {}

        @Injectable()
        class NeedsService {
          constructor(public service: UsefulService) {}
        }

        const injector = Injector.create({
          providers: [
            {provide: NeedsService, deps: [UsefulService]},
            {provide: UsefulService, deps: []},
          ],
        });
        expect(injector.get(NeedsService).service instanceof UsefulService).toBe(true);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Injectable>
