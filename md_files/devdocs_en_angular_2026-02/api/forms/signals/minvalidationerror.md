# MinValidationError

MinValidationError



# MinValidationError

An error used to indicate that a value is lower than the minimum allowed.

## API

```
class MinValidationError extends _NgValidationError {
  constructor(min: number, options?: ValidationErrorOptions | undefined): MinValidationError;
  readonly kind: "min";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`MinValidationError`

@parammin`number`

@paramoptions`ValidationErrorOptions | undefined`

@returns`MinValidationError`

### kind

`"min"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MinValidationError>
