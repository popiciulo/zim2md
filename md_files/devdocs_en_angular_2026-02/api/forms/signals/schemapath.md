# SchemaPath

SchemaPath



# SchemaPath

An object that represents a location in the [`FieldTree`](fieldtree) tree structure and is used to bind logic to a particular part of the structure prior to the creation of the form. Because the `FieldPath` exists prior to the form's creation, it cannot be used to access any of the field state.

## API

```
type SchemaPath<TValue, TSupportsRules extends SchemaPathRules = SchemaPathRules.Supported, TPathKind extends PathKind = PathKind.Root> = {
  [ɵɵTYPE]: {
    value: () => TValue;
    supportsRules: TSupportsRules;
    pathKind: TPathKind;
  };
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/SchemaPath>
