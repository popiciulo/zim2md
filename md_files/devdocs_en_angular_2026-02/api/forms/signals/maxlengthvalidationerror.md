# MaxLengthValidationError

MaxLengthValidationError



# MaxLengthValidationError

An error used to indicate that a value is longer than the maximum allowed length.

## API

```
class MaxLengthValidationError extends _NgValidationError {
  constructor(maxLength: number, options?: ValidationErrorOptions | undefined): MaxLengthValidationError;
  readonly kind: "maxLength";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`MaxLengthValidationError`

@parammaxLength`number`

@paramoptions`ValidationErrorOptions | undefined`

@returns`MaxLengthValidationError`

### kind

`"maxLength"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MaxLengthValidationError>
