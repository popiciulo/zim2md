# FactoryProvider

FactoryProvider



# FactoryProvider

Configures the [`Injector`](injector) to return a value by invoking a `useFactory` function.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface FactoryProvider extends FactorySansProvider {
  provide: any;
  multi?: boolean | undefined;
  override useFactory: Function;
  override deps?: any[] | undefined;
}
```

### provide

`any`

An injection token. (Typically an instance of [`Type`](type) or [`InjectionToken`](injectiontoken), but can be `any`).

### multi

`boolean | undefined`

When true, injector returns an array of instances. This is useful to allow multiple providers spread across many files to provide configuration information to a common token.

### useFactory

`Function`

A function to invoke to create a value for this `token`. The function is invoked with resolved values of `token`s in the `deps` field.

### deps

`any[] | undefined`

A list of `token`s to be resolved by the injector. The list of values is then used as arguments to the `useFactory` function.

## Usage Notes

```
const Location = new InjectionToken('location');
        const Hash = new InjectionToken('hash');

        const injector = Injector.create({
          providers: [
            {provide: Location, useValue: 'https://angular.io/#someLocation'},
            {
              provide: Hash,
              useFactory: (location: string) => location.split('#')[1],
              deps: [Location],
            },
          ],
        });

        expect(injector.get(Hash)).toEqual('someLocation');
```

Dependencies can also be marked as optional:

```
const Location = new InjectionToken('location');
        const Hash = new InjectionToken('hash');

        const injector = Injector.create({
          providers: [
            {
              provide: Hash,
              useFactory: (location: string) => `Hash for: ${location}`,
              // use a nested array to define metadata for dependencies.
              deps: [[new Optional(), Location]],
            },
          ],
        });

        expect(injector.get(Hash)).toEqual('Hash for: null');
```

### Multi-value example

```
const locale = new InjectionToken<string[]>('locale');
        const injector = Injector.create({
          providers: [
            {provide: locale, multi: true, useValue: 'en'},
            {provide: locale, multi: true, useValue: 'sk'},
          ],
        });

        const locales: string[] = injector.get(locale);
        expect(locales).toEqual(['en', 'sk']);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/FactoryProvider>
