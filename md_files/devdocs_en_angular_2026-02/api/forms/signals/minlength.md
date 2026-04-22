# minLength

minLength



# minLength

Binds a validator to the given path that requires the length of the value to be greater than or equal to the given [`minLength`](minlength). This function can only be called on string or array paths. In addition to binding a validator, this function adds [`MIN_LENGTH`](min_length) property to the field.

## API

```
function minLength<
  TValue extends ValueWithLengthOrSize,
  TPathKind extends PathKind = PathKind.Root,
>(
  path: SchemaPath<TValue, 1, TPathKind>,
  minLength: number | LogicFn<TValue, number | undefined, TPathKind>,
  config?: BaseValidatorConfig<TValue, TPathKind> | undefined,
): void;
```

### minLength

`void`

Binds a validator to the given path that requires the length of the value to be greater than or equal to the given [`minLength`](minlength). This function can only be called on string or array paths. In addition to binding a validator, this function adds [`MIN_LENGTH`](min_length) property to the field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

Path of the field to validate

@paramminLength`number | LogicFn<TValue, number | undefined, TPathKind>`

The minimum length, or a LogicFn that returns the minimum length.

@paramconfig`BaseValidatorConfig<TValue, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.minLength(minLength)`](validationerror#minLength(minLength)) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/minLength>
