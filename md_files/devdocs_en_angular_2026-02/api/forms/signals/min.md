# min

min



# min

Binds a validator to the given path that requires the value to be greater than or equal to the given `minValue`. This function can only be called on number paths. In addition to binding a validator, this function adds [`MIN`](min) property to the field.

## API

```
function min<
  TValue extends number | string | null,
  TPathKind extends PathKind = PathKind.Root,
>(
  path: SchemaPath<TValue, 1, TPathKind>,
  minValue: number | LogicFn<TValue, number | undefined, TPathKind>,
  config?: BaseValidatorConfig<TValue, TPathKind> | undefined,
): void;
```

### min

`void`

Binds a validator to the given path that requires the value to be greater than or equal to the given `minValue`. This function can only be called on number paths. In addition to binding a validator, this function adds [`MIN`](min) property to the field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

Path of the field to validate

@paramminValue`number | LogicFn<TValue, number | undefined, TPathKind>`

The minimum value, or a LogicFn that returns the minimum value.

@paramconfig`BaseValidatorConfig<TValue, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.min(minValue)`](validationerror#min(minValue)) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/min>
