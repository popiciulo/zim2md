# CdkDropList

CdkDropList



# CdkDropList

Container that wraps a set of draggable items.

## API

```
class CdkDropList<T = any> implements OnDestroy {
  element: any;
  connectedTo: string | CdkDropList<any> | (string | CdkDropList<any>)[];
  data: T;
  orientation: DropListOrientation;
  id: string;
  lockAxis: DragAxis | null;
   get disabled(): boolean;
  sortingDisabled: boolean;
  enterPredicate: (drag: CdkDrag<any>, drop: CdkDropList<any>) => boolean;
  sortPredicate: (index: number, drag: CdkDrag<any>, drop: CdkDropList<any>) => boolean;
  autoScrollDisabled: boolean;
  autoScrollStep: NumberInput;
  elementContainerSelector: string | null;
  hasAnchor: boolean;
  readonly dropped: EventEmitter<CdkDragDrop<T, any, any>>;
  readonly entered: EventEmitter<CdkDragEnter<T, T>>;
  readonly exited: EventEmitter<CdkDragExit<T, T>>;
  readonly sorted: EventEmitter<CdkDragSortEvent<T, T>>;
  addItem(item: CdkDrag<any>): void;
  removeItem(item: CdkDrag<any>): void;
  getSortedItems(): CdkDrag<any>[];
}
```

### element

`any`

### connectedTo

`string | CdkDropList<any> | (string | CdkDropList<any>)[]`

Other draggable containers that this container is connected to and into which the container's items can be transferred. Can either be references to other drop containers, or their unique IDs.

### data

`T`

Arbitrary data to attach to this container.

### orientation

`DropListOrientation`

Direction in which the list is oriented.

### id

`string`

Unique ID for the drop zone. Can be used as a reference in the `connectedTo` of another [`CdkDropList`](cdkdroplist).

### lockAxis

`DragAxis | null`

Locks the position of the draggable elements inside the container along the specified axis.

### disabled

`boolean`

Whether starting a dragging sequence from this container is disabled.

### disabled

`boolean`

### sortingDisabled

`boolean`

Whether sorting within this drop list is disabled.

### enterPredicate

`(drag: CdkDrag<any>, drop: CdkDropList<any>) => boolean`

Function that is used to determine whether an item is allowed to be moved into a drop container.

### sortPredicate

`(index: number, drag: CdkDrag<any>, drop: CdkDropList<any>) => boolean`

Functions that is used to determine whether an item can be sorted into a particular index.

### autoScrollDisabled

`boolean`

Whether to auto-scroll the view when the user moves their pointer close to the edges.

### autoScrollStep

`NumberInput`

Number of pixels to scroll for each frame when auto-scrolling an element.

### elementContainerSelector

`string | null`

Selector that will be used to resolve an alternate element container for the drop list. Passing an alternate container is useful for the cases where one might not have control over the parent node of the draggable items within the list (e.g. due to content projection). This allows for usages like:

```
<div cdkDropList cdkDropListElementContainer=".inner">
  <div class="inner">
    <div cdkDrag></div>
  </div>
</div>
```

### hasAnchor

`boolean`

By default when an item leaves its initial container, its placeholder will be transferred to the new container. If that's not desirable for your use case, you can enable this option which will clone the placeholder and leave it inside the original container. If the item is returned to the initial container, the anchor element will be removed automatically.

The cloned placeholder can be styled by targeting the `cdk-drag-anchor` class.

This option is useful in combination with `cdkDropListSortingDisabled` to implement copying behavior in a drop list.

### dropped

`EventEmitter<CdkDragDrop<T, any, any>>`

Emits when the user drops an item inside the container.

### entered

`EventEmitter<CdkDragEnter<T, T>>`

Emits when the user has moved a new drag item into this container.

### exited

`EventEmitter<CdkDragExit<T, T>>`

Emits when the user removes an item from the container by dragging it into another container.

### sorted

`EventEmitter<CdkDragSortEvent<T, T>>`

Emits as the user is swapping items while actively dragging.

### addItem

`void`

Registers an items with the drop list.

@paramitem`CdkDrag<any>`

@returns`void`

### removeItem

`void`

Removes an item from the drop list.

@paramitem`CdkDrag<any>`

@returns`void`

### getSortedItems

`CdkDrag<any>[]`

Gets the registered items in the list, sorted by their position in the DOM.

@returns`CdkDrag<any>[]`

### ngOnDestroy

`void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDropList>
