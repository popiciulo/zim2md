# WithProperties

WithProperties



# WithProperties

Additional type information that can be added to the NgElement class, for properties that are added based on the inputs and methods of the underlying component.

## API

```
type WithProperties<P> = {
  [property in keyof P]: P[property];
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/WithProperties>
