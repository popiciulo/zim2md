# KeyValueChanges

KeyValueChanges



# KeyValueChanges

An object describing the changes in the `Map` or `{[k:string]: string}` since last time [`KeyValueDiffer#diff()`](keyvaluediffer#diff) was invoked.

## API

```
interface KeyValueChanges<K, V> {
  forEachItem(fn: (r: KeyValueChangeRecord<K, V>) => void): void;
  forEachPreviousItem(fn: (r: KeyValueChangeRecord<K, V>) => void): void;
  forEachChangedItem(fn: (r: KeyValueChangeRecord<K, V>) => void): void;
  forEachAddedItem(fn: (r: KeyValueChangeRecord<K, V>) => void): void;
  forEachRemovedItem(fn: (r: KeyValueChangeRecord<K, V>) => void): void;
}
```

### forEachItem

`void`

Iterate over all changes. [`KeyValueChangeRecord`](keyvaluechangerecord) will contain information about changes to each item.

@paramfn`(r: KeyValueChangeRecord<K, V>) => void`

@returns`void`

### forEachPreviousItem

`void`

Iterate over changes in the order of original Map showing where the original items have moved.

@paramfn`(r: KeyValueChangeRecord<K, V>) => void`

@returns`void`

### forEachChangedItem

`void`

Iterate over all keys for which values have changed.

@paramfn`(r: KeyValueChangeRecord<K, V>) => void`

@returns`void`

### forEachAddedItem

`void`

Iterate over all added items.

@paramfn`(r: KeyValueChangeRecord<K, V>) => void`

@returns`void`

### forEachRemovedItem

`void`

Iterate over all removed items.

@paramfn`(r: KeyValueChangeRecord<K, V>) => void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/KeyValueChanges>
