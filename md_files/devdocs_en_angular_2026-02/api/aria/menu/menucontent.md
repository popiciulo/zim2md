# MenuContent

MenuContent



# MenuContent

Defers the rendering of the menu content.

## API

```
class MenuContent {
}
```

## Description

Defers the rendering of the menu content.

This structural directive should be applied to an `ng-template` within a `ngMenu` or `ngMenuBar` to lazily render its content only when the menu is opened.

```
<div ngMenu #myMenu="ngMenu">
  <ng-template ngMenuContent>
    <div ngMenuItem>Lazy Item 1</div>
    <div ngMenuItem>Lazy Item 2</div>
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/menu/MenuContent>
