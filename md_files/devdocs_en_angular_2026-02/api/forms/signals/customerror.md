# customError

customError



# customError

## API

```
function customError<E extends Partial<ValidationError.WithField>>(
  obj: WithField<E>,
): CustomValidationError;
function customError<E extends Partial<ValidationError.WithField>>(
  obj?: E | undefined,
): WithoutField<CustomValidationError>;
```

```
function customError<E>(obj: WithField<E>): CustomValidationError;
```

Create a custom error associated with the target field

@paramobj`WithField<E>`

The object to create an error from

@returns`CustomValidationError`

```
function customError<E>(obj?: E | undefined): WithoutField<CustomValidationError>;
```

Create a custom error

@paramobj`E | undefined`

The object to create an error from

@returns`WithoutField<CustomValidationError>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/customError>
