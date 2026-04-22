# MaxValidationError

MaxValidationError



# MaxValidationError

An error used to indicate that a value is higher than the maximum allowed.

## API

```
class MaxValidationError extends _NgValidationError {
  constructor(max: number, options?: ValidationErrorOptions | undefined): MaxValidationError;
  readonly kind: "max";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`MaxValidationError`

@parammax`number`

@paramoptions`ValidationErrorOptions | undefined`

@returns`MaxValidationError`

### kind

`"max"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MaxValidationError>
