# InjectionToken

InjectionToken



# InjectionToken

Creates a token that can be used in a DI Provider.

[What is an InjectionToken?](../../guide/di/defining-dependency-providers#what-is-an-injectiontoken)

## API

```
class InjectionToken<T> {
  constructor(_desc: string, options?: { providedIn?: Type<any> | "root" | "platform" | "any" | null | undefined; factory: () => T; } | undefined): InjectionToken<T>;
  toString(): string;
}
```

### constructor

`InjectionToken<T>`

@param\_desc`string`

Description for the token, used only for debugging purposes, it should but does not need to be unique

@paramoptions`{ providedIn?: Type<any> | "root" | "platform" | "any" | null | undefined; factory: () => T; } | undefined`

Options for the token's usage, as described above

@returns`InjectionToken<T>`

### toString

`string`

@returns`string`

## Description

Creates a token that can be used in a DI Provider.

Use an [`InjectionToken`](injectiontoken) whenever the type you are injecting is not reified (does not have a runtime representation) such as when injecting an interface, callable type, array or parameterized type.

[`InjectionToken`](injectiontoken) is parameterized on `T` which is the type of object which will be returned by the [`Injector`](injector). This provides an additional level of type safety.

**Important Note**: Ensure that you use the same instance of the [`InjectionToken`](injectiontoken) in both the provider and the injection call. Creating a new instance of [`InjectionToken`](injectiontoken) in different places, even with the same description, will be treated as different tokens by Angular's DI system, leading to a `NullInjectorError`.

```
const TOKEN = new InjectionToken<MyInterface>('SomeToken');

// Setting up the provider using the same token instance
const providers = [
  {provide: TOKEN, useValue: {someProperty: 'exampleValue'}}, // Mock value for MyInterface
];

// Creating the injector with the provider
const injector = Injector.create({providers});

// Retrieving the value using the same token instance
const myInterface = injector.get(TOKEN);
// myInterface is inferred to be MyInterface.
```

When creating an [`InjectionToken`](injectiontoken), you can optionally specify a factory function which returns (possibly by creating) a default value of the parameterized type `T`. This sets up the [`InjectionToken`](injectiontoken) using this factory as a provider as if it was defined explicitly in the application's root injector. If the factory function, which takes zero arguments, needs to inject dependencies, it can do so using the [`inject`](inject) function. As you can see in the Tree-shakable InjectionToken example below.

Additionally, if a `factory` is specified you can also specify the `providedIn` option, which overrides the above behavior and marks the token as belonging to a particular [`@NgModule`](ngmodule) (note: this option is now deprecated). As mentioned above, `'root'` is the default value for `providedIn`.

The `providedIn: NgModule` and `providedIn: 'any'` options are deprecated.

## Usage Notes

### Basic Examples

### Plain InjectionToken

```
const BASE_URL = new InjectionToken<string>('BaseUrl');
      const injector = Injector.create({
        providers: [{provide: BASE_URL, useValue: 'http://localhost'}],
      });
      const url = injector.get(BASE_URL);
      // Note: since `BASE_URL` is `InjectionToken<string>`
      // `url` is correctly inferred to be `string`
      expect(url).toBe('http://localhost');
```

### Tree-shakable InjectionToken

```
class MyService {
        constructor(readonly myDep: MyDep) {}
      }

      const MY_SERVICE_TOKEN = new InjectionToken<MyService>('Manually constructed MyService', {
        providedIn: 'root',
        factory: () => new MyService(inject(MyDep)),
      });

      const instance = injector.get(MY_SERVICE_TOKEN);
      expect(instance instanceof MyService).toBeTruthy();
      expect(instance.myDep instanceof MyDep).toBeTruthy();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/InjectionToken>
