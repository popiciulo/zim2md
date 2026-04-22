# KeyValueDiffers

KeyValueDiffers



# KeyValueDiffers

A repository of different Map diffing strategies used by NgClass, NgStyle, and others.

## API

```
class KeyValueDiffers {
  constructor(factories: KeyValueDifferFactory[]): KeyValueDiffers;
  find(kv: any): KeyValueDifferFactory;
  static create<S>(factories: KeyValueDifferFactory[], parent?: KeyValueDiffers | undefined): KeyValueDiffers;
  static extend<S>(factories: KeyValueDifferFactory[]): StaticProvider;
}
```

### constructor

`KeyValueDiffers`

@paramfactories`KeyValueDifferFactory[]`

@returns`KeyValueDiffers`

### find

`KeyValueDifferFactory`

@paramkv`any`

@returns`KeyValueDifferFactory`

### create

`KeyValueDiffers`

@paramfactories`KeyValueDifferFactory[]`

@paramparent`KeyValueDiffers | undefined`

@returns`KeyValueDiffers`

### extend

`StaticProvider`

Takes an array of [`KeyValueDifferFactory`](keyvaluedifferfactory) and returns a provider used to extend the inherited [`KeyValueDiffers`](keyvaluediffers) instance with the provided factories and return a new [`KeyValueDiffers`](keyvaluediffers) instance.

@paramfactories`KeyValueDifferFactory[]`

@returns`StaticProvider`

Usage notes

### Example

The following example shows how to extend an existing list of factories, which will only be applied to the injector for this component and its children. This step is all that's required to make a new [`KeyValueDiffer`](keyvaluediffer) available.

```
@Component({
  viewProviders: [
    KeyValueDiffers.extend([new ImmutableMapDiffer()])
  ]
})
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/KeyValueDiffers>
