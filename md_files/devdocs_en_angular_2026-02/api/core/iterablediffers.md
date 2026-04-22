# IterableDiffers

IterableDiffers



# IterableDiffers

A repository of different iterable diffing strategies used by NgFor, NgClass, and others.

## API

```
class IterableDiffers {
  constructor(factories: IterableDifferFactory[]): IterableDiffers;
  find(iterable: any): IterableDifferFactory;
  static create(factories: IterableDifferFactory[], parent?: IterableDiffers | undefined): IterableDiffers;
  static extend(factories: IterableDifferFactory[]): StaticProvider;
}
```

### constructor

`IterableDiffers`

@paramfactories`IterableDifferFactory[]`

@returns`IterableDiffers`

### find

`IterableDifferFactory`

@paramiterable`any`

@returns`IterableDifferFactory`

### create

`IterableDiffers`

@paramfactories`IterableDifferFactory[]`

@paramparent`IterableDiffers | undefined`

@returns`IterableDiffers`

### extend

`StaticProvider`

Takes an array of [`IterableDifferFactory`](iterabledifferfactory) and returns a provider used to extend the inherited [`IterableDiffers`](iterablediffers) instance with the provided factories and return a new [`IterableDiffers`](iterablediffers) instance.

@paramfactories`IterableDifferFactory[]`

@returns`StaticProvider`

Usage notes

### Example

The following example shows how to extend an existing list of factories, which will only be applied to the injector for this component and its children. This step is all that's required to make a new [`IterableDiffer`](iterablediffer) available.

```
@Component({
  viewProviders: [
    IterableDiffers.extend([new ImmutableListDiffer()])
  ]
})
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/IterableDiffers>
