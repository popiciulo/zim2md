# ResourceRef

ResourceRef



# ResourceRef

A [`WritableResource`](writableresource) created through the [`resource`](resource) function.

## API

```
interface ResourceRef<T> extends WritableResource<T> {
  hasValue(this: T extends undefined ? this : never): this is ResourceRef<Exclude<T, undefined>>;
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

### hasValue

`this is ResourceRef<Exclude<T, undefined>>`

@paramthis`T extends undefined ? this : never`

@returns`this is ResourceRef<Exclude<T, undefined>>`

### hasValue

`boolean`

@returns`boolean`

### destroy

`void`

Manually destroy the resource, which cancels pending requests and returns it to `idle` state.

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

The current status of the [`Resource`](resource), which describes what the resource is currently doing and what can be expected of its `value`.

### error

`Signal<Error | undefined>`

When in the `error` state, this returns the last known error from the [`Resource`](resource).

### isLoading

`Signal<boolean>`

Whether this resource is loading a new value (or reloading the existing one).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ResourceRef>
