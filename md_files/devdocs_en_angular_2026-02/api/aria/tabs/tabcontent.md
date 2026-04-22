# TabContent

TabContent



# TabContent

A TabContent container for the lazy-loaded content.

## API

```
class TabContent {
}
```

## Description

A TabContent container for the lazy-loaded content.

This structural directive should be applied to an `ng-template` within an `ngTabPanel`. It enables lazy loading of the tab's content, meaning the content is only rendered when the tab is activated for the first time.

```
<div ngTabPanel value="myTabId">
  <ng-template ngTabContent>
    <p>This content will be loaded when 'myTabId' is selected.</p>
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tabs/TabContent>
