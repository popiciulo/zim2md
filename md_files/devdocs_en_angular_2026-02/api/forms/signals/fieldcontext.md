# FieldContext

FieldContext



# FieldContext

Provides access to the state of the current field as well as functions that can be used to look up state of other fields based on a `FieldPath`.

## API

```
type FieldContext<TValue, TPathKind extends PathKind = PathKind.Root> = TPathKind extends PathKind.Item
  ? ItemFieldContext<TValue>
  : TPathKind extends PathKind.Child
    ? ChildFieldContext<TValue>
    : RootFieldContext<TValue>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FieldContext>
