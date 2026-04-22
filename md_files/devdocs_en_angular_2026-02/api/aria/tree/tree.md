# Tree

Tree



# Tree

A container that transforms nested lists into an accessible, ARIA-compliant tree structure. It manages the overall state of the tree, including selection, expansion, and keyboard navigation.

## API

```
class Tree<V> {
  readonly element: HTMLElement;
  readonly id: any;
  readonly orientation: any;
  readonly multi: any;
  readonly disabled: any;
  readonly selectionMode: any;
  readonly focusMode: any;
  readonly wrap: any;
  readonly softDisabled: any;
  readonly typeaheadDelay: any;
  readonly values: any;
  readonly textDirection: any;
  readonly nav: any;
  readonly currentType: any;
  scrollActiveItemIntoView(options?: ScrollIntoViewOptions): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### id

`any`

A unique identifier for the tree.

### orientation

`any`

Orientation of the tree.

### multi

`any`

Whether multi-selection is allowed.

### disabled

`any`

Whether the tree is disabled.

### selectionMode

`any`

The selection strategy used by the tree.

- `explicit`: Items are selected explicitly by the user (e.g., via click or spacebar).
- `follow`: The focused item is automatically selected.

### focusMode

`any`

The focus strategy used by the tree.

- `roving`: Focus is moved to the active item using `tabindex`.
- `activedescendant`: Focus remains on the tree container, and `aria-activedescendant` is used to indicate the active item.

### wrap

`any`

Whether navigation wraps.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### typeaheadDelay

`any`

The delay in seconds before the typeahead search is reset.

### values

`any`

The values of the currently selected items.

### textDirection

`any`

Text direction.

### nav

`any`

Whether the tree is in navigation mode.

### currentType

`any`

The `aria-current` type. It can be used in navigation trees to indicate the currently active item. See <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current> for more details.

### scrollActiveItemIntoView

`void`

@paramoptions`ScrollIntoViewOptions`

@returns`void`

## Description

A container that transforms nested lists into an accessible, ARIA-compliant tree structure. It manages the overall state of the tree, including selection, expansion, and keyboard navigation.

```
<ul ngTree [(value)]="selectedItems" [multi]="true">
  <ng-template
    [ngTemplateOutlet]="treeNodes"
    [ngTemplateOutletContext]="{nodes: treeData, parent: tree}"
  />
</ul>

<ng-template #treeNodes let-nodes="nodes" let-parent="parent">
  @for (node of nodes; track node.name) {
    <li ngTreeItem [parent]="parent" [value]="node.name" [label]="node.name">
      {{ node.name }}
      @if (node.children) {
        <ul role="group">
          <ng-template ngTreeItemGroup [ownedBy]="treeItem" #group="ngTreeItemGroup">
            <ng-template
              [ngTemplateOutlet]="treeNodes"
              [ngTemplateOutletContext]="{nodes: node.children, parent: group}"
            />
          </ng-template>
        </ul>
      }
    </li>
  }
</ng-template>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tree/Tree>
