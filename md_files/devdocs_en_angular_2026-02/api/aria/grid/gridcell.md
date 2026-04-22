# GridCell

GridCell



# GridCell

Represents a cell within a grid row. It is the primary focusable element within the grid. It can be disabled and can have its selection state managed through the `selected` input.

## API

```
class GridCell {
  readonly element: HTMLElement;
  readonly active: any;
  readonly textDirection: any;
  readonly @Input() id: any;
  readonly @Input() role: any;
  readonly @Input() rowSpan: any;
  readonly @Input() colSpan: any;
  readonly @Input() rowIndex: any;
  readonly @Input() colIndex: any;
  readonly @Input() disabled: any;
  readonly @Input() @Output('selectedChange') selected: any;
  readonly @Input() selectable: any;
  readonly @Input() orientation: any;
  readonly @Input() wrap: any;
  readonly @Input() tabindex: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### active

`any`

Whether the cell is currently active (focused).

### textDirection

`any`

Text direction.

### id

`any`

A unique identifier for the cell.

### role

`any`

The ARIA role for the cell.

### rowSpan

`any`

The number of rows the cell should span.

### colSpan

`any`

The number of columns the cell should span.

### rowIndex

`any`

The index of this cell's row within the grid.

### colIndex

`any`

The index of this cell's column within the grid.

### disabled

`any`

Whether the cell is disabled.

### selected

`any`

Whether the cell is selected.

### selectable

`any`

Whether the cell is selectable.

### orientation

`any`

Orientation of the widgets in the cell.

### wrap

`any`

Whether widgets navigation wraps.

### tabindex

`any`

The tabindex override.

## Description

Represents a cell within a grid row. It is the primary focusable element within the grid. It can be disabled and can have its selection state managed through the `selected` input.

```
<td ngGridCell [disabled]="isDisabled" [(selected)]="isSelected">
  Cell Content
</td>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/grid/GridCell>
