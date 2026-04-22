# DragDrop

DragDrop



# DragDrop

Service that allows for drag-and-drop functionality to be attached to DOM elements.

## API

```
class DragDrop {
  createDrag<T = any>(element: any, config?: DragRefConfig): DragRef<T>;
  createDropList<T = any>(element: any): DropListRef<T>;
}
```

### createDrag

`DragRef<T>`

Turns an element into a draggable item.

@paramelement`any`

Element to which to attach the dragging functionality.

@paramconfig`DragRefConfig`

Object used to configure the dragging behavior.

@returns`DragRef<T>`

### createDropList

`DropListRef<T>`

Turns an element into a drop list.

@paramelement`any`

Element to which to attach the drop list functionality.

@returns`DropListRef<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/DragDrop>
