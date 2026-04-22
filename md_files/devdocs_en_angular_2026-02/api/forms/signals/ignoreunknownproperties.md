# IgnoreUnknownProperties

IgnoreUnknownProperties



# IgnoreUnknownProperties

Utility type that recursively ignores unknown string index properties on the given object. We use this on the `TSchema` type in [`validateStandardSchema`](validatestandardschema) in order to accommodate Zod's `looseObject` which includes `{[key: string]: unknown}` as part of the type.

## API

```
type IgnoreUnknownProperties<T> = T extends Record<PropertyKey, unknown>
    ? {
        [K in keyof T as RemoveStringIndexUnknownKey<K, T[K]>]: IgnoreUnknownProperties<T[K]>;
      }
    : T
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/IgnoreUnknownProperties>
