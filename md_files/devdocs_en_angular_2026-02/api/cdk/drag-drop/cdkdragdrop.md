# CdkDragDrop

CdkDragDrop



# CdkDragDrop

Event emitted when the user drops a draggable item inside a drop container.

## API

```
interface CdkDragDrop<T, O = T, I = any> {
  previousIndex: number;
  currentIndex: number;
  item: CdkDrag<I>;
  container: CdkDropList<T>;
  previousContainer: CdkDropList<O>;
  isPointerOverContainer: boolean;
  distance: { x: number; y: number; };
  dropPoint: { x: number; y: number; };
  event: MouseEvent | TouchEvent;
}
```

### previousIndex

`number`

Index of the item when it was picked up.

### currentIndex

`number`

Current index of the item.

### item

`CdkDrag<I>`

Item that is being dropped.

### container

`CdkDropList<T>`

Container in which the item was dropped.

### previousContainer

`CdkDropList<O>`

Container from which the item was picked up. Can be the same as the `container`.

### isPointerOverContainer

`boolean`

Whether the user's pointer was over the container when the item was dropped.

### distance

`{ x: number; y: number; }`

Distance in pixels that the user has dragged since the drag sequence started.

### dropPoint

`{ x: number; y: number; }`

Position where the pointer was when the item was dropped

### event

`MouseEvent | TouchEvent`

Native event that caused the drop event.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragDrop>
