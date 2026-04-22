# IterableChangeRecord

IterableChangeRecord



# IterableChangeRecord

Record representing the item change information.

## API

```
interface IterableChangeRecord<V> {
  readonly currentIndex: number | null;
  readonly previousIndex: number | null;
  readonly item: V;
  readonly trackById: any;
}
```

### currentIndex

`number | null`

Current index of the item in `Iterable` or null if removed.

### previousIndex

`number | null`

Previous index of the item in `Iterable` or null if added.

### item

`V`

The item.

### trackById

`any`

Track by identity as computed by the [`TrackByFunction`](trackbyfunction).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/IterableChangeRecord>
