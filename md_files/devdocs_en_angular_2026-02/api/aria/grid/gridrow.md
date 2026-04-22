# GridRow

GridRow



# GridRow

Represents a row within a grid. It is a container for `ngGridCell` directives.

## API

```
class GridRow {
  readonly element: HTMLElement;
  readonly @Input() rowIndex: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### rowIndex

`any`

The index of this row within the grid.

## Description

Represents a row within a grid. It is a container for `ngGridCell` directives.

```
<tr ngGridRow>
  <!-- ... cells ... -->
</tr>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/grid/GridRow>
