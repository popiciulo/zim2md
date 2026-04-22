# hidden

hidden



# hidden

Adds logic to a field to conditionally hide it. A hidden field does not contribute to the validation, touched/dirty, or other state of its parent field.

## API

```
function hidden<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  logic: NoInfer<LogicFn<TValue, boolean, TPathKind>>,
): void;
```

### hidden

`void`

Adds logic to a field to conditionally hide it. A hidden field does not contribute to the validation, touched/dirty, or other state of its parent field.

If a field may be hidden it is recommended to guard it with an `@if` in the template:

```
@if (!email().hidden()) {
  <label for="email">Email</label>
  <input id="email" type="email" [control]="email" />
}
```

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to add the hidden logic to.

@paramlogic`NoInfer<LogicFn<TValue, boolean, TPathKind>>`

A reactive function that returns `true` when the field is hidden.

@returns`void`

## Description

Adds logic to a field to conditionally hide it. A hidden field does not contribute to the validation, touched/dirty, or other state of its parent field.

If a field may be hidden it is recommended to guard it with an `@if` in the template:

```
@if (!email().hidden()) {
  <label for="email">Email</label>
  <input id="email" type="email" [control]="email" />
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/hidden>
