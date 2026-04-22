# validateStandardSchema

validateStandardSchema



# validateStandardSchema

Validates a field using a `StandardSchemaV1` compatible validator (e.g. a Zod validator).

## API

```
function validateStandardSchema<
  TSchema,
  TModel extends IgnoreUnknownProperties<TSchema>,
>(
  path: SchemaPath<TModel> &
    ([TModel] extends [AbstractControl]
      ? CompatSchemaPath<TModel, Root>
      : SchemaPath<TModel, 1, Root>) &
    (TModel extends AbstractControl
      ? unknown
      : TModel extends any[]
        ? unknown
        : TModel extends Record<string, any>
          ? { [K in keyof TModel]: MaybeSchemaPathTree<TModel[K], Child> }
          : unknown),
  schema: StandardSchemaV1<TSchema>,
): void;
```

### validateStandardSchema

`void`

Validates a field using a `StandardSchemaV1` compatible validator (e.g. a Zod validator).

See <https://github.com/standard-schema/standard-schema> for more about standard schema.

@parampath`SchemaPath<TModel> & ([TModel] extends [AbstractControl] ? CompatSchemaPath<TModel, Root> : SchemaPath<TModel, 1, Root>) & (TModel extends AbstractControl ? unknown : TModel extends any[] ? unknown : TModel extends Record<string, any> ? { [K in keyof TModel]: MaybeSchemaPathTree<TModel[K], Child>; } : unknown)`

The `FieldPath` to the field to validate.

@paramschema`StandardSchemaV1<TSchema>`

The standard schema compatible validator to use for validation.

@returns`void`

## Description

Validates a field using a `StandardSchemaV1` compatible validator (e.g. a Zod validator).

See <https://github.com/standard-schema/standard-schema> for more about standard schema.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/validateStandardSchema>
