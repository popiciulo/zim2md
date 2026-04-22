# StandardSchemaValidationError

StandardSchemaValidationError



# StandardSchemaValidationError

An error used to indicate an issue validating against a standard schema.

## API

```
class StandardSchemaValidationError extends _NgValidationError {
  constructor(issue: StandardSchemaV1.Issue, options?: ValidationErrorOptions | undefined): StandardSchemaValidationError;
  readonly kind: "standardSchema";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### constructor

`StandardSchemaValidationError`

@paramissue`StandardSchemaV1.Issue`

@paramoptions`ValidationErrorOptions | undefined`

@returns`StandardSchemaValidationError`

### kind

`"standardSchema"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/StandardSchemaValidationError>
