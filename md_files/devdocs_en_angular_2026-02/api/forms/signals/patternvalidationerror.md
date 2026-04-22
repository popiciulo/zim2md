# PatternValidationError

PatternValidationError



# PatternValidationError

An error used to indicate that a value does not match the required pattern.

## API

```
class PatternValidationError extends _NgValidationError {
  constructor(pattern: RegExp, options?: ValidationErrorOptions | undefined): PatternValidationError;
  readonly kind: "pattern";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`PatternValidationError`

@parampattern`RegExp`

@paramoptions`ValidationErrorOptions | undefined`

@returns`PatternValidationError`

### kind

`"pattern"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/PatternValidationError>
