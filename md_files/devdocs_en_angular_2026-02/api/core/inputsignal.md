# InputSignal

InputSignal



# InputSignal

[`InputSignal`](inputsignal) represents a special [`Signal`](signal) for a directive/component input.

[InputOptionsWithTransform](inputoptionswithtransform)

## API

```
interface InputSignal<T> extends InputSignalWithTransform<T, T> {
  override [SIGNAL]: InputSignalNode<T, TransformT>;
}
```

### [SIGNAL]

`InputSignalNode<T, TransformT>`

## Description

[`InputSignal`](inputsignal) represents a special [`Signal`](signal) for a directive/component input.

An input signal is similar to a non-writable signal except that it also carries additional type-information for transforms, and that Angular internally updates the signal whenever a new value is bound.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/InputSignal>
