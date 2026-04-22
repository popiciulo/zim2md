# FieldValidator

FieldValidator



# FieldValidator

A function that takes the [`FieldContext`](fieldcontext) for the field being validated and returns a [`ValidationResult`](validationresult) indicating errors for the field.

## API

```
type FieldValidator<TValue, TPathKind extends PathKind = PathKind.Root> = LogicFn<
  TValue,
  ValidationResult<ValidationError.WithoutField>,
  TPathKind
>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FieldValidator>
