# RxResourceOptions

RxResourceOptions



# RxResourceOptions

Like `ResourceOptions` but uses an RxJS-based `loader`.

## API

```
interface RxResourceOptions<T, R> extends BaseResourceOptions<T, R> {
  stream: (params: ResourceLoaderParams<R>) => Observable<T>;
  override params?: (() => R) | undefined;
  override defaultValue?: NoInfer<T> | undefined;
  override equal?: ValueEqualityFn<T> | undefined;
  override injector?: Injector | undefined;
}
```

### stream

`(params: ResourceLoaderParams<R>) => Observable<T>`

### params

`(() => R) | undefined`

A reactive function which determines the request to be made. Whenever the request changes, the loader will be triggered to fetch a new value for the resource.

If a params function isn't provided, the loader won't rerun unless the resource is reloaded.

### defaultValue

`NoInfer<T> | undefined`

The value which will be returned from the resource when a server value is unavailable, such as when the resource is still loading.

### equal

`ValueEqualityFn<T> | undefined`

Equality function used to compare the return value of the loader.

### injector

`Injector | undefined`

Overrides the `Injector` used by `resource`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/RxResourceOptions>
