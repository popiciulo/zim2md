# TabPanel

TabPanel



# TabPanel

A TabPanel container for the resources of layered content associated with a tab.

## API

```
class TabPanel implements OnInit ,OnDestroy {
  readonly element: HTMLElement;
  readonly id: any;
  readonly value: any;
  readonly visible: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### id

`any`

A global unique identifier for the tab.

### value

`any`

A local unique identifier for the tabpanel.

### visible

`any`

Whether the tab panel is visible.

### ngOnInit

`void`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

## Description

A TabPanel container for the resources of layered content associated with a tab.

The `ngTabPanel` directive holds the content for a specific tab. It is linked to an `ngTab` by a matching `value`. If a tab panel is hidden, the `inert` attribute will be applied to remove it from the accessibility tree. Proper styling is required for visual hiding.

```
<div ngTabPanel value="myTabId">
  <ng-template ngTabContent>
    <!-- Content for the tab panel -->
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tabs/TabPanel>
