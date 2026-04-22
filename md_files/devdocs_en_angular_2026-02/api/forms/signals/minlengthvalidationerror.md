# MinLengthValidationError

MinLengthValidationError



# MinLengthValidationError

An error used to indicate that a value is shorter than the minimum allowed length.

## API

```
class MinLengthValidationError extends _NgValidationError {
  constructor(minLength: number, options?: ValidationErrorOptions | undefined): MinLengthValidationError;
  readonly kind: "minLength";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`MinLengthValidationError`

@paramminLength`number`

@paramoptions`ValidationErrorOptions | undefined`

@returns`MinLengthValidationError`

### kind

`"minLength"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MinLengthValidationError>
