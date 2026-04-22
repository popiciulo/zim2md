# ToolbarWidgetGroup

ToolbarWidgetGroup



# ToolbarWidgetGroup

A directive that groups toolbar widgets, used for more complex widgets like radio groups that have their own internal navigation.

## API

```
class ToolbarWidgetGroup<V> {
  readonly element: HTMLElement;
  readonly @Input() disabled: any;
  readonly @Input() multi: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### disabled

`any`

Whether the widget group is disabled.

### multi

`any`

Whether the group allows multiple widgets to be selected.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/toolbar/ToolbarWidgetGroup>
