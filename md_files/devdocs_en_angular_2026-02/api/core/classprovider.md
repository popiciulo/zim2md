# ClassProvider

ClassProvider



# ClassProvider

Configures the [`Injector`](injector) to return an instance of `useClass` for a token.

[Dependency Injection Guide](../../guide/di/dependency-injection)

## API

```
interface ClassProvider extends ClassSansProvider {
  provide: any;
  multi?: boolean | undefined;
  override useClass: Type<any>;
}
```

### provide

`any`

An injection token. (Typically an instance of [`Type`](type) or [`InjectionToken`](injectiontoken), but can be `any`).

### multi

`boolean | undefined`

When true, injector returns an array of instances. This is useful to allow multiple providers spread across many files to provide configuration information to a common token.

### useClass

`Type<any>`

Class to instantiate for the `token`.

## Usage Notes

```
abstract class Shape {
          name!: string;
        }

        class Square extends Shape {
          override name = 'square';
        }

        const injector = Injector.create({providers: [{provide: Shape, useValue: new Square()}]});

        const shape: Shape = injector.get(Shape);
        expect(shape.name).toEqual('square');
        expect(shape instanceof Square).toBe(true);
```

Note that following two providers are not equal:

```
class Greeting {
          salutation = 'Hello';
        }

        class FormalGreeting extends Greeting {
          override salutation = 'Greetings';
        }

        const injector = Injector.create({
          providers: [
            {provide: FormalGreeting, useClass: FormalGreeting},
            {provide: Greeting, useClass: FormalGreeting},
          ],
        });

        // The injector returns different instances.
        // See: {provide: ?, useExisting: ?} if you want the same instance.
        expect(injector.get(FormalGreeting)).not.toBe(injector.get(Greeting));
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
<https://angular.dev/api/core/ClassProvider>
