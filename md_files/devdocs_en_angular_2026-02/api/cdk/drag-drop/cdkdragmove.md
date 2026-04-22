# CdkDragMove

CdkDragMove



# CdkDragMove

Event emitted as the user is dragging a draggable item.

## API

```
interface CdkDragMove<T = any> {
  source: CdkDrag<T>;
  pointerPosition: { x: number; y: number; };
  event: MouseEvent | TouchEvent;
  distance: { x: number; y: number; };
  delta: { x: 0 | 1 | -1; y: 0 | 1 | -1; };
}
```

### source

`CdkDrag<T>`

Item that is being dragged.

### pointerPosition

`{ x: number; y: number; }`

Position of the user's pointer on the page.

### event

`MouseEvent | TouchEvent`

Native event that is causing the dragging.

### distance

`{ x: number; y: number; }`

Distance in pixels that the user has dragged since the drag sequence started.

### delta

`{ x: 0 | 1 | -1; y: 0 | 1 | -1; }`

Indicates the direction in which the user is dragging the element along each axis. `1` means that the position is increasing (e.g. the user is moving to the right or downwards), whereas `-1` means that it's decreasing (they're moving to the left or upwards). `0` means that the position hasn't changed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragMove>
