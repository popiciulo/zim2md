# validate

validate



# validate

Adds logic to a field to determine if the field has validation errors.

## API

```
function validate<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  logic: NoInfer<FieldValidator<TValue, TPathKind>>,
): void;
```

### validate

`void`

Adds logic to a field to determine if the field has validation errors.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to add the validation logic to.

@paramlogic`NoInfer<FieldValidator<TValue, TPathKind>>`

A [`Validator`](validator) that returns the current validation errors.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/validate>
