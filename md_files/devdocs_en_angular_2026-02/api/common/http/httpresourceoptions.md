# HttpResourceOptions

HttpResourceOptions



# HttpResourceOptions

Options for creating an [`httpResource`](httpresource).

## API

```
interface HttpResourceOptions<TResult, TRaw> {
  parse?: ((value: TRaw) => TResult) | undefined;
  defaultValue?: NoInfer<TResult> | undefined;
  injector?: Injector | undefined;
  equal?: ValueEqualityFn<NoInfer<TResult>> | undefined;
  debugName?: string | undefined;
}
```

### parse

`((value: TRaw) => TResult) | undefined`

Transform the result of the HTTP request before it's delivered to the resource.

`parse` receives the value from the HTTP layer as its raw type (e.g. as `unknown` for JSON data). It can be used to validate or transform the type of the resource, and return a more specific type. This is also useful for validating backend responses using a runtime schema validation library such as Zod.

### defaultValue

`NoInfer<TResult> | undefined`

Value that the resource will take when in Idle or Loading states.

If not set, the resource will use `undefined` as its default value.

### injector

`Injector | undefined`

The [`Injector`](../../core/injector) in which to create the [`httpResource`](httpresource).

If this is not provided, the current [injection context](../../../guide/di/dependency-injection-context) will be used instead (via [`inject`](../../core/inject)).

### equal

`ValueEqualityFn<NoInfer<TResult>> | undefined`

A comparison function which defines equality for the response value.

### debugName

`string | undefined`

A debug name for the reactive node. Used in Angular DevTools to identify the node.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResourceOptions>
