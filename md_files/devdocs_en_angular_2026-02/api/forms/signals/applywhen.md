# applyWhen

applyWhen



# applyWhen

Conditionally applies a predefined schema to a given `FieldPath`.

## API

```
function applyWhen<TValue>(
  path: SchemaPath<TValue>,
  logic: LogicFn<TValue, boolean>,
  schema: NoInfer<SchemaOrSchemaFn<TValue>>,
): void;
```

### applyWhen

`void`

Conditionally applies a predefined schema to a given `FieldPath`.

@parampath`SchemaPath<TValue>`

The target path to apply the schema to.

@paramlogic`LogicFn<TValue, boolean>`

A `LogicFn<T, boolean>` that returns `true` when the schema should be applied.

@paramschema`NoInfer<SchemaOrSchemaFn<TValue>>`

The schema to apply to the field when the `logic` function returns `true`.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/applyWhen>
