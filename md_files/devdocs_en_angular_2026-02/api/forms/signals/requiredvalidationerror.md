# RequiredValidationError

RequiredValidationError



# RequiredValidationError

An error used to indicate that a required field is empty.

## API

```
class RequiredValidationError extends _NgValidationError {
  readonly kind: "required";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### kind

`"required"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/RequiredValidationError>
