# MaybeFieldTree

MaybeFieldTree



# MaybeFieldTree

Helper type for defining [`FieldTree`](fieldtree). Given a type `TValue` that may include `undefined`, it extracts the `undefined` outside the [`FieldTree`](fieldtree) type.

## API

```
type MaybeFieldTree<TModel, TKey extends string | number = string | number> = | (TModel & undefined)
  | FieldTree<Exclude<TModel, undefined>, TKey>
```

## Description

Helper type for defining [`FieldTree`](fieldtree). Given a type `TValue` that may include `undefined`, it extracts the `undefined` outside the [`FieldTree`](fieldtree) type.

For example `MaybeField<{a: number} | undefined, TKey>` would be equivalent to `undefined | FieldTree<{a: number}, TKey>`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MaybeFieldTree>
