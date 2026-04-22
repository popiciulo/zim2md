# ItemType

ItemType



# ItemType

Gets the item type of an object that is possibly an array.

## API

```
type ItemType<T extends Object> = T extends ReadonlyArray<any> ? T[number] : T[keyof T]
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/ItemType>
