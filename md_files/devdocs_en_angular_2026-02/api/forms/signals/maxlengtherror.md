# maxLengthError

maxLengthError



# maxLengthError

## API

```
function maxLengthError(
  maxLength: number,
  options: WithField<ValidationErrorOptions>,
): MaxLengthValidationError;
function maxLengthError(
  maxLength: number,
  options?: ValidationErrorOptions | undefined,
): WithoutField<MaxLengthValidationError>;
```

```
function maxLengthError(maxLength: number, options: WithField<ValidationErrorOptions>): MaxLengthValidationError;
```

Create a maxLength error associated with the target field

@parammaxLength`number`

The maxLength constraint

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`MaxLengthValidationError`

```
function maxLengthError(maxLength: number, options?: ValidationErrorOptions | undefined): WithoutField<MaxLengthValidationError>;
```

Create a maxLength error

@parammaxLength`number`

The maxLength constraint

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<MaxLengthValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/maxLengthError>
