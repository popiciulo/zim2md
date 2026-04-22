# CdkDragEnter

CdkDragEnter



# CdkDragEnter

Event emitted when the user moves an item into a new drop container.

## API

```
interface CdkDragEnter<T = any, I = T> {
  container: CdkDropList<T>;
  item: CdkDrag<I>;
  currentIndex: number;
}
```

### container

`CdkDropList<T>`

Container into which the user has moved the item.

### item

`CdkDrag<I>`

Item that was moved into the container.

### currentIndex

`number`

Index at which the item has entered the container.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragEnter>
