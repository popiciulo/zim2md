# Menu

Menu



# Menu

A list of menu items.

## API

```
class Menu<V> {
  readonly element: HTMLElement;
  readonly textDirection: any;
  readonly id: any;
  readonly wrap: any;
  readonly typeaheadDelay: any;
  readonly disabled: any;
  readonly parent: any;
  readonly visible: any;
  readonly tabIndex: any;
  onSelect: any;
  readonly expansionDelay: any;
  close(): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### textDirection

`any`

The directionality (LTR / RTL) context for the application (or a subtree of it).

### id

`any`

The unique ID of the menu.

### wrap

`any`

Whether the menu should wrap its items.

### typeaheadDelay

`any`

The delay in milliseconds before the typeahead buffer is cleared.

### disabled

`any`

Whether the menu is disabled.

### parent

`any`

A reference to the parent menu item or menu trigger.

### visible

`any`

Whether the menu is visible.

### tabIndex

`any`

The tab index of the menu.

### onSelect

`any`

A callback function triggered when a menu item is selected.

### expansionDelay

`any`

The delay in milliseconds before expanding sub-menus on hover.

### close

`void`

Closes the menu.

@returns`void`

## Description

A list of menu items.

A `ngMenu` is used to offer a list of menu item choices to users. Menus can be nested within other menus to create sub-menus. It works in conjunction with `ngMenuTrigger` and `ngMenuItem` directives.

```
<button ngMenuTrigger [menu]="myMenu">Options</button>

<div ngMenu #myMenu="ngMenu">
  <div ngMenuItem>Star</div>
  <div ngMenuItem>Edit</div>
  <div ngMenuItem [submenu]="subMenu">More</div>
</div>

<div ngMenu #subMenu="ngMenu">
  <div ngMenuItem>Sub Item 1</div>
  <div ngMenuItem>Sub Item 2</div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/menu/Menu>
