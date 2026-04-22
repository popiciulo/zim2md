# SchemaPathTree

SchemaPathTree



# SchemaPathTree

Nested schema path.

## API

```
type SchemaPathTree<TModel, TPathKind extends PathKind = PathKind.Root> = ([TModel] extends [AbstractControl]
    ? CompatSchemaPath<TModel, TPathKind>
    : SchemaPath<TModel, SchemaPathRules.Supported, TPathKind>) &
    // Subpaths
    (TModel extends AbstractControl
      ? unknown
      : // Array paths have no subpaths
        TModel extends Array<any>
        ? unknown
        : // Object subfields
          TModel extends Record<string, any>
          ? {[K in keyof TModel]: MaybeSchemaPathTree<TModel[K], PathKind.Child>}
          : // Primitive or other type - no subpaths
            unknown)
```

## Description

Nested schema path.

It mirrors the structure of a given data structure, and allows applying rules to the appropriate fields.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/SchemaPathTree>
