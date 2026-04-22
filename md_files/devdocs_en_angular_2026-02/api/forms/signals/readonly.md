# readonly

readonly



# readonly

Adds logic to a field to conditionally make it readonly. A readonly field does not contribute to the validation, touched/dirty, or other state of its parent field.

## API

```
function readonly<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  logic?: NoInfer<LogicFn<TValue, boolean, TPathKind>>,
): void;
```

### readonly

`void`

Adds logic to a field to conditionally make it readonly. A readonly field does not contribute to the validation, touched/dirty, or other state of its parent field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to make readonly.

@paramlogic`NoInfer<LogicFn<TValue, boolean, TPathKind>>`

A reactive function that returns `true` when the field is readonly.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/readonly>
