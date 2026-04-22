# MenuTrigger

MenuTrigger



# MenuTrigger

A trigger for a menu.

## API

```
class MenuTrigger<V> {
  readonly element: HTMLElement;
  readonly textDirection: any;
  @Input() menu: any;
  readonly expanded: any;
  readonly hasPopup: any;
  readonly @Input() disabled: any;
  readonly @Input() softDisabled: any;
  open(): void;
  close(): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### textDirection

`any`

The directionality (LTR / RTL) context for the application (or a subtree of it).

### menu

`any`

The menu associated with the trigger.

### expanded

`any`

Whether the menu is expanded.

### hasPopup

`any`

Whether the menu trigger has a popup.

### disabled

`any`

Whether the menu trigger is disabled.

### softDisabled

`any`

Whether the menu trigger is soft disabled.

### open

`void`

Opens the menu focusing on the first menu item.

@returns`void`

### close

`void`

Closes the menu.

@returns`void`

## Description

A trigger for a menu.

The `ngMenuTrigger` directive is used to open and close menus. It can be applied to any interactive element (e.g., a button) to associate it with a `ngMenu` instance. It also supports linking to sub-menus when applied to a `ngMenuItem`.

```
<button ngMenuTrigger [menu]="myMenu">Open Menu</button>

<div ngMenu #myMenu="ngMenu">
  <div ngMenuItem>Item 1</div>
  <div ngMenuItem>Item 2</div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/menu/MenuTrigger>
