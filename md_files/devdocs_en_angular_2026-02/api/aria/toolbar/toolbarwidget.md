# ToolbarWidget

ToolbarWidget



# ToolbarWidget

A widget within a toolbar.

## API

```
class ToolbarWidget<V> implements OnInit ,OnDestroy {
  readonly element: HTMLElement;
  readonly @Input() id: any;
  readonly @Input() disabled: any;
  readonly hardDisabled: any;
  readonly @Input() value: any;
  readonly active: any;
  readonly selected: () => any;
}
```

### element

`HTMLElement`

A reference to the host element.

### id

`any`

A unique identifier for the widget.

### disabled

`any`

Whether the widget is disabled.

### hardDisabled

`any`

Whether the widget is 'hard' disabled, which is different from `aria-disabled`. A hard disabled widget cannot receive focus.

### value

`any`

The value associated with the widget.

### active

`any`

Whether the widget is currently active (focused).

### selected

`() => any`

Whether the widget is selected (only relevant in a selection group).

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

## Description

A widget within a toolbar.

The `ngToolbarWidget` directive should be applied to any native HTML element that acts as an interactive widget within an `ngToolbar` or `ngToolbarWidgetGroup`. It enables keyboard navigation and selection within the toolbar.

```
<button ngToolbarWidget value="action-id" [disabled]="isDisabled">
  Perform Action
</button>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/toolbar/ToolbarWidget>
