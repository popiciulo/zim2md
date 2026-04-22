# DragRefConfig

DragRefConfig



# DragRefConfig

Object that can be used to configure the behavior of DragRef.

## API

```
interface DragRefConfig {
  dragStartThreshold: number;
  pointerDirectionChangeThreshold: number;
  zIndex?: number | undefined;
  parentDragRef?: DragRef<any> | undefined;
}
```

### dragStartThreshold

`number`

Minimum amount of pixels that the user should drag, before the CDK initiates a drag sequence.

### pointerDirectionChangeThreshold

`number`

Amount the pixels the user should drag before the CDK considers them to have changed the drag direction.

### zIndex

`number | undefined`

`z-index` for the absolutely-positioned elements that are created by the drag item.

### parentDragRef

`DragRef<any> | undefined`

Ref that the current drag item is nested in.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/DragRefConfig>
