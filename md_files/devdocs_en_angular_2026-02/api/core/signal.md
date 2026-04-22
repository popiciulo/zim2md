# Signal

Signal



# Signal

A reactive value which notifies consumers of any changes.

[What are signals?](../../guide/signals#what-are-signals)

## API

```
type Signal<T> = (() => T) & {
  [SIGNAL]: unknown;
}
```

## Description

A reactive value which notifies consumers of any changes.

Signals are functions which returns their current value. To access the current value of a signal, call it.

Ordinary values can be turned into [`Signal`](signal)s with the [`signal`](signal) function.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Signal>
