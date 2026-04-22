# TreeItemGroup

TreeItemGroup



# TreeItemGroup

Group that contains children tree items.

## API

```
class TreeItemGroup<V> implements OnInit ,OnDestroy {
  readonly element: HTMLElement;
  readonly ownedBy: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### ownedBy

`any`

Tree item that owns the group.

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

## Description

Group that contains children tree items.

The `ngTreeItemGroup` structural directive should be applied to an `ng-template` that wraps the child `ngTreeItem` elements. It is used to define a group of children for an expandable `ngTreeItem`. The `ownedBy` input links the group to its parent `ngTreeItem`.

```
<li ngTreeItem [value]="'parent-id'">
  Parent Item
  <ul role="group">
    <ng-template ngTreeItemGroup [ownedBy]="parentTreeItemRef">
      <li ngTreeItem [value]="'child-id'">Child Item</li>
    </ng-template>
  </ul>
</li>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tree/TreeItemGroup>
