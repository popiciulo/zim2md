# SimpleChanges

SimpleChanges



# SimpleChanges

A hashtable of changes represented by [`SimpleChange`](simplechange) objects stored at the declared property name they belong to on a Directive or Component. This is the type passed to the `ngOnChanges` hook. Pass the current class or `this` as the first generic argument for stronger type checking (e.g. `SimpleChanges<YourComponent>`).

[OnChanges](onchanges)[Inspecting changes](../../guide/components/lifecycle#inspecting-changes)

## API

```
type SimpleChanges<T = unknown> = T extends object
  ? {
      [Key in keyof T]?: SimpleChange<
        T[Key] extends {[ɵINPUT_SIGNAL_BRAND_READ_TYPE]: infer V} ? V : T[Key]
      >;
    }
  : {
      [propName: string]: SimpleChange; // Backwards-compatible signature.
    }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/SimpleChanges>
