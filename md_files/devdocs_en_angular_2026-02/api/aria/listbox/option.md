# Option

Option



# Option

A selectable option in an `ngListbox`.

## API

```
class Option<V> {
  readonly element: HTMLElement;
  active: any;
  readonly @Input() id: any;
  protected searchTerm: any;
  @Input() value: any;
  @Input() disabled: any;
  @Input() label: any;
  readonly selected: any;
}
```

### element

`HTMLElement`

A reference to the host element.

### active

`any`

Whether the option is currently active (focused).

### id

`any`

A unique identifier for the option.

### searchTerm

`any`

The text used by the typeahead search.

### value

`any`

The value of the option.

### disabled

`any`

Whether an item is disabled.

### label

`any`

The text used by the typeahead search.

### selected

`any`

Whether the option is selected.

## Description

A selectable option in an `ngListbox`.

This directive should be applied to an element (e.g., `<li>`, `<div>`) within an `ngListbox`. The `value` input is used to identify the option, and the `label` input provides the accessible name for the option.

```
<li ngOption value="item-id" label="Item Name">
  Item Name
</li>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/listbox/Option>
