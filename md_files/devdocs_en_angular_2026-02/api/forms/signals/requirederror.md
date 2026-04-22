# requiredError

requiredError



# requiredError

## API

```
function requiredError(
  options: WithField<ValidationErrorOptions>,
): RequiredValidationError;
function requiredError(
  options?: ValidationErrorOptions | undefined,
): WithoutField<RequiredValidationError>;
```

```
function requiredError(options: WithField<ValidationErrorOptions>): RequiredValidationError;
```

Create a required error associated with the target field

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`RequiredValidationError`

```
function requiredError(options?: ValidationErrorOptions | undefined): WithoutField<RequiredValidationError>;
```

Create a required error

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<RequiredValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/requiredError>
