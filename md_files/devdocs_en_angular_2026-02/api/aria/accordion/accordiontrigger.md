# AccordionTrigger

AccordionTrigger



# AccordionTrigger

The trigger that toggles the visibility of its associated `ngAccordionPanel`.

## API

```
class AccordionTrigger {
  readonly element: HTMLElement;
  readonly @Input() id: any;
  readonly @Input() panelId: any;
  readonly @Input() disabled: any;
  readonly @Input() @Output('expandedChange') expanded: any;
  readonly active: any;
  expand(): void;
  collapse(): void;
  toggle(): void;
}
```

### element

`HTMLElement`

A reference to the trigger element.

### id

`any`

A unique identifier for the widget.

### panelId

`any`

A local unique identifier for the trigger, used to match with its panel's `panelId`.

### disabled

`any`

Whether the trigger is disabled.

### expanded

`any`

Whether the corresponding panel is expanded.

### active

`any`

Whether the trigger is active.

### expand

`void`

Expands this item.

@returns`void`

### collapse

`void`

Collapses this item.

@returns`void`

### toggle

`void`

Toggles the expansion state of this item.

@returns`void`

## Description

The trigger that toggles the visibility of its associated `ngAccordionPanel`.

This directive requires a `panelId` that must match the `panelId` of the `ngAccordionPanel` it controls. When clicked, it will expand or collapse the panel. It also handles keyboard interactions for navigation within the `ngAccordionGroup`. It applies `role="button"` and manages `aria-expanded`, `aria-controls`, and `aria-disabled` attributes for accessibility. The `disabled` input can be used to disable the trigger.

```
<button ngAccordionTrigger panelId="unique-id-1">
  Accordion Trigger Text
</button>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/accordion/AccordionTrigger>
