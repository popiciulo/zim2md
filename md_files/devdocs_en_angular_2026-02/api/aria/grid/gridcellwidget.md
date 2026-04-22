# GridCellWidget

GridCellWidget



# GridCellWidget

Represents an interactive element inside a [`GridCell`](gridcell). It allows for pausing grid navigation to interact with the widget.

## API

```
class GridCellWidget {
  readonly element: HTMLElement;
  readonly active: any;
  readonly @Input() id: any;
  readonly @Input() widgetType: any;
  readonly @Input() disabled: any;
  readonly @Input() focusTarget: any;
  readonly @Output() onActivate: any;
  readonly @Output() onDeactivate: any;
  readonly @Input() tabindex: any;
  readonly isActivated: Signal<boolean>;
  activate(): void;
  deactivate(): void;
}
```

### element

`HTMLElement`

A reference to the host element.

### active

`any`

Whether the widget is currently active (focused).

### id

`any`

A unique identifier for the widget.

### widgetType

`any`

The type of widget, which determines how it is activated.

### disabled

`any`

Whether the widget is disabled.

### focusTarget

`any`

The target that will receive focus instead of the widget.

### onActivate

`any`

Emits when the widget is activated.

### onDeactivate

`any`

Emits when the widget is deactivated.

### tabindex

`any`

The tabindex override.

### isActivated

`Signal<boolean>`

Whether the widget is activated.

### activate

`void`

Activates the widget.

@returns`void`

### deactivate

`void`

Deactivates the widget.

@returns`void`

## Description

Represents an interactive element inside a [`GridCell`](gridcell). It allows for pausing grid navigation to interact with the widget.

When the user interacts with the widget (e.g., by typing in an input or opening a menu), grid navigation is temporarily suspended to allow the widget to handle keyboard events.

```
<td ngGridCell>
  <button ngGridCellWidget>Click Me</button>
</td>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/grid/GridCellWidget>
