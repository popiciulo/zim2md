# StreamingResourceOptions

StreamingResourceOptions



# StreamingResourceOptions

Options to the [`resource`](resource) function, for creating a resource.

## API

```
interface StreamingResourceOptions<T, R> extends BaseResourceOptions<T, R> {
  stream: ResourceStreamingLoader<T, R>;
  loader?: undefined;
  override params?: (() => R) | undefined;
  override defaultValue?: NoInfer<T> | undefined;
  override equal?: ValueEqualityFn<T> | undefined;
  override injector?: Injector | undefined;
}
```

### stream

`ResourceStreamingLoader<T, R>`

Loading function which returns a `Promise` of a signal of the resource's value for a given request, which can change over time as new values are received from a stream.

### loader

`undefined`

Cannot specify `stream` and `loader` at the same time.

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

Overrides the [`Injector`](injector) used by [`resource`](resource).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/StreamingResourceOptions>
