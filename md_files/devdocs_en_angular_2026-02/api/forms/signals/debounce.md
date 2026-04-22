# debounce

debounce



# debounce

Configures the frequency at which a form field is updated by UI events.

## API

```
function debounce<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  durationOrDebouncer: number | Debouncer<TValue, TPathKind>,
): void;
```

### debounce

`void`

Configures the frequency at which a form field is updated by UI events.

When this rule is applied, updates from the UI to the form model will be delayed until either the field is touched, or the most recently debounced update resolves.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to debounce.

@paramdurationOrDebouncer`number | Debouncer<TValue, TPathKind>`

Either a debounce duration in milliseconds, or a custom [`Debouncer`](debouncer) function.

@returns`void`

## Description

Configures the frequency at which a form field is updated by UI events.

When this rule is applied, updates from the UI to the form model will be delayed until either the field is touched, or the most recently debounced update resolves.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/debounce>
