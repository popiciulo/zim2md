# Tab

Tab



# Tab

A selectable tab in a TabList.

## API

```
class Tab implements HasElement ,OnInit ,OnDestroy {
  readonly element: HTMLElement;
  readonly @Input() id: any;
  readonly @Input() disabled: any;
  readonly @Input() value: any;
  readonly active: any;
  readonly selected: any;
  open(): void;
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

Whether a tab is disabled.

### value

`any`

The remote tabpanel unique identifier.

### active

`any`

Whether the tab is active.

### selected

`any`

Whether the tab is selected.

### open

`void`

Opens this tab panel.

@returns`void`

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

## Description

A selectable tab in a TabList.

The `ngTab` directive represents an individual tab control within an `ngTabList`. It requires a `value` that uniquely identifies it and links it to a corresponding `ngTabPanel`.

```
<li ngTab value="myTabId" [disabled]="isTabDisabled">
  My Tab Label
</li>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tabs/Tab>
