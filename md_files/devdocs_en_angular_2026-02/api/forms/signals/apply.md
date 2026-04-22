# apply

apply



# apply

Applies a predefined schema to a given `FieldPath`.

## API

```
function apply<TValue>(
  path: SchemaPath<TValue>,
  schema: NoInfer<SchemaOrSchemaFn<TValue>>,
): void;
```

### apply

`void`

Applies a predefined schema to a given `FieldPath`.

@parampath`SchemaPath<TValue>`

The target path to apply the schema to.

@paramschema`NoInfer<SchemaOrSchemaFn<TValue>>`

The schema to apply to the property

@returns`void`

Usage notes

```
const nameSchema = schema<{first: string, last: string}>((name) => {
  required(name.first);
  required(name.last);
});
const profileForm = form(signal({name: {first: '', last: ''}, age: 0}), (profile) => {
  apply(profile.name, nameSchema);
});
```

## Usage Notes

```
const nameSchema = schema<{first: string, last: string}>((name) => {
  required(name.first);
  required(name.last);
});
const profileForm = form(signal({name: {first: '', last: ''}, age: 0}), (profile) => {
  apply(profile.name, nameSchema);
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/apply>
