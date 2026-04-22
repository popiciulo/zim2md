# email

email



# email

Binds a validator to the given path that requires the value to match the standard email format. This function can only be called on string paths.

## API

```
function email<TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<string, 1, TPathKind>,
  config?: BaseValidatorConfig<string, TPathKind> | undefined,
): void;
```

### email

`void`

Binds a validator to the given path that requires the value to match the standard email format. This function can only be called on string paths.

@parampath`SchemaPath<string, 1, TPathKind>`

Path of the field to validate

@paramconfig`BaseValidatorConfig<string, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.email()`](validationerror#email) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/email>
