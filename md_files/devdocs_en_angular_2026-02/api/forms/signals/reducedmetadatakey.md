# reducedMetadataKey

reducedMetadataKey



# reducedMetadataKey

Creates an [`AggregateMetadataKey`](aggregatemetadatakey) that reduces its individual values into an accumulated value using the given `reduce` and `getInitial` functions.

## API

```
function reducedMetadataKey<TAcc, TItem>(
  reduce: (acc: TAcc, item: TItem) => TAcc,
  getInitial: NoInfer<() => TAcc>,
): AggregateMetadataKey<TAcc, TItem>;
```

### reducedMetadataKey

`AggregateMetadataKey<TAcc, TItem>`

Creates an [`AggregateMetadataKey`](aggregatemetadatakey) that reduces its individual values into an accumulated value using the given `reduce` and `getInitial` functions.

@paramreduce`(acc: TAcc, item: TItem) => TAcc`

The reducer function.

@paramgetInitial`NoInfer<() => TAcc>`

A function that gets the initial value for the reduce operation.

@returns`AggregateMetadataKey<TAcc, TItem>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/reducedMetadataKey>
