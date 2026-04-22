# ModelSignal

ModelSignal



# ModelSignal

[`ModelSignal`](modelsignal) represents a special [`Signal`](signal) for a directive/component model field.

## API

```
interface ModelSignal<T> extends WritableSignal<T>, InputSignal<T>, OutputRef<T> {
  [SIGNAL]: InputSignalNode<T, T>;
  override set(value: T): void;
  override update(updateFn: (value: T) => T): void;
  override asReadonly(): Signal<T>;
  override subscribe(callback: (value: T) => void): OutputRefSubscription;
}
```

### [SIGNAL]

`InputSignalNode<T, T>`

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

### subscribe

`OutputRefSubscription`

Registers a callback that is invoked whenever the output emits a new value of type `T`.

Angular will automatically clean up the subscription when the directive/component of the output is destroyed.

@paramcallback`(value: T) => void`

@returns`OutputRefSubscription`

## Description

[`ModelSignal`](modelsignal) represents a special [`Signal`](signal) for a directive/component model field.

A model signal is a writeable signal that can be exposed as an output. Whenever its value is updated, it emits to the output.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ModelSignal>
