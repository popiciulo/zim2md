# AsyncValidationResult

AsyncValidationResult



# AsyncValidationResult

An asynchronous validation result where all errors explicitly define their target field.

## API

```
type AsyncValidationResult<E extends ValidationError = ValidationError> = | ValidationResult<E>
  | 'pending'
```

## Description

An asynchronous validation result where all errors explicitly define their target field.

The result may be one of the following:

1. A [`ValidationResult`](validationresult) to indicate the result if resolved.
2. 'pending' if the validation is not yet resolved.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/AsyncValidationResult>
