# inject

inject



# inject

Injects a token from the currently active injector. [`inject`](inject) is only supported in an [injection context](../../guide/di/dependency-injection-context). It can be used during:

- Construction (via the `constructor`) of a class being instantiated by the DI system, such as an [`@Injectable`](injectable) or [`@Component`](component).
- In the initializer for fields of such classes.
- In the factory function specified for `useFactory` of a [`Provider`](provider) or an [`@Injectable`](injectable).
- In the `factory` function specified for an [`InjectionToken`](injectiontoken).
- In a stackframe of a function call in a DI context

[Injecting dependencies with inject()](../../guide/di#injecting-dependencies-with-inject)

## API

```
function inject<T>(token: ProviderToken<T>): T;
function inject<T>(
  token: ProviderToken<T>,
  options: InjectOptions & { optional?: false | undefined },
): T;
function inject<T>(token: ProviderToken<T>, options: InjectOptions): T | null;
function inject(token: HostAttributeToken): string;
function inject(
  token: HostAttributeToken,
  options: { optional: true },
): string | null;
function inject(
  token: HostAttributeToken,
  options: { optional: false },
): string;
```

```
function inject<T>(token: ProviderToken<T>): T;
```

@paramtoken`ProviderToken<T>`

A token that represents a dependency that should be injected.

@returns`T`

```
function inject<T>(token: ProviderToken<T>, options: InjectOptions & { optional?: false | undefined; }): T;
```

@paramtoken`ProviderToken<T>`

A token that represents a dependency that should be injected.

@paramoptions`InjectOptions & { optional?: false | undefined; }`

Control how injection is executed. Options correspond to injection strategies that can be specified with parameter decorators [`@Host`](host), [`@Self`](self), [`@SkipSelf`](skipself), and [`@Optional`](optional).

@returns`T`

```
function inject<T>(token: ProviderToken<T>, options: InjectOptions): T | null;
```

@paramtoken`ProviderToken<T>`

A token that represents a dependency that should be injected.

@paramoptions`InjectOptions`

Control how injection is executed. Options correspond to injection strategies that can be specified with parameter decorators [`@Host`](host), [`@Self`](self), [`@SkipSelf`](skipself), and [`@Optional`](optional).

@returns`T | null`

```
function inject(token: HostAttributeToken): string;
```

@paramtoken`HostAttributeToken`

A token that represents a static attribute on the host node that should be injected.

@returns`string`

```
function inject(token: HostAttributeToken, options: { optional: true; }): string | null;
```

@paramtoken`HostAttributeToken`

A token that represents a static attribute on the host node that should be injected.

@paramoptions`{ optional: true; }`

@returns`string | null`

```
function inject(token: HostAttributeToken, options: { optional: false; }): string;
```

@paramtoken`HostAttributeToken`

A token that represents a static attribute on the host node that should be injected.

@paramoptions`{ optional: false; }`

@returns`string`

## Usage Notes

In practice the [`inject()`](inject) calls are allowed in a constructor, a constructor parameter and a field initializer:

```
@Injectable({providedIn: 'root'})
export class Car {
  radio: Radio|undefined;
  // OK: field initializer
  spareTyre = inject(Tyre);

  constructor() {
    // OK: constructor body
    this.radio = inject(Radio);
  }
}
```

It is also legal to call [`inject`](inject) from a provider's factory:

```
providers: [
  {provide: Car, useFactory: () => {
    // OK: a class factory
    const engine = inject(Engine);
    return new Car(engine);
  }}
]
```

Calls to the [`inject()`](inject) function outside of the class creation context will result in error. Most notably, calls to [`inject()`](inject) are disallowed after a class instance was created, in methods (including lifecycle hooks):

```
@Component({ ... })
export class CarComponent {
  ngOnInit() {
    // ERROR: too late, the component instance was already created
    const engine = inject(Engine);
    engine.start();
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/inject>
