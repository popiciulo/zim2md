# OutputEmitterRef

OutputEmitterRef



# OutputEmitterRef

An [`OutputEmitterRef`](outputemitterref) is created by the [`output()`](output) function and can be used to emit values to consumers of your directive or component.

[Custom events with outputs](../../guide/components/outputs)

## API

```
class OutputEmitterRef<T> implements OutputRef<T> {
  subscribe(callback: (value: T) => void): OutputRefSubscription;
  emit(value: T): void;
}
```

### subscribe

`OutputRefSubscription`

@paramcallback`(value: T) => void`

@returns`OutputRefSubscription`

### emit

`void`

Emits a new value to the output.

@paramvalue`T`

@returns`void`

## Description

An [`OutputEmitterRef`](outputemitterref) is created by the [`output()`](output) function and can be used to emit values to consumers of your directive or component.

Consumers of your directive/component can bind to the output and subscribe to changes via the bound event syntax. For example:

```
<my-comp (valueChange)="processNewValue($event)" />
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OutputEmitterRef>
