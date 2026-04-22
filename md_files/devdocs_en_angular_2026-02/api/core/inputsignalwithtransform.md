# InputSignalWithTransform

InputSignalWithTransform



# InputSignalWithTransform

[`InputSignalWithTransform`](inputsignalwithtransform) represents a special [`Signal`](signal) for a directive/component input with a `transform` function.

[InputSignal](inputsignal)

## API

```
interface InputSignalWithTransform<T, TransformT> extends Signal<T> {
  [SIGNAL]: InputSignalNode<T, TransformT>;
}
```

### [SIGNAL]

`InputSignalNode<T, TransformT>`

## Description

[`InputSignalWithTransform`](inputsignalwithtransform) represents a special [`Signal`](signal) for a directive/component input with a `transform` function.

Signal inputs with transforms capture an extra generic for their transform write type. Transforms can expand the accepted bound values for an input while ensuring value retrievals of the signal input are still matching the generic input type.

```
class MyDir {
  disabled = input(false, {
    transform: (v: string|boolean) => convertToBoolean(v),
  }); // InputSignalWithTransform<boolean, string|boolean>

  click() {
    this.disabled() // always returns a `boolean`.
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/InputSignalWithTransform>
