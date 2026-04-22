# max

max



# max

Binds a validator to the given path that requires the value to be less than or equal to the given `maxValue`. This function can only be called on number paths. In addition to binding a validator, this function adds [`MAX`](max) property to the field.

## API

```
function max<TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<string | number | null, 1, TPathKind>,
  maxValue:
    | number
    | LogicFn<string | number | null, number | undefined, TPathKind>,
  config?: BaseValidatorConfig<string | number | null, TPathKind> | undefined,
): void;
```

### max

`void`

Binds a validator to the given path that requires the value to be less than or equal to the given `maxValue`. This function can only be called on number paths. In addition to binding a validator, this function adds [`MAX`](max) property to the field.

@parampath`SchemaPath<string | number | null, 1, TPathKind>`

Path of the field to validate

@parammaxValue`number | LogicFn<string | number | null, number | undefined, TPathKind>`

The maximum value, or a LogicFn that returns the maximum value.

@paramconfig`BaseValidatorConfig<string | number | null, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.max(maxValue)`](validationerror#max(maxValue)) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/max>
