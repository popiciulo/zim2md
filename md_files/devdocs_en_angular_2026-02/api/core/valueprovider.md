# ValueProvider

ValueProvider



# ValueProvider

Configures the [`Injector`](injector) to return a value for a token.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface ValueProvider extends ValueSansProvider {
  provide: any;
  multi?: boolean | undefined;
  override useValue: any;
}
```

### provide

`any`

An injection token. Typically an instance of [`Type`](type) or [`InjectionToken`](injectiontoken), but can be `any`.

### multi

`boolean | undefined`

When true, injector returns an array of instances. This is useful to allow multiple providers spread across many files to provide configuration information to a common token.

### useValue

`any`

The value to inject.

## Usage Notes

### Example

```
const injector = Injector.create({providers: [{provide: String, useValue: 'Hello'}]});

        expect(injector.get(String)).toEqual('Hello');
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
<https://angular.dev/api/core/ValueProvider>
