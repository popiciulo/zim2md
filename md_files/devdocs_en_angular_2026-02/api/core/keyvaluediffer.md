# KeyValueDiffer

KeyValueDiffer



# KeyValueDiffer

A differ that tracks changes made to an object over time.

## API

```
interface KeyValueDiffer<K, V> {
  diff(object: Map<K, V>): KeyValueChanges<K, V> | null;
  diff(object: { [key: string]: V; }): KeyValueChanges<string, V> | null;
}
```

### diff

`KeyValueChanges<K, V> | null`

Compute a difference between the previous state and the new `object` state.

@paramobject`Map<K, V>`

containing the new value.

@returns`KeyValueChanges<K, V> | null`

### diff

`KeyValueChanges<string, V> | null`

Compute a difference between the previous state and the new `object` state.

@paramobject`{ [key: string]: V; }`

containing the new value.

@returns`KeyValueChanges<string, V> | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/KeyValueDiffer>
