# maxLength

maxLength



# maxLength

Binds a validator to the given path that requires the length of the value to be less than or equal to the given [`maxLength`](maxlength). This function can only be called on string or array paths. In addition to binding a validator, this function adds [`MAX_LENGTH`](max_length) property to the field.

## API

```
function maxLength<
  TValue extends ValueWithLengthOrSize,
  TPathKind extends PathKind = PathKind.Root,
>(
  path: SchemaPath<TValue, 1, TPathKind>,
  maxLength: number | LogicFn<TValue, number | undefined, TPathKind>,
  config?: BaseValidatorConfig<TValue, TPathKind> | undefined,
): void;
```

### maxLength

`void`

Binds a validator to the given path that requires the length of the value to be less than or equal to the given [`maxLength`](maxlength). This function can only be called on string or array paths. In addition to binding a validator, this function adds [`MAX_LENGTH`](max_length) property to the field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

Path of the field to validate

@parammaxLength`number | LogicFn<TValue, number | undefined, TPathKind>`

The maximum length, or a LogicFn that returns the maximum length.

@paramconfig`BaseValidatorConfig<TValue, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.maxLength(maxLength)`](validationerror#maxLength(maxLength)) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/maxLength>
