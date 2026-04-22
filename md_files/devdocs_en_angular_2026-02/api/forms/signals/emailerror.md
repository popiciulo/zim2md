# emailError

emailError



# emailError

## API

```
function emailError(
  options: WithField<ValidationErrorOptions>,
): EmailValidationError;
function emailError(
  options?: ValidationErrorOptions | undefined,
): WithoutField<EmailValidationError>;
```

```
function emailError(options: WithField<ValidationErrorOptions>): EmailValidationError;
```

Create an email format error associated with the target field

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`EmailValidationError`

```
function emailError(options?: ValidationErrorOptions | undefined): WithoutField<EmailValidationError>;
```

Create an email format error

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<EmailValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/emailError>
