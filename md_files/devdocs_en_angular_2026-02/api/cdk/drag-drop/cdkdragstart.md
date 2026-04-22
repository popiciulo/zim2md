# CdkDragStart

CdkDragStart



# CdkDragStart

Event emitted when the user starts dragging a draggable.

## API

```
interface CdkDragStart<T = any> {
  source: CdkDrag<T>;
  event: MouseEvent | TouchEvent;
}
```

### source

`CdkDrag<T>`

Draggable that emitted the event.

### event

`MouseEvent | TouchEvent`

Native event that started the drag sequence.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragStart>
