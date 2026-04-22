# MenuItem

MenuItem



# MenuItem

An item in a Menu.

## API

```
class MenuItem<V> {
  readonly element: HTMLElement;
  readonly @Input() id: any;
  readonly @Input() value: any;
  readonly @Input() disabled: any;
  readonly @Input() @Output('searchTermChange') searchTerm: any;
  readonly parent: any;
  readonly @Input() submenu: any;
  readonly active: any;
  readonly expanded: any;
  readonly hasPopup: any;
  open(): void;
  close(): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### id

`any`

The unique ID of the menu item.

### value

`any`

The value of the menu item.

### disabled

`any`

Whether the menu item is disabled.

### searchTerm

`any`

The search term associated with the menu item.

### parent

`any`

A reference to the parent menu or menubar.

### submenu

`any`

The submenu associated with the menu item.

### active

`any`

Whether the menu item is active.

### expanded

`any`

Whether the menu is expanded.

### hasPopup

`any`

Whether the menu item has a popup.

### open

`void`

Opens the submenu focusing on the first menu item.

@returns`void`

### close

`void`

Closes the submenu.

@returns`void`

## Description

An item in a Menu.

`ngMenuItem` directives can be used in `ngMenu` and `ngMenuBar` to represent a choice or action a user can take. They can also act as triggers for sub-menus.

```
<div ngMenuItem (onSelect)="doAction()">Action Item</div>

<div ngMenuItem [submenu]="anotherMenu">Submenu Trigger</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/menu/MenuItem>
