# DestroyableInjector

DestroyableInjector



# DestroyableInjector

An Injector that the owner can destroy and trigger the DestroyRef.destroy hooks.

## API

```
interface DestroyableInjector extends Injector {
  destroy(): void;
  abstract override get<T>(token: ProviderToken<T>, notFoundValue: undefined, options: InjectOptions & { optional?: false | undefined; }): T;
  abstract override get<T>(token: ProviderToken<T>, notFoundValue: null | undefined, options: InjectOptions): T | null;
  abstract override get<T>(token: ProviderToken<T>, notFoundValue?: T | undefined, options?: InjectOptions | undefined): T;
  abstract override get<T>(token: string | ProviderToken<T>, notFoundValue?: any): any;
}
```

### destroy

`void`

@returns`void`

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

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DestroyableInjector>
