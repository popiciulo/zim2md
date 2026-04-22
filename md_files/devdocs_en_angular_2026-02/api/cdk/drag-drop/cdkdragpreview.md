# CdkDragPreview

CdkDragPreview



# CdkDragPreview

Element that will be used as a template for the preview of a CdkDrag when it is being dragged.

## API

```
class CdkDragPreview<T = any> implements OnDestroy {
  templateRef: any;
  data: T;
  matchSize: boolean;
}
```

### templateRef

`any`

### data

`T`

Context data to be added to the preview template instance.

### matchSize

`boolean`

Whether the preview should preserve the same size as the item that is being dragged.

### ngOnDestroy

`void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/CdkDragPreview>
