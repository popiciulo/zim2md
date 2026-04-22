# LogicFn

LogicFn



# LogicFn

A function that receives the [`FieldContext`](fieldcontext) for the field the logic is bound to and returns a specific result type.

## API

```
type LogicFn<TValue, TReturn, TPathKind extends PathKind = PathKind.Root> = (
  ctx: FieldContext<TValue, TPathKind>,
) => TReturn
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/LogicFn>
