# MaybeSchemaPathTree

MaybeSchemaPathTree



# MaybeSchemaPathTree

Helper type for defining `FieldPath`. Given a type `TValue` that may include `undefined`, it extracts the `undefined` outside the `FieldPath` type.

## API

```
type MaybeSchemaPathTree<TModel, TPathKind extends PathKind = PathKind.Root> = | (TModel & undefined)
  | SchemaPathTree<Exclude<TModel, undefined>, TPathKind>
```

## Description

Helper type for defining `FieldPath`. Given a type `TValue` that may include `undefined`, it extracts the `undefined` outside the `FieldPath` type.

For example `MaybeFieldPath<{a: number} | undefined, PathKind.Child>` would be equivalent to `undefined | FieldTree<{a: number}, PathKind.child>`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MaybeSchemaPathTree>
