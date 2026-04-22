# applyEach

applyEach



# applyEach

## API

```
function applyEach<TValue extends ReadonlyArray<any>>(
  path: SchemaPath<TValue>,
  schema: NoInfer<SchemaOrSchemaFn<TValue[number], Item>>,
): void;
function applyEach<TValue extends Object>(
  path: SchemaPath<TValue>,
  schema: NoInfer<SchemaOrSchemaFn<ItemType<TValue>, Child>>,
): void;
```

```
function applyEach<TValue>(path: SchemaPath<TValue>, schema: NoInfer<SchemaOrSchemaFn<TValue[number], Item>>): void;
```

Applies a schema to each item of an array.

@parampath`SchemaPath<TValue>`

The target path for an array field whose items the schema will be applied to.

@paramschema`NoInfer<SchemaOrSchemaFn<TValue[number], Item>>`

A schema for an element of the array, or function that binds logic to an element of the array.

@returns`void`

Usage notes

```
const nameSchema = schema<{first: string, last: string}>((name) => {
  required(name.first);
  required(name.last);
});
const namesForm = form(signal([{first: '', last: ''}]), (names) => {
  applyEach(names, nameSchema);
});
```

```
function applyEach<TValue>(path: SchemaPath<TValue>, schema: NoInfer<SchemaOrSchemaFn<ItemType<TValue>, Child>>): void;
```

@parampath`SchemaPath<TValue>`

@paramschema`NoInfer<SchemaOrSchemaFn<ItemType<TValue>, Child>>`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/applyEach>
