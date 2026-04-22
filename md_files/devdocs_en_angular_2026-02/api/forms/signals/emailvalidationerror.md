# EmailValidationError

EmailValidationError



# EmailValidationError

An error used to indicate that a value is not a valid email.

## API

```
class EmailValidationError extends _NgValidationError {
  readonly kind: "email";
  readonly override field: FieldTree<unknown>;
  readonly override message?: string | undefined;
}
```

### kind

`"email"`

### field

`FieldTree<unknown>`

The field associated with this error.

### message

`string | undefined`

Human readable error message.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/EmailValidationError>
