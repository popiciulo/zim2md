# ViewEncapsulation

ViewEncapsulation



# ViewEncapsulation

Defines the CSS styles encapsulation policies for the [`Component`](component) decorator's `encapsulation` option.

## API

```
enum ViewEncapsulation {
  Emulated: ViewEncapsulation.Emulated;
  None: ViewEncapsulation.None;
  ShadowDom: ViewEncapsulation.ShadowDom;
  ExperimentalIsolatedShadowDom: ViewEncapsulation.ExperimentalIsolatedShadowDom;
}
```

### Emulated

Emulates a native Shadow DOM encapsulation behavior by adding a specific attribute to the component's host element and applying the same attribute to all the CSS selectors provided via [`styles`](component#styles) or [`styleUrls`](component#styleUrls).

This is the default option.

### None

Doesn't provide any sort of CSS style encapsulation, meaning that all the styles provided via [`styles`](component#styles) or [`styleUrls`](component#styleUrls) are applicable to any HTML element of the application regardless of their host Component.

### ShadowDom

Uses the browser's native Shadow DOM API to encapsulate CSS styles, meaning that it creates a ShadowRoot for the component's host element which is then used to encapsulate all the Component's styling.

### ExperimentalIsolatedShadowDom

@experimental

Similar to `ShadowDom`, but prevents any external styles from leaking into the component's ShadowRoot. This is useful when you want to ensure that the component's styles are completely isolated from the rest of the application, including global styles.

## Description

Defines the CSS styles encapsulation policies for the [`Component`](component) decorator's `encapsulation` option.

See [`encapsulation`](component#encapsulation).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ViewEncapsulation>
