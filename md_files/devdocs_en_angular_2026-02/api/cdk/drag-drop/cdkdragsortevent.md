# CdkDragSortEvent

CdkDragSortEvent



# CdkDragSortEvent

Event emitted when the user swaps the position of two drag items.

## API

```
interface CdkDragSortEvent<T = any, I = T> {
  previousIndex: number;
  currentIndex: number;
  container: CdkDropList<T>;
  item: CdkDrag<I>;
}
```

### previousIndex

`number`

Index from which the item was sorted previously.

### currentIndex

`number`

Index that the item is currently in.

### container

`CdkDropList<T>`

Container that the item belongs to.

### item

`CdkDrag<I>`

Item that is being sorted.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragSortEvent>
