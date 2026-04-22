# maxError

maxError



# maxError

## API

```
function maxError(
  max: number,
  options: WithField<ValidationErrorOptions>,
): MaxValidationError;
function maxError(
  max: number,
  options?: ValidationErrorOptions | undefined,
): WithoutField<MaxValidationError>;
```

```
function maxError(max: number, options: WithField<ValidationErrorOptions>): MaxValidationError;
```

Create a max value error associated with the target field

@parammax`number`

The max value constraint

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`MaxValidationError`

```
function maxError(max: number, options?: ValidationErrorOptions | undefined): WithoutField<MaxValidationError>;
```

Create a max value error

@parammax`number`

The max value constraint

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<MaxValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/maxError>
