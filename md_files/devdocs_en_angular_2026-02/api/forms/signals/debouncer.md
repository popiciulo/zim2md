# Debouncer

Debouncer



# Debouncer

A function that defines custom debounce logic for a field.

## API

```
type Debouncer<TValue, TPathKind extends PathKind = PathKind.Root> = (
  context: FieldContext<TValue, TPathKind>,
  abortSignal: AbortSignal,
) => Promise<void> | void
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/Debouncer>
