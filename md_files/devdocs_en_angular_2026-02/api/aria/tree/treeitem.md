# TreeItem

TreeItem



# TreeItem

A selectable and expandable item in an `ngTree`.

## API

```
class TreeItem<V> extends DeferredContentAware implements OnInit ,OnDestroy ,HasElement {
  readonly element: HTMLElement;
  readonly @Input() id: any;
  readonly @Input() value: any;
  readonly @Input() parent: any;
  readonly @Input() disabled: any;
  readonly @Input() selectable: any;
  readonly @Input() @Output('expandedChange') expanded: any;
  readonly @Input() label: any;
  readonly searchTerm: any;
  readonly tree: Signal<Tree<V>>;
  readonly active: any;
  readonly level: any;
  readonly selected: any;
  readonly visible: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### id

`any`

A unique identifier for the tree item.

### value

`any`

The value of the tree item.

### parent

`any`

The parent tree root or tree item group.

### disabled

`any`

Whether the tree item is disabled.

### selectable

`any`

Whether the tree item is selectable.

### expanded

`any`

Whether the tree item is expanded.

### label

`any`

Optional label for typeahead. Defaults to the element's textContent.

### searchTerm

`any`

Search term for typeahead.

### tree

`Signal<Tree<V>>`

The tree root.

### active

`any`

Whether the item is active.

### level

`any`

The level of the current item in a tree.

### selected

`any`

Whether the item is selected.

### visible

`any`

Whether this item is visible due to all of its parents being expanded.

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

## Description

A selectable and expandable item in an `ngTree`.

The `ngTreeItem` directive represents an individual node within an `ngTree`. It can be selected, expanded (if it has children), and disabled. The `parent` input establishes the hierarchical relationship within the tree.

```
<li ngTreeItem [parent]="parentTreeOrGroup" value="item-id" label="Item Label">
  Item Label
</li>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tree/TreeItem>
