# TreeValidationResult

TreeValidationResult



# TreeValidationResult

The result of running a tree validation function.

## API

```
type TreeValidationResult<E extends ValidationError.WithOptionalField = ValidationError.WithOptionalField> = ValidationSuccess | OneOrMany<E>
```

## Description

The result of running a tree validation function.

The result may be one of the following:

1. A [`ValidationSuccess`](validationsuccess) to indicate no errors.
2. A [`ValidationError`](validationerror) without a field to indicate an error on the field being validated.
3. A [`ValidationError`](validationerror) with a field to indicate an error on the target field.
4. A list of [`ValidationError`](validationerror) with or without fields to indicate multiple errors.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/TreeValidationResult>
