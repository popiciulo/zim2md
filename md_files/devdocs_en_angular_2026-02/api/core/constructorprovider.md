# ConstructorProvider

ConstructorProvider



# ConstructorProvider

Configures the [`Injector`](injector) to return an instance of a token.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface ConstructorProvider extends ConstructorSansProvider {
  provide: Type<any>;
  multi?: boolean | undefined;
  override deps?: any[] | undefined;
}
```

### provide

`Type<any>`

An injection token. Typically an instance of [`Type`](type) or [`InjectionToken`](injectiontoken), but can be `any`.

### multi

`boolean | undefined`

When true, injector returns an array of instances. This is useful to allow multiple providers spread across many files to provide configuration information to a common token.

### deps

`any[] | undefined`

A list of `token`s to be resolved by the injector.

## Usage Notes

```
class Square {
          name = 'square';
        }

        const injector = Injector.create({providers: [{provide: Square, deps: []}]});

        const shape: Square = injector.get(Square);
        expect(shape.name).toEqual('square');
        expect(shape instanceof Square).toBe(true);
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
<https://angular.dev/api/core/ConstructorProvider>
