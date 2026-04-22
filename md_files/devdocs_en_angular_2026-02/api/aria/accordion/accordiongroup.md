# AccordionGroup

AccordionGroup



# AccordionGroup

A container for a group of accordion items. It manages the overall state and interactions of the accordion, such as keyboard navigation and expansion mode.

## API

```
class AccordionGroup {
  readonly element: HTMLElement;
  readonly textDirection: any;
  readonly @Input() disabled: any;
  readonly @Input() multiExpandable: any;
  readonly @Input() softDisabled: any;
  readonly @Input() wrap: any;
  expandAll(): void;
  collapseAll(): void;
}
```

### element

`HTMLElement`

A reference to the group element.

### textDirection

`any`

The text direction (ltr or rtl).

### disabled

`any`

Whether the entire accordion group is disabled.

### multiExpandable

`any`

Whether multiple accordion items can be expanded simultaneously.

### softDisabled

`any`

Whether to allow disabled items to receive focus. When `true`, disabled items are focusable but not interactive. When `false`, disabled items are skipped during navigation.

### wrap

`any`

Whether keyboard navigation should wrap around from the last item to the first, and vice-versa.

### expandAll

`void`

Expands all accordion panels if multi-expandable.

@returns`void`

### collapseAll

`void`

Collapses all accordion panels.

@returns`void`

## Description

A container for a group of accordion items. It manages the overall state and interactions of the accordion, such as keyboard navigation and expansion mode.

The `ngAccordionGroup` serves as the root of a group of accordion triggers and panels, coordinating the behavior of the `ngAccordionTrigger` and `ngAccordionPanel` elements within it. It supports both single and multiple expansion modes.

```
<div ngAccordionGroup [multiExpandable]="true" [(expandedPanels)]="expandedItems">
  <div class="accordion-item">
    <h3>
      <button ngAccordionTrigger panelId="item-1">Item 1</button>
    </h3>
    <div ngAccordionPanel panelId="item-1">
      <ng-template ngAccordionContent>
        <p>Content for Item 1.</p>
      </ng-template>
    </div>
  </div>
  <div class="accordion-item">
    <h3>
      <button ngAccordionTrigger panelId="item-2">Item 2</button>
    </h3>
    <div ngAccordionPanel panelId="item-2">
      <ng-template ngAccordionContent>
        <p>Content for Item 2.</p>
      </ng-template>
    </div>
  </div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/accordion/AccordionGroup>
