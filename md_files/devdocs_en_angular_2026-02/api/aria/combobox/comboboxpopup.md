# ComboboxPopup

ComboboxPopup



# ComboboxPopup

Identifies an element as a popup for an `ngCombobox`.

## API

```
class ComboboxPopup<V> {
  readonly combobox: any;
}
```

### combobox

`any`

The combobox that the popup belongs to.

## Description

Identifies an element as a popup for an `ngCombobox`.

This directive acts as a bridge, allowing the `ngCombobox` to discover and interact with the underlying control (e.g., `ngListbox`, `ngTree`, or `ngComboboxDialog`) that manages the options. It's primarily used as a host directive and is responsible for exposing the popup's control pattern to the parent combobox.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/combobox/ComboboxPopup>
