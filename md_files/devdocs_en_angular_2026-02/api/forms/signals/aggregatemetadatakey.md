# AggregateMetadataKey

AggregateMetadataKey



# AggregateMetadataKey

Represents metadata that is aggregated from multiple parts according to the key's reducer function. A value can be contributed to the aggregated value for a field using an [`aggregateMetadata`](aggregatemetadata) rule in the schema. There may be multiple rules in a schema that contribute values to the same [`AggregateMetadataKey`](aggregatemetadatakey) of the same field.

## API

```
class AggregateMetadataKey<TAcc, TItem> {
  constructor(reduce: (acc: TAcc, item: TItem) => TAcc, getInitial: () => TAcc): AggregateMetadataKey<TAcc, TItem>;
}
```

### constructor

`AggregateMetadataKey<TAcc, TItem>`

Use [`reducedMetadataKey`](reducedmetadatakey).

@paramreduce`(acc: TAcc, item: TItem) => TAcc`

@paramgetInitial`() => TAcc`

@returns`AggregateMetadataKey<TAcc, TItem>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/AggregateMetadataKey>
