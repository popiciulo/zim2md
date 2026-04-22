# CdkDrag

CdkDrag



# CdkDrag

Element that can be moved inside a CdkDropList container.

## API

```
class CdkDrag<T = any> implements AfterViewInit ,OnChanges ,OnDestroy {
  element: any;
  dropContainer: any;
  data: T;
  lockAxis: DragAxis | null;
  rootElementSelector: string;
  boundaryElement: any;
  dragStartDelay: DragStartDelay;
  freeDragPosition: Point;
   get disabled(): boolean;
  constrainPosition?: DragConstrainPosition | undefined;
  previewClass: string | string[];
  previewContainer: any;
  scale: number;
  readonly started: EventEmitter<CdkDragStart<any>>;
  readonly released: EventEmitter<CdkDragRelease<any>>;
  readonly ended: EventEmitter<CdkDragEnd<any>>;
  readonly entered: EventEmitter<CdkDragEnter<any, any>>;
  readonly exited: EventEmitter<CdkDragExit<any, any>>;
  readonly dropped: EventEmitter<CdkDragDrop<any, any, any>>;
  readonly moved: Observable<CdkDragMove<T>>;
  getPlaceholderElement(): HTMLElement;
  getRootElement(): HTMLElement;
  reset(): void;
  resetToBoundary(): void;
  getFreeDragPosition(): Readonly<Point>;
  setFreeDragPosition(value: Point): void;
}
```

### element

`any`

### dropContainer

`any`

### data

`T`

Arbitrary data to attach to this drag instance.

### lockAxis

`DragAxis | null`

Locks the position of the dragged element along the specified axis.

### rootElementSelector

`string`

Selector that will be used to determine the root draggable element, starting from the `cdkDrag` element and going up the DOM. Passing an alternate root element is useful when trying to enable dragging on an element that you might not have access to.

### boundaryElement

`any`

Node or selector that will be used to determine the element to which the draggable's position will be constrained. If a string is passed in, it'll be used as a selector that will be matched starting from the element's parent and going up the DOM until a match has been found.

### dragStartDelay

`DragStartDelay`

Amount of milliseconds to wait after the user has put their pointer down before starting to drag the element.

### freeDragPosition

`Point`

Sets the position of a [`CdkDrag`](cdkdrag) that is outside of a drop container. Can be used to restore the element's position for a returning user.

### disabled

`boolean`

Whether starting to drag this element is disabled.

### disabled

`boolean`

### constrainPosition

`DragConstrainPosition | undefined`

Function that can be used to customize the logic of how the position of the drag item is limited while it's being dragged. Gets called with a point containing the current position of the user's pointer on the page, a reference to the item being dragged and its dimensions. Should return a point describing where the item should be rendered.

### previewClass

`string | string[]`

Class to be added to the preview element.

### previewContainer

`any`

Configures the place into which the preview of the item will be inserted. Can be configured globally through [`CDK_DROP_LIST`](cdk_drop_list). Possible values:

- `global` - Preview will be inserted at the bottom of the `<body>`. The advantage is that you don't have to worry about `overflow: hidden` or `z-index`, but the item won't retain its inherited styles.
- `parent` - Preview will be inserted into the parent of the drag item. The advantage is that inherited styles will be preserved, but it may be clipped by `overflow: hidden` or not be visible due to `z-index`. Furthermore, the preview is going to have an effect over selectors like `:nth-child` and some flexbox configurations.
- `ElementRef<HTMLElement> | HTMLElement` - Preview will be inserted into a specific element. Same advantages and disadvantages as `parent`.

### scale

`number`

If the parent of the dragged element has a `scale` transform, it can throw off the positioning when the user starts dragging. Use this input to notify the CDK of the scale.

### started

`EventEmitter<CdkDragStart<any>>`

Emits when the user starts dragging the item.

### released

`EventEmitter<CdkDragRelease<any>>`

Emits when the user has released a drag item, before any animations have started.

### ended

`EventEmitter<CdkDragEnd<any>>`

Emits when the user stops dragging an item in the container.

### entered

`EventEmitter<CdkDragEnter<any, any>>`

Emits when the user has moved the item into a new container.

### exited

`EventEmitter<CdkDragExit<any, any>>`

Emits when the user removes the item its container by dragging it into another container.

### dropped

`EventEmitter<CdkDragDrop<any, any, any>>`

Emits when the user drops the item inside a container.

### moved

`Observable<CdkDragMove<T>>`

Emits as the user is dragging the item. Use with caution, because this event will fire for every pixel that the user has dragged.

### getPlaceholderElement

`HTMLElement`

Returns the element that is being used as a placeholder while the current element is being dragged.

@returns`HTMLElement`

### getRootElement

`HTMLElement`

Returns the root draggable element.

@returns`HTMLElement`

### reset

`void`

Resets a standalone drag item to its initial position.

@returns`void`

### resetToBoundary

`void`

Resets drag item to end of boundary element.

@returns`void`

### getFreeDragPosition

`Readonly<Point>`

Gets the pixel coordinates of the draggable outside of a drop container.

@returns`Readonly<Point>`

### setFreeDragPosition

`void`

Sets the current position in pixels the draggable outside of a drop container.

@paramvalue`Point`

New position to be set.

@returns`void`

### ngAfterViewInit

`void`

@returns`void`

### ngOnChanges

`void`

@paramchanges`SimpleChanges`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDrag>
