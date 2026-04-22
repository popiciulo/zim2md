# AccordionPanel

AccordionPanel



# AccordionPanel

The content panel of an accordion item that is conditionally visible.

## API

```
class AccordionPanel {
  readonly id: any;
  readonly panelId: any;
  readonly visible: any;
  expand(): void;
  collapse(): void;
  toggle(): void;
}
```

### id

`any`

A global unique identifier for the panel.

### panelId

`any`

A local unique identifier for the panel, used to match with its trigger's `panelId`.

### visible

`any`

Whether the accordion panel is visible. True if the associated trigger is expanded.

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

The content panel of an accordion item that is conditionally visible.

This directive is a container for the content that is shown or hidden. It requires a `panelId` that must match the `panelId` of its corresponding `ngAccordionTrigger`. The content within the panel should be provided using an `ng-template` with the `ngAccordionContent` directive so that the content is not rendered on the page until the trigger is expanded. It applies `role="region"` for accessibility and uses the `inert` attribute to hide its content from assistive technologies when not visible.

```
<div ngAccordionPanel panelId="unique-id-1">
  <ng-template ngAccordionContent>
    <p>This content is lazily rendered and will be shown when the panel is expanded.</p>
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/accordion/AccordionPanel>
