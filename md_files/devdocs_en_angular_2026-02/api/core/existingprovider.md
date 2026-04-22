# ExistingProvider

ExistingProvider



# ExistingProvider

Configures the [`Injector`](injector) to return a value of another `useExisting` token.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface ExistingProvider extends ExistingSansProvider {
  provide: any;
  multi?: boolean | undefined;
  override useExisting: any;
}
```

### provide

`any`

An injection token. Typically an instance of [`Type`](type) or [`InjectionToken`](injectiontoken), but can be `any`.

### multi

`boolean | undefined`

When true, injector returns an array of instances. This is useful to allow multiple providers spread across many files to provide configuration information to a common token.

### useExisting

`any`

Existing `token` to return. (Equivalent to `injector.get(useExisting)`)

## Usage Notes

```
class Greeting {
          salutation = 'Hello';
        }

        class FormalGreeting extends Greeting {
          override salutation = 'Greetings';
        }

        const injector = Injector.create({
          providers: [
            {provide: FormalGreeting, deps: []},
            {provide: Greeting, useExisting: FormalGreeting},
          ],
        });

        expect(injector.get(Greeting).salutation).toEqual('Greetings');
        expect(injector.get(FormalGreeting).salutation).toEqual('Greetings');
        expect(injector.get(FormalGreeting)).toBe(injector.get(Greeting));
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
<https://angular.dev/api/core/ExistingProvider>
