# CompatValidationError

CompatValidationError



# CompatValidationError

An error used for compat errors.

## API

```
class CompatValidationError<T = unknown> implements ValidationError {
  constructor({context, kind, control}: { context: T; kind: string; control: AbstractControl; }): CompatValidationError<T>;
  readonly kind: string;
  readonly control: AbstractControl;
  readonly field: FieldTree<unknown>;
  readonly context: T;
  readonly message?: string | undefined;
}
```

### constructor

`CompatValidationError<T>`

@param{context, kind, control}`{ context: T; kind: string; control: AbstractControl; }`

@returns`CompatValidationError<T>`

### kind

`string`

### control

`AbstractControl`

### field

`FieldTree<unknown>`

### context

`T`

### message

`string | undefined`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/compat/CompatValidationError>
