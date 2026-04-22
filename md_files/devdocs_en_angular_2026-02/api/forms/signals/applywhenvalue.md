# applyWhenValue

applyWhenValue



# applyWhenValue

## API

```
function applyWhenValue<TValue, TNarrowed extends TValue>(
  path: SchemaPath<TValue>,
  predicate: (value: TValue) => value is TNarrowed,
  schema: SchemaOrSchemaFn<TNarrowed>,
): void;
function applyWhenValue<TValue>(
  path: SchemaPath<TValue>,
  predicate: (value: TValue) => boolean,
  schema: NoInfer<SchemaOrSchemaFn<TValue>>,
): void;
```

```
function applyWhenValue<TValue, TNarrowed>(path: SchemaPath<TValue>, predicate: (value: TValue) => value is TNarrowed, schema: SchemaOrSchemaFn<TNarrowed>): void;
```

Conditionally applies a predefined schema to a given `FieldPath`.

@parampath`SchemaPath<TValue>`

The target path to apply the schema to.

@parampredicate`(value: TValue) => value is TNarrowed`

A type guard that accepts a value `T` and returns `true` if `T` is of type `TNarrowed`.

@paramschema`SchemaOrSchemaFn<TNarrowed>`

The schema to apply to the field when `predicate` returns `true`.

@returns`void`

```
function applyWhenValue<TValue>(path: SchemaPath<TValue>, predicate: (value: TValue) => boolean, schema: NoInfer<SchemaOrSchemaFn<TValue>>): void;
```

Conditionally applies a predefined schema to a given `FieldPath`.

@parampath`SchemaPath<TValue>`

The target path to apply the schema to.

@parampredicate`(value: TValue) => boolean`

A function that accepts a value `T` and returns `true` when the schema should be applied.

@paramschema`NoInfer<SchemaOrSchemaFn<TValue>>`

The schema to apply to the field when `predicate` returns `true`.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/applyWhenValue>
