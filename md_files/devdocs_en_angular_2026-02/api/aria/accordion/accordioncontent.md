# AccordionContent

AccordionContent



# AccordionContent

A structural directive that provides a mechanism for lazily rendering the content for an `ngAccordionPanel`.

## API

```
class AccordionContent {
}
```

## Description

A structural directive that provides a mechanism for lazily rendering the content for an `ngAccordionPanel`.

This directive should be applied to an `ng-template` inside an `ngAccordionPanel`. It allows the content of the panel to be lazily rendered, improving performance by only creating the content when the panel is first expanded.

```
<div ngAccordionPanel panelId="unique-id-1">
  <ng-template ngAccordionContent>
    <p>This is the content that will be displayed inside the panel.</p>
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/accordion/AccordionContent>
