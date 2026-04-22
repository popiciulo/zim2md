# WithOptionalField

WithOptionalField



# WithOptionalField

A type that allows the given type `T` to optionally have a `field` property.

## API

```
type WithOptionalField<T> = Omit<T, 'field'> & {field?: FieldTree<unknown>}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/WithOptionalField>
