# KeyValueChangeRecord

KeyValueChangeRecord



# KeyValueChangeRecord

Record representing the item change information.

## API

```
interface KeyValueChangeRecord<K, V> {
  readonly key: K;
  readonly currentValue: V | null;
  readonly previousValue: V | null;
}
```

### key

`K`

Current key in the Map.

### currentValue

`V | null`

Current value for the key or `null` if removed.

### previousValue

`V | null`

Previous value for the key or `null` if added.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/KeyValueChangeRecord>
