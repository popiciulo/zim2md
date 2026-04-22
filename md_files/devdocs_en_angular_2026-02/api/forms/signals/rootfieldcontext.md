# RootFieldContext

RootFieldContext



# RootFieldContext

The base field context that is available for all fields.

## API

```
interface RootFieldContext<TValue> {
  readonly value: Signal<TValue>;
  readonly state: FieldState<TValue, string | number>;
  readonly field: FieldTree<TValue, string | number>;
  valueOf<PValue>(p: SchemaPath<PValue, SchemaPathRules, Root>): PValue;
  stateOf<PControl extends AbstractControl>(p: CompatSchemaPath<PControl, Root>): CompatFieldState<PControl, string | number>;
  stateOf<PValue>(p: SchemaPath<PValue, SchemaPathRules, Root>): FieldState<PValue, string | number>;
  fieldTreeOf<PModel>(p: SchemaPathTree<PModel, Root>): FieldTree<PModel, string | number>;
  readonly pathKeys: Signal<readonly string[]>;
}
```

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
<https://angular.dev/api/forms/signals/RootFieldContext>
