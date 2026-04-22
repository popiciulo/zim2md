# copyArrayItem

copyArrayItem



# copyArrayItem

Copies an item from one array to another, leaving it in its original position in current array.

## API

```
function copyArrayItem<T = any>(
  currentArray: T[],
  targetArray: T[],
  currentIndex: number,
  targetIndex: number,
): void;
```

### copyArrayItem

`void`

Copies an item from one array to another, leaving it in its original position in current array.

@paramcurrentArray`T[]`

Array from which to copy the item.

@paramtargetArray`T[]`

Array into which is copy the item.

@paramcurrentIndex`number`

Index of the item in its current array.

@paramtargetIndex`number`

Index at which to insert the item.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/copyArrayItem>
