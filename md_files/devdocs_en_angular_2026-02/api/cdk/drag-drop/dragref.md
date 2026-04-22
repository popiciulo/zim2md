# DragRef

DragRef



# DragRef

Reference to a draggable item. Used to manipulate or dispose of the item.

## API

```
class DragRef<T = any> {
  constructor(element: any, _config: DragRefConfig, _document: Document, _ngZone: NgZone, _viewportRuler: ViewportRuler, _dragDropRegistry: DragDropRegistry, _renderer: Renderer2): DragRef<T>;
  lockAxis: "x" | "y" | null;
  dragStartDelay: number | { touch: number; mouse: number; };
  previewClass: string | string[] | undefined;
  scale: number;
   get disabled(): boolean;
  readonly beforeStarted: any;
  readonly started: any;
  readonly released: any;
  readonly ended: any;
  readonly entered: any;
  readonly exited: any;
  readonly dropped: any;
  readonly moved: Observable<{ source: DragRef<any>; pointerPosition: { x: number; y: number; }; event: MouseEvent | TouchEvent; distance: Point; delta: { x: 0 | 1 | -1; y: 0 | 1 | -1; }; }>;
  data: T;
  constrainPosition?: DragConstrainPosition | undefined;
  getPlaceholderElement(): HTMLElement;
  getRootElement(): HTMLElement;
  getVisibleElement(): HTMLElement;
  withHandles(handles: any[]): this;
  withPreviewTemplate(template: DragPreviewTemplate<any> | null): this;
  withPlaceholderTemplate(template: DragHelperTemplate<any> | null): this;
  withRootElement(rootElement: any): this;
  withBoundaryElement(boundaryElement: any): this;
  withParent(parent: DragRef<unknown> | null): this;
  dispose(): void;
  isDragging(): boolean;
  reset(): void;
  resetToBoundary(): void;
  disableHandle(handle: HTMLElement): void;
  enableHandle(handle: HTMLElement): void;
  withDirection(direction: Direction): this;
  getFreeDragPosition(): Readonly<Point>;
  setFreeDragPosition(value: Point): this;
  withPreviewContainer(value: any): this;
}
```

### constructor

`DragRef<T>`

@paramelement`any`

@param\_config`DragRefConfig`

@param\_document`Document`

@param\_ngZone`NgZone`

@param\_viewportRuler`ViewportRuler`

@param\_dragDropRegistry`DragDropRegistry`

@param\_renderer`Renderer2`

@returns`DragRef<T>`

### lockAxis

`"x" | "y" | null`

Axis along which dragging is locked.

### dragStartDelay

`number | { touch: number; mouse: number; }`

Amount of milliseconds to wait after the user has put their pointer down before starting to drag the element.

### previewClass

`string | string[] | undefined`

Class to be added to the preview element.

### scale

`number`

If the parent of the dragged element has a `scale` transform, it can throw off the positioning when the user starts dragging. Use this input to notify the CDK of the scale.

### disabled

`boolean`

Whether starting to drag this element is disabled.

### disabled

`boolean`

### beforeStarted

`any`

Emits as the drag sequence is being prepared.

### started

`any`

Emits when the user starts dragging the item.

### released

`any`

Emits when the user has released a drag item, before any animations have started.

### ended

`any`

Emits when the user stops dragging an item in the container.

### entered

`any`

Emits when the user has moved the item into a new container.

### exited

`any`

Emits when the user removes the item its container by dragging it into another container.

### dropped

`any`

Emits when the user drops the item inside a container.

### moved

`Observable<{ source: DragRef<any>; pointerPosition: { x: number; y: number; }; event: MouseEvent | TouchEvent; distance: Point; delta: { x: 0 | 1 | -1; y: 0 | 1 | -1; }; }>`

Emits as the user is dragging the item. Use with caution, because this event will fire for every pixel that the user has dragged.

### data

`T`

Arbitrary data that can be attached to the drag item.

### constrainPosition

`DragConstrainPosition | undefined`

Function that can be used to customize the logic of how the position of the drag item is limited while it's being dragged. Gets called with a point containing the current position of the user's pointer on the page, a reference to the item being dragged and its dimensions. Should return a point describing where the item should be rendered.

### getPlaceholderElement

`HTMLElement`

Returns the element that is being used as a placeholder while the current element is being dragged.

@returns`HTMLElement`

### getRootElement

`HTMLElement`

Returns the root draggable element.

@returns`HTMLElement`

### getVisibleElement

`HTMLElement`

Gets the currently-visible element that represents the drag item. While dragging this is the placeholder, otherwise it's the root element.

@returns`HTMLElement`

### withHandles

`this`

Registers the handles that can be used to drag the element.

@paramhandles`any[]`

@returns`this`

### withPreviewTemplate

`this`

Registers the template that should be used for the drag preview.

@paramtemplate`DragPreviewTemplate<any> | null`

Template that from which to stamp out the preview.

@returns`this`

### withPlaceholderTemplate

`this`

Registers the template that should be used for the drag placeholder.

@paramtemplate`DragHelperTemplate<any> | null`

Template that from which to stamp out the placeholder.

@returns`this`

### withRootElement

`this`

Sets an alternate drag root element. The root element is the element that will be moved as the user is dragging. Passing an alternate root element is useful when trying to enable dragging on an element that you might not have access to.

@paramrootElement`any`

@returns`this`

### withBoundaryElement

`this`

Element to which the draggable's position will be constrained.

@paramboundaryElement`any`

@returns`this`

### withParent

`this`

Sets the parent ref that the ref is nested in.

@paramparent`DragRef<unknown> | null`

@returns`this`

### dispose

`void`

Removes the dragging functionality from the DOM element.

@returns`void`

### isDragging

`boolean`

Checks whether the element is currently being dragged.

@returns`boolean`

### reset

`void`

Resets a standalone drag item to its initial position.

@returns`void`

### resetToBoundary

`void`

Resets drag item to end of boundary element.

@returns`void`

### disableHandle

`void`

Sets a handle as disabled. While a handle is disabled, it'll capture and interrupt dragging.

@paramhandle`HTMLElement`

Handle element that should be disabled.

@returns`void`

### enableHandle

`void`

Enables a handle, if it has been disabled.

@paramhandle`HTMLElement`

Handle element to be enabled.

@returns`void`

### withDirection

`this`

Sets the layout direction of the draggable item.

@paramdirection`Direction`

@returns`this`

### getFreeDragPosition

`Readonly<Point>`

Gets the current position in pixels the draggable outside of a drop container.

@returns`Readonly<Point>`

### setFreeDragPosition

`this`

Sets the current position in pixels the draggable outside of a drop container.

@paramvalue`Point`

New position to be set.

@returns`this`

### withPreviewContainer

`this`

Sets the container into which to insert the preview element.

@paramvalue`any`

Container into which to insert the preview.

@returns`this`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/DragRef>
