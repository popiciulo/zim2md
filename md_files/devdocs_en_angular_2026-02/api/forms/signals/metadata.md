# metadata

metadata



# metadata

## API

```
function metadata<TValue, TData, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  factory: (ctx: FieldContext<TValue, TPathKind>) => TData,
): MetadataKey<TData>;
function metadata<TValue, TData, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  key: MetadataKey<TData>,
  factory: (ctx: FieldContext<TValue, TPathKind>) => TData,
): MetadataKey<TData>;
```

```
function metadata<TValue, TData, TPathKind = PathKind.Root>(path: SchemaPath<TValue, 1, TPathKind>, factory: (ctx: FieldContext<TValue, TPathKind>) => TData): MetadataKey<TData>;
```

Creates a new [`MetadataKey`](metadatakey) and defines the value of the new metadata key for the given field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The path to define the metadata for.

@paramfactory`(ctx: FieldContext<TValue, TPathKind>) => TData`

A factory function that creates the value for the metadata. This function is **not** reactive. It is run once when the field is created.

@returns`MetadataKey<TData>`

```
function metadata<TValue, TData, TPathKind = PathKind.Root>(path: SchemaPath<TValue, 1, TPathKind>, key: MetadataKey<TData>, factory: (ctx: FieldContext<TValue, TPathKind>) => TData): MetadataKey<TData>;
```

Defines the value of a [`MetadataKey`](metadatakey) for a given field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The path to define the metadata for.

@paramkey`MetadataKey<TData>`

The metadata key to define.

@paramfactory`(ctx: FieldContext<TValue, TPathKind>) => TData`

A factory function that creates the value for the metadata. This function is **not** reactive. It is run once when the field is created.

@returns`MetadataKey<TData>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/metadata>
