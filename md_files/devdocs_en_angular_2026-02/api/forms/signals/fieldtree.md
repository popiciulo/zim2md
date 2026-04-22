# FieldTree

FieldTree



# FieldTree

An object that represents a tree of fields in a form. This includes both primitive value fields (e.g. fields that contain a `string` or `number`), as well as "grouping fields" that contain sub-fields. [`FieldTree`](fieldtree) objects are arranged in a tree whose structure mimics the structure of the underlying data. For example a `FieldTree<{x: number}>` has a property `x` which contains a `FieldTree<number>`. To access the state associated with a field, call it as a function.

## API

```
type FieldTree<TModel, TKey extends string | number = string | number> = (() => [TModel] extends [AbstractControl]
    ? CompatFieldState<TModel, TKey>
    : FieldState<TModel, TKey>) &
    // Children:
    ([TModel] extends [AbstractControl]
      ? object
      : [TModel] extends [Array<infer U>]
        ? ReadonlyArrayLike<MaybeFieldTree<U, number>>
        : TModel extends Record<string, any>
          ? Subfields<TModel>
          : object)
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FieldTree>
