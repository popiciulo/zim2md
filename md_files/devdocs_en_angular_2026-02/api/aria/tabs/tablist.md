# TabList

TabList



# TabList

A TabList container.

## API

```
class TabList implements OnInit ,OnDestroy {
  readonly element: HTMLElement;
  readonly textDirection: any;
  readonly @Input() orientation: any;
  readonly @Input() wrap: any;
  readonly @Input() softDisabled: any;
  readonly @Input() focusMode: any;
  readonly @Input() selectionMode: any;
  readonly @Input() @Output('selectedTabChange') selectedTab: any;
  readonly @Input() disabled: any;
  open(value: string): boolean;
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

Whether the tablist is vertically or horizontally oriented.

### wrap

`any`

Whether focus should wrap when navigating.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### focusMode

`any`

The focus strategy used by the tablist.

- `roving`: Focus is moved to the active tab using `tabindex`.
- `activedescendant`: Focus remains on the tablist container, and `aria-activedescendant` is used to indicate the active tab.

### selectionMode

`any`

The selection strategy used by the tablist.

- `follow`: The focused tab is automatically selected.
- `explicit`: Tabs are selected explicitly by the user (e.g., via click or spacebar).

### selectedTab

`any`

The current selected tab.

### disabled

`any`

Whether the tablist is disabled.

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

### open

`boolean`

Opens the tab panel with the specified value.

@paramvalue`string`

@returns`boolean`

## Description

A TabList container.

The `ngTabList` directive controls a list of `ngTab` elements. It manages keyboard navigation, selection, and the overall orientation of the tabs. It should be placed within an `ngTabs` container.

```
<ul ngTabList [(selectedTab)]="mySelectedTab" orientation="horizontal" selectionMode="explicit">
  <li ngTab value="first">First Tab</li>
  <li ngTab value="second">Second Tab</li>
</ul>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tabs/TabList>
