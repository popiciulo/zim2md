# minLengthError

minLengthError



# minLengthError

## API

```
function minLengthError(
  minLength: number,
  options: WithField<ValidationErrorOptions>,
): MinLengthValidationError;
function minLengthError(
  minLength: number,
  options?: ValidationErrorOptions | undefined,
): WithoutField<MinLengthValidationError>;
```

```
function minLengthError(minLength: number, options: WithField<ValidationErrorOptions>): MinLengthValidationError;
```

Create a minLength error associated with the target field

@paramminLength`number`

The minLength constraint

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`MinLengthValidationError`

```
function minLengthError(minLength: number, options?: ValidationErrorOptions | undefined): WithoutField<MinLengthValidationError>;
```

Create a minLength error

@paramminLength`number`

The minLength constraint

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<MinLengthValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/minLengthError>
