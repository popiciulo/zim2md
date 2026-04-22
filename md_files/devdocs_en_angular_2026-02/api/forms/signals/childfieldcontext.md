# ChildFieldContext

ChildFieldContext



# ChildFieldContext

Field context that is available for all fields that are a child of another field.

## API

```
interface ChildFieldContext<TValue> extends RootFieldContext<TValue> {
  readonly key: Signal<string>;
  readonly override value: Signal<TValue>;
  readonly override state: FieldState<TValue, string | number>;
  readonly override field: FieldTree<TValue, string | number>;
  override valueOf<PValue>(p: SchemaPath<PValue, SchemaPathRules, Root>): PValue;
  override stateOf<PControl extends AbstractControl>(p: CompatSchemaPath<PControl, Root>): CompatFieldState<PControl, string | number>;
  override stateOf<PValue>(p: SchemaPath<PValue, SchemaPathRules, Root>): FieldState<PValue, string | number>;
  override fieldTreeOf<PModel>(p: SchemaPathTree<PModel, Root>): FieldTree<PModel, string | number>;
  readonly override pathKeys: Signal<readonly string[]>;
}
```

### key

`Signal<string>`

The key of the current field in its parent field.

### value

`Signal<TValue>`

A signal containing the value of the current field.

### state

`FieldState<TValue, string | number>`

The state of the current field.

### field

`FieldTree<TValue, string | number>`

The current field.

### valueOf

`PValue`

Gets the value of the field represented by the given path.

@paramp`SchemaPath<PValue, SchemaPathRules, Root>`

@returns`PValue`

### stateOf

`CompatFieldState<PControl, string | number>`

Gets the state of the field represented by the given path.

@paramp`CompatSchemaPath<PControl, Root>`

@returns`CompatFieldState<PControl, string | number>`

### stateOf

`FieldState<PValue, string | number>`

@paramp`SchemaPath<PValue, SchemaPathRules, Root>`

@returns`FieldState<PValue, string | number>`

### fieldTreeOf

`FieldTree<PModel, string | number>`

Gets the field represented by the given path.

@paramp`SchemaPathTree<PModel, Root>`

@returns`FieldTree<PModel, string | number>`

### pathKeys

`Signal<readonly string[]>`

The list of keys that lead from the root field to the current field.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/ChildFieldContext>
