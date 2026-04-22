# Tabs

Tabs



# Tabs

A Tabs container.

## API

```
class Tabs {
  readonly element: HTMLElement;
}
```

### element

`HTMLElement`

A reference to the host element.

## Description

A Tabs container.

The `ngTabs` directive represents a set of layered sections of content. It acts as the overarching container for a tabbed interface, coordinating the behavior of `ngTabList`, `ngTab`, and `ngTabPanel` directives.

```
<div ngTabs>
  <ul ngTabList [(selectedTab)]="selectedTabValue">
    <li ngTab value="tab1">Tab 1</li>
    <li ngTab value="tab2">Tab 2</li>
    <li ngTab value="tab3">Tab 3</li>
  </ul>

  <div ngTabPanel value="tab1">
     <ng-template ngTabContent>Content for Tab 1</ng-template>
  </div>
  <div ngTabPanel value="tab2">
     <ng-template ngTabContent>Content for Tab 2</ng-template>
  </div>
  <div ngTabPanel value="tab3">
     <ng-template ngTabContent>Content for Tab 3</ng-template>
  </div>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/tabs/Tabs>
