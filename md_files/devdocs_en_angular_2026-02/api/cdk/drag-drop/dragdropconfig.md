# DragDropConfig

DragDropConfig



# DragDropConfig

Object that can be used to configure the drag items and drop lists within a module or a component.

## API

```
interface DragDropConfig extends Partial<DragRefConfig> {
  lockAxis?: DragAxis | null | undefined;
  dragStartDelay?: DragStartDelay | undefined;
  constrainPosition?: DragConstrainPosition | undefined;
  previewClass?: string | string[] | undefined;
  boundaryElement?: string | undefined;
  rootElementSelector?: string | undefined;
  draggingDisabled?: boolean | undefined;
  sortingDisabled?: boolean | undefined;
  listAutoScrollDisabled?: boolean | undefined;
  listOrientation?: DropListOrientation | undefined;
  zIndex?: number | undefined;
  previewContainer?: "global" | "parent" | undefined;
  override dragStartThreshold: number;
  override pointerDirectionChangeThreshold: number;
  override parentDragRef?: DragRef<any> | undefined;
}
```

### lockAxis

`DragAxis | null | undefined`

### dragStartDelay

`DragStartDelay | undefined`

### constrainPosition

`DragConstrainPosition | undefined`

### previewClass

`string | string[] | undefined`

### boundaryElement

`string | undefined`

### rootElementSelector

`string | undefined`

### draggingDisabled

`boolean | undefined`

### sortingDisabled

`boolean | undefined`

### listAutoScrollDisabled

`boolean | undefined`

### listOrientation

`DropListOrientation | undefined`

### zIndex

`number | undefined`

### previewContainer

`"global" | "parent" | undefined`

### dragStartThreshold

`number`

Minimum amount of pixels that the user should drag, before the CDK initiates a drag sequence.

### pointerDirectionChangeThreshold

`number`

Amount the pixels the user should drag before the CDK considers them to have changed the drag direction.

### parentDragRef

`DragRef<any> | undefined`

Ref that the current drag item is nested in.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/DragDropConfig>
