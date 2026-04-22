# WritableSignal

WritableSignal



# WritableSignal

A [`Signal`](signal) with a value that can be mutated via a setter interface.

## API

```
interface WritableSignal<T> extends Signal<T> {
  set(value: T): void;
  update(updateFn: (value: T) => T): void;
  asReadonly(): Signal<T>;
  override [SIGNAL]: unknown;
}
```

### set

`void`

Directly set the signal to a new value, and notify any dependents.

@paramvalue`T`

@returns`void`

### update

`void`

Update the value of the signal based on its current value, and notify any dependents.

@paramupdateFn`(value: T) => T`

@returns`void`

### asReadonly

`Signal<T>`

Returns a readonly version of this signal. Readonly signals can be accessed to read their value but can't be changed using set or update methods. The readonly signals do *not* have any built-in mechanism that would prevent deep-mutation of their value.

@returns`Signal<T>`

### [SIGNAL]

`unknown`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/WritableSignal>
