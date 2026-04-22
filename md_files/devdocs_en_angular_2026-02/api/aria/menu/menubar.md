# MenuBar

MenuBar



# MenuBar

A menu bar of menu items.

## API

```
class MenuBar<V> {
  readonly element: HTMLElement;
  readonly @Input() disabled: any;
  readonly @Input() softDisabled: any;
  readonly textDirection: any;
  readonly @Input() @Output('valuesChange') values: any;
  readonly @Input() wrap: any;
  readonly @Input() typeaheadDelay: any;
  @Output() onSelect: any;
  close(): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### disabled

`any`

Whether the menubar is disabled.

### softDisabled

`any`

Whether the menubar is soft disabled.

### textDirection

`any`

The directionality (LTR / RTL) context for the application (or a subtree of it).

### values

`any`

The values of the currently selected menu items.

### wrap

`any`

Whether the menu should wrap its items.

### typeaheadDelay

`any`

The delay in milliseconds before the typeahead buffer is cleared.

### onSelect

`any`

A callback function triggered when a menu item is selected.

### close

`void`

Closes the menubar.

@returns`void`

## Description

A menu bar of menu items.

Like the `ngMenu`, a `ngMenuBar` is used to offer a list of menu item choices to users. However, a menubar is used to display a persistent, top-level, always-visible set of menu item choices, typically found at the top of an application window.

```
<div ngMenuBar>
  <button ngMenuTrigger [menu]="fileMenu">File</button>
  <button ngMenuTrigger [menu]="editMenu">Edit</button>
</div>

<div ngMenu #fileMenu="ngMenu">
  <div ngMenuItem>New</div>
  <div ngMenuItem>Open</div>
</div>

<div ngMenu #editMenu="ngMenu">
  <div ngMenuItem>Cut</div>
  <div ngMenuItem>Copy</div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/menu/MenuBar>
