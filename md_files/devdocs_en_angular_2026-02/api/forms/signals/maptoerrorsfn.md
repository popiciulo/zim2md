# MapToErrorsFn

MapToErrorsFn



# MapToErrorsFn

A function that takes the result of an async operation and the current field context, and maps it to a list of validation errors.

## API

```
type MapToErrorsFn<TValue, TResult, TPathKind extends PathKind = PathKind.Root> = (
  result: TResult,
  ctx: FieldContext<TValue, TPathKind>,
) => TreeValidationResult
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/MapToErrorsFn>
