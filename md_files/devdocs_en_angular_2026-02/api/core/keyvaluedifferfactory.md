# KeyValueDifferFactory

KeyValueDifferFactory



# KeyValueDifferFactory

Provides a factory for [`KeyValueDiffer`](keyvaluediffer).

## API

```
interface KeyValueDifferFactory {
  supports(objects: any): boolean;
  create<K, V>(): KeyValueDiffer<K, V>;
}
```

### supports

`boolean`

Test to see if the differ knows how to diff this kind of object.

@paramobjects`any`

@returns`boolean`

### create

`KeyValueDiffer<K, V>`

Create a [`KeyValueDiffer`](keyvaluediffer).

@returns`KeyValueDiffer<K, V>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/KeyValueDifferFactory>
