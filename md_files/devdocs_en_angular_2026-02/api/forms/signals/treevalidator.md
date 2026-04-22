# TreeValidator

TreeValidator



# TreeValidator

A function that takes the [`FieldContext`](fieldcontext) for the field being validated and returns a [`TreeValidationResult`](treevalidationresult) indicating errors for the field and its sub-fields.

## API

```
type TreeValidator<TValue, TPathKind extends PathKind = PathKind.Root> = LogicFn<
  TValue,
  TreeValidationResult,
  TPathKind
>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/TreeValidator>
