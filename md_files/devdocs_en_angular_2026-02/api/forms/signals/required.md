# required

required



# required

Binds a validator to the given path that requires the value to be non-empty. This function can only be called on any type of path. In addition to binding a validator, this function adds [`REQUIRED`](required) property to the field.

## API

```
function required<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  config?:
    | (BaseValidatorConfig<TValue, TPathKind> & {
        when?: NoInfer<LogicFn<TValue, boolean, TPathKind>> | undefined;
      })
    | undefined,
): void;
```

### required

`void`

Binds a validator to the given path that requires the value to be non-empty. This function can only be called on any type of path. In addition to binding a validator, this function adds [`REQUIRED`](required) property to the field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

Path of the field to validate

@paramconfig`(BaseValidatorConfig<TValue, TPathKind> & { when?: NoInfer<LogicFn<TValue, boolean, TPathKind>> | undefined; }) | undefined`

Optional, allows providing any of the following options:

- `message`: A user-facing message for the error.
- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.required()`](validationerror#required) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).
- `when`: A function that receives the [`FieldContext`](fieldcontext) and returns true if the field is required

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/required>
