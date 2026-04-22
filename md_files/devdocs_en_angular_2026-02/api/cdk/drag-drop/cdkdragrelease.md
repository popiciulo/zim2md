# CdkDragRelease

CdkDragRelease



# CdkDragRelease

Event emitted when the user releases an item, before any animations have started.

## API

```
interface CdkDragRelease<T = any> {
  source: CdkDrag<T>;
  event: MouseEvent | TouchEvent;
}
```

### source

`CdkDrag<T>`

Draggable that emitted the event.

### event

`MouseEvent | TouchEvent`

Native event that caused the release event.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragRelease>
