# CdkDragExit

CdkDragExit



# CdkDragExit

Event emitted when the user removes an item from a drop container by moving it into another one.

## API

```
interface CdkDragExit<T = any, I = T> {
  container: CdkDropList<T>;
  item: CdkDrag<I>;
}
```

### container

`CdkDropList<T>`

Container from which the user has a removed an item.

### item

`CdkDrag<I>`

Item that was removed from the container.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragExit>
