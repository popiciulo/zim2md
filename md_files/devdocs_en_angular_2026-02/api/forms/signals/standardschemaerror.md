# standardSchemaError

standardSchemaError



# standardSchemaError

## API

```
function standardSchemaError(
  issue: StandardSchemaV1.Issue,
  options: WithField<ValidationErrorOptions>,
): StandardSchemaValidationError;
function standardSchemaError(
  issue: StandardSchemaV1.Issue,
  options?: ValidationErrorOptions | undefined,
): WithoutField<StandardSchemaValidationError>;
```

```
function standardSchemaError(issue: StandardSchemaV1.Issue, options: WithField<ValidationErrorOptions>): StandardSchemaValidationError;
```

Create a standard schema issue error associated with the target field

@paramissue`StandardSchemaV1.Issue`

The standard schema issue

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`StandardSchemaValidationError`

```
function standardSchemaError(issue: StandardSchemaV1.Issue, options?: ValidationErrorOptions | undefined): WithoutField<StandardSchemaValidationError>;
```

Create a standard schema issue error

@paramissue`StandardSchemaV1.Issue`

The standard schema issue

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<StandardSchemaValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/standardSchemaError>
