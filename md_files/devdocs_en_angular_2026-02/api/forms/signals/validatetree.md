# validateTree

validateTree



# validateTree

Adds logic to a field to determine if the field or any of its child fields has validation errors.

## API

```
function validateTree<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  logic: NoInfer<TreeValidator<TValue, TPathKind>>,
): void;
```

### validateTree

`void`

Adds logic to a field to determine if the field or any of its child fields has validation errors.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to add the validation logic to.

@paramlogic`NoInfer<TreeValidator<TValue, TPathKind>>`

A [`TreeValidator`](treevalidator) that returns the current validation errors. Errors returned by the validator may specify a target field to indicate an error on a child field.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/validateTree>
