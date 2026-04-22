# IterableDiffer

IterableDiffer



# IterableDiffer

A strategy for tracking changes over time to an iterable. Used by [`NgForOf`](../common/ngforof) to respond to changes in an iterable by effecting equivalent changes in the DOM.

## API

```
interface IterableDiffer<V> {
  diff(object: NgIterable<V> | null | undefined): IterableChanges<V> | null;
}
```

### diff

`IterableChanges<V> | null`

Compute a difference between the previous state and the new `object` state.

@paramobject`NgIterable<V> | null | undefined`

containing the new value.

@returns`IterableChanges<V> | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/IterableDiffer>
