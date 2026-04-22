# IterableChanges

IterableChanges



# IterableChanges

An object describing the changes in the `Iterable` collection since last time [`IterableDiffer#diff()`](iterablediffer#diff) was invoked.

## API

```
interface IterableChanges<V> {
  forEachItem(fn: (record: IterableChangeRecord<V>) => void): void;
  forEachOperation(fn: (record: IterableChangeRecord<V>, previousIndex: number | null, currentIndex: number | null) => void): void;
  forEachPreviousItem(fn: (record: IterableChangeRecord<V>) => void): void;
  forEachAddedItem(fn: (record: IterableChangeRecord<V>) => void): void;
  forEachMovedItem(fn: (record: IterableChangeRecord<V>) => void): void;
  forEachRemovedItem(fn: (record: IterableChangeRecord<V>) => void): void;
  forEachIdentityChange(fn: (record: IterableChangeRecord<V>) => void): void;
}
```

### forEachItem

`void`

Iterate over all changes. [`IterableChangeRecord`](iterablechangerecord) will contain information about changes to each item.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

### forEachOperation

`void`

Iterate over a set of operations which when applied to the original `Iterable` will produce the new `Iterable`.

**NOTE:** These are not necessarily the actual operations which were applied to the original `Iterable`, rather these are a set of computed operations which may not be the same as the ones applied.

@paramfn`(record: IterableChangeRecord<V>, previousIndex: number | null, currentIndex: number | null) => void`

@returns`void`

### forEachPreviousItem

`void`

Iterate over changes in the order of original `Iterable` showing where the original items have moved.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

### forEachAddedItem

`void`

Iterate over all added items.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

### forEachMovedItem

`void`

Iterate over all moved items.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

### forEachRemovedItem

`void`

Iterate over all removed items.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

### forEachIdentityChange

`void`

Iterate over all items which had their identity (as computed by the [`TrackByFunction`](trackbyfunction)) changed.

@paramfn`(record: IterableChangeRecord<V>) => void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/IterableChanges>
