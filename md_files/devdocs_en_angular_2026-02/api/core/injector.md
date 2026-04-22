# Injector

Injector



# Injector

Concrete injectors implement this interface. Injectors are configured with [providers](../../guide/di/dependency-injection-providers) that associate dependencies of various types with [injection tokens](../../guide/di/dependency-injection-providers).

[DI Providers](../../guide/di/dependency-injection-providers)[StaticProvider](staticprovider)[Types of injector hierarchies](../../guide/di/hierarchical-dependency-injection#types-of-injector-hierarchies)

## API

```
abstract class Injector {
  abstract get<T>(token: ProviderToken<T>, notFoundValue: undefined, options: InjectOptions & { optional?: false | undefined; }): T;
  abstract get<T>(token: ProviderToken<T>, notFoundValue: null | undefined, options: InjectOptions): T | null;
  abstract get<T>(token: ProviderToken<T>, notFoundValue?: T | undefined, options?: InjectOptions | undefined): T;
  abstract get<T>(token: string | ProviderToken<T>, notFoundValue?: any): any;
  static THROW_IF_NOT_FOUND: {};
  static NULL: Injector;
  static create(providers: StaticProvider[], parent?: Injector | undefined): Injector;
  static create(options: { providers: (any[] | TypeProvider | ValueProvider | ClassProvider | ConstructorProvider | ExistingProvider | FactoryProvider | StaticClassProvider)[]; parent?: Injector | undefined; name?: string | undefined; }): DestroyableInjector;
}
```

### get

4 overloads

Retrieves an instance from the injector based on the provided token.

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`undefined`

@paramoptions`InjectOptions & { optional?: false | undefined; }`

@returns`T`

Retrieves an instance from the injector based on the provided token.

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`null | undefined`

@paramoptions`InjectOptions`

@returns`T | null`

Retrieves an instance from the injector based on the provided token.

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`T | undefined`

@paramoptions`InjectOptions | undefined`

@returns`T`

@deprecated

from v4.0.0 use ProviderToken

@paramtoken`string | ProviderToken<T>`

@paramnotFoundValue`any`

@returns`any`

### THROW\_IF\_NOT\_FOUND

`{}`

### NULL

`Injector`

### create

2 overloads

@deprecated

from v5 use the new signature Injector.create(options)

@paramproviders`StaticProvider[]`

@paramparent`Injector | undefined`

@returns`Injector`

Creates a new injector instance that provides one or more dependencies, according to a given type or types of [`StaticProvider`](staticprovider).

@paramoptions`{ providers: (any[] | TypeProvider | ValueProvider | ClassProvider | ConstructorProvider | ExistingProvider | FactoryProvider | StaticClassProvider)[]; parent?: Injector | undefined; name?: string | undefined; }`

An object with the following properties:

- `providers`: An array of providers of the [StaticProvider type](staticprovider).
- `parent`: (optional) A parent injector.
- `name`: (optional) A developer-defined identifying name for the new injector.

@returns`DestroyableInjector`

## Usage Notes

The following example creates a service injector instance.

```
class Square {
          name = 'square';
        }

        const injector = Injector.create({providers: [{provide: Square, deps: []}]});

        const shape: Square = injector.get(Square);
        expect(shape.name).toEqual('square');
        expect(shape instanceof Square).toBe(true);
```

### Usage example

```
const injector: Injector = Injector.create({
        providers: [{provide: 'validToken', useValue: 'Value'}],
      });
      expect(injector.get('validToken')).toEqual('Value');
      expect(() => injector.get('invalidToken')).toThrowError();
      expect(injector.get('invalidToken', 'notFound')).toEqual('notFound');
```

[`Injector`](injector) returns itself when given [`Injector`](injector) as a token:

```
const injector = Injector.create({providers: []});
      expect(injector.get(Injector)).toBe(injector);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Injector>
