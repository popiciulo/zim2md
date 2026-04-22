# EnvironmentInjector

EnvironmentInjector



# EnvironmentInjector

An [`Injector`](injector) that's part of the environment injector hierarchy, which exists outside of the component tree.

[Types of injector hierarchies](../../guide/di/hierarchical-dependency-injection#types-of-injector-hierarchies)

## API

```
abstract class EnvironmentInjector implements Injector {
  abstract get<T>(token: ProviderToken<T>, notFoundValue: undefined, options: InjectOptions & { optional?: false | undefined; }): T;
  abstract get<T>(token: ProviderToken<T>, notFoundValue: null | undefined, options: InjectOptions): T | null;
  abstract get<T>(token: ProviderToken<T>, notFoundValue?: T | undefined, options?: InjectOptions | undefined): T;
  abstract get<T>(token: string | ProviderToken<T>, notFoundValue?: any): any;
  abstract runInContext<ReturnT>(fn: () => ReturnT): ReturnT;
  abstract destroy(): void;
  abstract readonly destroyed: boolean;
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

### runInContext

`ReturnT`

Runs the given function in the context of this [`EnvironmentInjector`](environmentinjector).

Within the function's stack frame, [`inject`](inject) can be used to inject dependencies from this injector. Note that [`inject`](inject) is only usable synchronously, and cannot be used in any asynchronous callbacks or after any `await` points.

@deprecated

use the standalone function [`runInInjectionContext`](runininjectioncontext) instead

@paramfn`() => ReturnT`

the closure to be run in the context of this injector

@returns`ReturnT`

### destroy

`void`

@returns`void`

### destroyed

`boolean`

Indicates whether the instance has already been destroyed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/EnvironmentInjector>
