# ValidationResult

ValidationResult



# ValidationResult

A validation result where all errors explicitly define their target field.

## API

```
type ValidationResult<E extends ValidationError = ValidationError> = | ValidationSuccess
  | OneOrMany<E>
```

## Description

A validation result where all errors explicitly define their target field.

The result may be one of the following:

1. A [`ValidationSuccess`](validationsuccess) to indicate no errors.
2. A [`ValidationError`](validationerror) with a field to indicate an error on the target field.
3. A list of [`ValidationError`](validationerror) with fields to indicate multiple errors.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/ValidationResult>
