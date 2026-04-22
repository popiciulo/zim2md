# Toolbar

Toolbar



# Toolbar

A toolbar widget container for a group of interactive widgets, such as buttons or radio groups. It provides a single point of reference for keyboard navigation and focus management. It supports various orientations and disabled states.

## API

```
class Toolbar<V> {
  readonly element: HTMLElement;
  readonly textDirection: any;
  readonly @Input() orientation: any;
  @Input() softDisabled: any;
  readonly @Input() disabled: any;
  readonly @Input() wrap: any;
  readonly @Input() @Output('valuesChange') values: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### textDirection

`any`

Text direction.

### orientation

`any`

Whether the toolbar is vertically or horizontally oriented.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### disabled

`any`

Whether the toolbar is disabled.

### wrap

`any`

Whether focus should wrap when navigating.

### values

`any`

The values of the selected widgets within the toolbar.

## Description

A toolbar widget container for a group of interactive widgets, such as buttons or radio groups. It provides a single point of reference for keyboard navigation and focus management. It supports various orientations and disabled states.

```
<div ngToolbar orientation="horizontal" [wrap]="true">
  <button ngToolbarWidget value="save">Save</button>
  <button ngToolbarWidget value="print">Print</button>

  <div ngToolbarWidgetGroup [(value)]="selectedAlignment">
    <button ngToolbarWidget value="left">Left</button>
    <button ngToolbarWidget value="center">Center</button>
    <button ngToolbarWidget value="right">Right</button>
  </div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/toolbar/Toolbar>
