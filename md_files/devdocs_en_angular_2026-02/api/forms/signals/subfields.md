# Subfields

Subfields



# Subfields

The sub-fields that a user can navigate to from a `FieldTree<TModel>`.

## API

```
type Subfields<TModel> = {
  readonly [K in keyof TModel as TModel[K] extends Function ? never : K]: MaybeFieldTree<
    TModel[K],
    string
  >;
} & {
  [Symbol.iterator](): Iterator<[string, MaybeFieldTree<TModel[keyof TModel], string>]>;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/Subfields>
