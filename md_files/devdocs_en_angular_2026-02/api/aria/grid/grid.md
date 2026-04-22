# Grid

Grid



# Grid

The container for a grid. It provides keyboard navigation and focus management for the grid's rows and cells. It manages the overall behavior of the grid, including focus wrapping, selection, and disabled states.

## API

```
class Grid {
  readonly element: HTMLElement;
  readonly textDirection: any;
  readonly @Input() enableSelection: any;
  readonly @Input() disabled: any;
  readonly @Input() softDisabled: any;
  readonly @Input() focusMode: any;
  readonly @Input() rowWrap: any;
  readonly @Input() colWrap: any;
  readonly @Input() multi: any;
  readonly @Input() selectionMode: any;
  readonly @Input() enableRangeSelection: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### textDirection

`any`

Text direction.

### enableSelection

`any`

Whether selection is enabled for the grid.

### disabled

`any`

Whether the grid is disabled.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### focusMode

`any`

The focus strategy used by the grid.

- `roving`: Focus is moved to the active cell using `tabindex`.
- `activedescendant`: Focus remains on the grid container, and `aria-activedescendant` is used to indicate the active cell.

### rowWrap

`any`

The wrapping behavior for keyboard navigation along the row axis.

- `continuous`: Navigation wraps from the last row to the first, and vice-versa.
- `loop`: Navigation wraps within the current row.
- `nowrap`: Navigation stops at the first/last item in the row.

### colWrap

`any`

The wrapping behavior for keyboard navigation along the column axis.

- `continuous`: Navigation wraps from the last column to the first, and vice-versa.
- `loop`: Navigation wraps within the current column.
- `nowrap`: Navigation stops at the first/last item in the column.

### multi

`any`

Whether multiple cells in the grid can be selected.

### selectionMode

`any`

The selection strategy used by the grid.

- `follow`: The focused cell is automatically selected.
- `explicit`: Cells are selected explicitly by the user (e.g., via click or spacebar).

### enableRangeSelection

`any`

Whether enable range selections (with modifier keys or dragging).

## Description

The container for a grid. It provides keyboard navigation and focus management for the grid's rows and cells. It manages the overall behavior of the grid, including focus wrapping, selection, and disabled states.

```
<table ngGrid [multi]="true" [enableSelection]="true">
  @for (row of gridData; track row) {
    <tr ngGridRow>
      @for (cell of row; track cell) {
        <td ngGridCell [disabled]="cell.disabled">
          {{cell.value}}
        </td>
      }
    </tr>
  }
</table>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/grid/Grid>
