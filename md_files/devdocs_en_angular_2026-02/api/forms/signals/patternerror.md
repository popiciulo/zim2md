# patternError

patternError



# patternError

## API

```
function patternError(
  pattern: RegExp,
  options: WithField<ValidationErrorOptions>,
): PatternValidationError;
function patternError(
  pattern: RegExp,
  options?: ValidationErrorOptions | undefined,
): WithoutField<PatternValidationError>;
```

```
function patternError(pattern: RegExp, options: WithField<ValidationErrorOptions>): PatternValidationError;
```

Create a pattern matching error associated with the target field

@parampattern`RegExp`

The violated pattern

@paramoptions`WithField<ValidationErrorOptions>`

The validation error options

@returns`PatternValidationError`

```
function patternError(pattern: RegExp, options?: ValidationErrorOptions | undefined): WithoutField<PatternValidationError>;
```

Create a pattern matching error

@parampattern`RegExp`

The violated pattern

@paramoptions`ValidationErrorOptions | undefined`

The optional validation error options

@returns`WithoutField<PatternValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/patternError>
