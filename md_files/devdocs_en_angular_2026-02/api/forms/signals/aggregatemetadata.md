# aggregateMetadata

aggregateMetadata



# aggregateMetadata

Adds a value to an [`AggregateMetadataKey`](aggregatemetadatakey) of a field.

## API

```
function aggregateMetadata<
  TValue,
  TMetadataItem,
  TPathKind extends PathKind = PathKind.Root,
>(
  path: SchemaPath<TValue, 1, TPathKind>,
  key: AggregateMetadataKey<any, TMetadataItem>,
  logic: NoInfer<LogicFn<TValue, TMetadataItem, TPathKind>>,
): void;
```

### aggregateMetadata

`void`

Adds a value to an [`AggregateMetadataKey`](aggregatemetadatakey) of a field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to set the aggregate metadata on.

@paramkey`AggregateMetadataKey<any, TMetadataItem>`

The aggregate metadata key

@paramlogic`NoInfer<LogicFn<TValue, TMetadataItem, TPathKind>>`

A function that receives the [`FieldContext`](fieldcontext) and returns a value to add to the aggregate metadata.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/aggregateMetadata>
