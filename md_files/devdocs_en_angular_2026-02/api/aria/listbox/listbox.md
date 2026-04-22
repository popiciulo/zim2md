# Listbox

Listbox



# Listbox

Represents a container used to display a list of items for a user to select from.

## API

```
class Listbox<V> {
  readonly id: any;
  readonly element: HTMLElement;
  protected textDirection: any;
  protected items: any;
  orientation: any;
  multi: any;
  wrap: any;
  softDisabled: any;
  focusMode: any;
  selectionMode: any;
  typeaheadDelay: any;
  disabled: any;
  readonly: any;
  values: any;
  scrollActiveItemIntoView(options?: ScrollIntoViewOptions): void;
  gotoFirst(): void;
}
```

### id

`any`

A unique identifier for the listbox.

### element

`HTMLElement`

A reference to the host element.

### textDirection

`any`

A signal wrapper for directionality.

### items

`any`

The Option UIPatterns of the child Options.

### orientation

`any`

Whether the list is vertically or horizontally oriented.

### multi

`any`

Whether multiple items in the list can be selected at once.

### wrap

`any`

Whether focus should wrap when navigating.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### focusMode

`any`

The focus strategy used by the list.

- `roving`: Focus is moved to the active item using `tabindex`.
- `activedescendant`: Focus remains on the listbox container, and `aria-activedescendant` is used to indicate the active item.

### selectionMode

`any`

The selection strategy used by the list.

- `follow`: The focused item is automatically selected.
- `explicit`: Items are selected explicitly by the user (e.g., via click or spacebar).

### typeaheadDelay

`any`

The amount of time before the typeahead search is reset.

### disabled

`any`

Whether the listbox is disabled.

### readonly

`any`

Whether the listbox is readonly.

### values

`any`

The values of the currently selected items.

### scrollActiveItemIntoView

`void`

@paramoptions`ScrollIntoViewOptions`

@returns`void`

### gotoFirst

`void`

Navigates to the first item in the listbox.

@returns`void`

## Description

Represents a container used to display a list of items for a user to select from.

The `ngListbox` is meant to be used in conjunction with `ngOption` directives to create a selectable list. It supports single and multiple selection modes, as well as various focus and orientation strategies.

```
<ul ngListbox [(value)]="selectedItems" [multi]="true" orientation="vertical">
  @for (item of items; track item.id) {
    <li ngOption [value]="item.id" [label]="item.name" [disabled]="item.disabled">
      {{item.name}}
    </li>
  }
</ul>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/listbox/Listbox>
