# CdkDragEnd

CdkDragEnd



# CdkDragEnd

Event emitted when the user stops dragging a draggable.

## API

```
interface CdkDragEnd<T = any> {
  source: CdkDrag<T>;
  distance: { x: number; y: number; };
  dropPoint: { x: number; y: number; };
  event: MouseEvent | TouchEvent;
}
```

### source

`CdkDrag<T>`

Draggable that emitted the event.

### distance

`{ x: number; y: number; }`

Distance in pixels that the user has dragged since the drag sequence started.

### dropPoint

`{ x: number; y: number; }`

Position where the pointer was when the item was dropped

### event

`MouseEvent | TouchEvent`

Native event that caused the dragging to stop.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragEnd>
