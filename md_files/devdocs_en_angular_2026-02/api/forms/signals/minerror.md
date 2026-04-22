# minError

minError



# minError

## API

```
function minError(
  min: number,
  options: WithField<ValidationErrorOptions>,
): MinValidationError;
function minError(
  min: number,
  options?: ValidationErrorOptions | undefined,
): WithoutField<MinValidationError>;
```

```
function minError(min: number, options: WithField<ValidationErrorOptions>): MinValidationError;
```

Create a min value error associated with the target field

@parammin`number`

The min value constraint

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`MinValidationError`

```
function minError(min: number, options?: ValidationErrorOptions | undefined): WithoutField<MinValidationError>;
```

Create a min value error

@parammin`number`

The min value constraint

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<MinValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/minError>
