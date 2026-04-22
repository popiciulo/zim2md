# HttpResourceRef

HttpResourceRef



# HttpResourceRef

A [`WritableResource`](../../core/writableresource) that represents the results of a reactive HTTP request.

## API

```
interface HttpResourceRef<T> extends WritableResource<T>, ResourceRef<T> {
  readonly headers: Signal<HttpHeaders | undefined>;
  readonly statusCode: Signal<number | undefined>;
  readonly progress: Signal<HttpProgressEvent | undefined>;
  hasValue(this: T extends undefined ? this : never): this is HttpResourceRef<Exclude<T, undefined>>;
  hasValue(): boolean;
  destroy(): void;
  readonly override value: WritableSignal<T>;
  override set(value: T): void;
  override update(updater: (value: T) => T): void;
  override asReadonly(): Resource<T>;
  override reload(): boolean;
  readonly override status: Signal<ResourceStatus>;
  readonly override error: Signal<Error | undefined>;
  readonly override isLoading: Signal<boolean>;
}
```

### headers

`Signal<HttpHeaders | undefined>`

Signal of the response headers, when available.

### statusCode

`Signal<number | undefined>`

Signal of the response status code, when available.

### progress

`Signal<HttpProgressEvent | undefined>`

Signal of the latest progress update, if the request was made with `reportProgress: true`.

### hasValue

`this is HttpResourceRef<Exclude<T, undefined>>`

@paramthis`T extends undefined ? this : never`

@returns`this is HttpResourceRef<Exclude<T, undefined>>`

### hasValue

`boolean`

@returns`boolean`

### destroy

`void`

@returns`void`

### value

`WritableSignal<T>`

### set

`void`

Convenience wrapper for `value.set`.

@paramvalue`T`

@returns`void`

### update

`void`

Convenience wrapper for `value.update`.

@paramupdater`(value: T) => T`

@returns`void`

### asReadonly

`Resource<T>`

@returns`Resource<T>`

### reload

`boolean`

Instructs the resource to re-load any asynchronous dependency it may have.

Note that the resource will not enter its reloading state until the actual backend request is made.

@returns`boolean`

### status

`Signal<ResourceStatus>`

The current status of the `Resource`, which describes what the resource is currently doing and what can be expected of its `value`.

### error

`Signal<Error | undefined>`

When in the `error` state, this returns the last known error from the `Resource`.

### isLoading

`Signal<boolean>`

Whether this resource is loading a new value (or reloading the existing one).

## Description

A [`WritableResource`](../../core/writableresource) that represents the results of a reactive HTTP request.

`HttpResource`s are backed by [`HttpClient`](httpclient), including support for interceptors, testing, and the other features of the [`HttpClient`](httpclient) API.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResourceRef>
