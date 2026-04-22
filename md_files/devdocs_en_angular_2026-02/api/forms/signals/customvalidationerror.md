# CustomValidationError

CustomValidationError



# CustomValidationError

A custom error that may contain additional properties

## API

```
class CustomValidationError implements ValidationError {
  constructor(options?: ValidationErrorOptions | undefined): CustomValidationError;
  readonly kind: string;
  readonly field: FieldTree<unknown>;
  readonly message?: string | undefined;
}
```

### constructor

`CustomValidationError`

@paramoptions`ValidationErrorOptions | undefined`

@returns`CustomValidationError`

### kind

`string`

Identifies the kind of error.

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/CustomValidationError>
