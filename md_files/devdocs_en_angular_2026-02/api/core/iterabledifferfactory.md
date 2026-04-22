# IterableDifferFactory

IterableDifferFactory



# IterableDifferFactory

Provides a factory for [`IterableDiffer`](iterablediffer).

## API

```
interface IterableDifferFactory {
  supports(objects: any): boolean;
  create<V>(trackByFn?: TrackByFunction<V> | undefined): IterableDiffer<V>;
}
```

### supports

`boolean`

@paramobjects`any`

@returns`boolean`

### create

`IterableDiffer<V>`

@paramtrackByFn`TrackByFunction<V> | undefined`

@returns`IterableDiffer<V>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/IterableDifferFactory>
