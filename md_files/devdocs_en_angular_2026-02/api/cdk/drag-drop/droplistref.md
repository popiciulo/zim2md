# DropListRef

DropListRef



# DropListRef

Reference to a drop list. Used to manipulate or dispose of the container.

## API

```
class DropListRef<T = any> {
  constructor(element: any, _dragDropRegistry: DragDropRegistry, _document: any, _ngZone: NgZone, _viewportRuler: ViewportRuler): DropListRef<T>;
  element: any;
  disabled: boolean;
  sortingDisabled: boolean;
  lockAxis: "x" | "y" | null;
  autoScrollDisabled: boolean;
  autoScrollStep: number;
  hasAnchor: boolean;
  enterPredicate: (drag: DragRef<any>, drop: DropListRef<any>) => boolean;
  sortPredicate: (index: number, drag: DragRef<any>, drop: DropListRef<any>) => boolean;
  readonly beforeStarted: any;
  readonly entered: any;
  readonly exited: any;
  readonly dropped: any;
  readonly sorted: any;
  readonly receivingStarted: any;
  readonly receivingStopped: any;
  data: T;
  dispose(): void;
  isDragging(): boolean;
  start(): void;
  enter(item: DragRef<any>, pointerX: number, pointerY: number, index?: number | undefined): void;
  exit(item: DragRef<any>): void;
  drop(item: DragRef<any>, currentIndex: number, previousIndex: number, previousContainer: DropListRef<any>, isPointerOverContainer: boolean, distance: Point, dropPoint: Point, event?: MouseEvent | TouchEvent): void;
  withItems(items: DragRef<any>[]): this;
  withDirection(direction: Direction): this;
  connectedTo(connectedTo: DropListRef<any>[]): this;
  withOrientation(orientation: DropListOrientation): this;
  withScrollableParents(elements: HTMLElement[]): this;
  withElementContainer(container: HTMLElement): this;
  getScrollableParents(): readonly HTMLElement[];
  getItemIndex(item: DragRef<any>): number;
  getItemAtIndex(index: number): DragRef<any> | null;
  isReceiving(): boolean;
}
```

### constructor

`DropListRef<T>`

@paramelement`any`

@param\_dragDropRegistry`DragDropRegistry`

@param\_document`any`

@param\_ngZone`NgZone`

@param\_viewportRuler`ViewportRuler`

@returns`DropListRef<T>`

### element

`any`

Element that the drop list is attached to.

### disabled

`boolean`

Whether starting a dragging sequence from this container is disabled.

### sortingDisabled

`boolean`

Whether sorting items within the list is disabled.

### lockAxis

`"x" | "y" | null`

Locks the position of the draggable elements inside the container along the specified axis.

### autoScrollDisabled

`boolean`

Whether auto-scrolling the view when the user moves their pointer close to the edges is disabled.

### autoScrollStep

`number`

Number of pixels to scroll for each frame when auto-scrolling an element.

### hasAnchor

`boolean`

Whether the items in the list should leave an anchor node when leaving the initial container.

### enterPredicate

`(drag: DragRef<any>, drop: DropListRef<any>) => boolean`

Function that is used to determine whether an item is allowed to be moved into a drop container.

### sortPredicate

`(index: number, drag: DragRef<any>, drop: DropListRef<any>) => boolean`

Function that is used to determine whether an item can be sorted into a particular index.

### beforeStarted

`any`

Emits right before dragging has started.

### entered

`any`

Emits when the user has moved a new drag item into this container.

### exited

`any`

Emits when the user removes an item from the container by dragging it into another container.

### dropped

`any`

Emits when the user drops an item inside the container.

### sorted

`any`

Emits as the user is swapping items while actively dragging.

### receivingStarted

`any`

Emits when a dragging sequence is started in a list connected to the current one.

### receivingStopped

`any`

Emits when a dragging sequence is stopped from a list connected to the current one.

### data

`T`

Arbitrary data that can be attached to the drop list.

### dispose

`void`

Removes the drop list functionality from the DOM element.

@returns`void`

### isDragging

`boolean`

Whether an item from this list is currently being dragged.

@returns`boolean`

### start

`void`

Starts dragging an item.

@returns`void`

### enter

`void`

Attempts to move an item into the container.

@paramitem`DragRef<any>`

Item that was moved into the container.

@parampointerX`number`

Position of the item along the X axis.

@parampointerY`number`

Position of the item along the Y axis.

@paramindex`number | undefined`

Index at which the item entered. If omitted, the container will try to figure it out automatically.

@returns`void`

### exit

`void`

Removes an item from the container after it was dragged into another container by the user.

@paramitem`DragRef<any>`

Item that was dragged out.

@returns`void`

### drop

`void`

Drops an item into this container.

@paramitem`DragRef<any>`

Item being dropped into the container.

@paramcurrentIndex`number`

Index at which the item should be inserted.

@parampreviousIndex`number`

Index of the item when dragging started.

@parampreviousContainer`DropListRef<any>`

Container from which the item got dragged in.

@paramisPointerOverContainer`boolean`

Whether the user's pointer was over the container when the item was dropped.

@paramdistance`Point`

Distance the user has dragged since the start of the dragging sequence.

@paramdropPoint`Point`

@paramevent`MouseEvent | TouchEvent`

Event that triggered the dropping sequence.

@returns`void`

### withItems

`this`

Sets the draggable items that are a part of this list.

@paramitems`DragRef<any>[]`

Items that are a part of this list.

@returns`this`

### withDirection

`this`

Sets the layout direction of the drop list.

@paramdirection`Direction`

@returns`this`

### connectedTo

`this`

Sets the containers that are connected to this one. When two or more containers are connected, the user will be allowed to transfer items between them.

@paramconnectedTo`DropListRef<any>[]`

Other containers that the current containers should be connected to.

@returns`this`

### withOrientation

`this`

Sets the orientation of the container.

@paramorientation`DropListOrientation`

New orientation for the container.

@returns`this`

### withScrollableParents

`this`

Sets which parent elements are can be scrolled while the user is dragging.

@paramelements`HTMLElement[]`

Elements that can be scrolled.

@returns`this`

### withElementContainer

`this`

Configures the drop list so that a different element is used as the container for the dragged items. This is useful for the cases when one might not have control over the full DOM that sets up the dragging. Note that the alternate container needs to be a descendant of the drop list.

@paramcontainer`HTMLElement`

New element container to be assigned.

@returns`this`

### getScrollableParents

`readonly HTMLElement[]`

Gets the scrollable parents that are registered with this drop container.

@returns`readonly HTMLElement[]`

### getItemIndex

`number`

Figures out the index of an item in the container.

@paramitem`DragRef<any>`

Item whose index should be determined.

@returns`number`

### getItemAtIndex

`DragRef<any> | null`

Gets the item at a specific index.

@paramindex`number`

Index at which to retrieve the item.

@returns`DragRef<any> | null`

### isReceiving

`boolean`

Whether the list is able to receive the item that is currently being dragged inside a connected drop list.

@returns`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/DropListRef>
