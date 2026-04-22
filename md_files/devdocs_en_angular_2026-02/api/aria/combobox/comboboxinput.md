# ComboboxInput

ComboboxInput



# ComboboxInput

An input that is part of a combobox. It is responsible for displaying the current value and handling user input for filtering and selection.

## API

```
class ComboboxInput {
  readonly element: HTMLElement;
  readonly combobox: any;
  @Input() @Output('valueChange') value: any;
}
```

### element

`HTMLElement`

A reference to the input element.

### combobox

`any`

The combobox that the input belongs to.

### value

`any`

The value of the input.

## Description

An input that is part of a combobox. It is responsible for displaying the current value and handling user input for filtering and selection.

This directive should be applied to an `<input>` element within an `ngCombobox` container. It automatically handles keyboard interactions, such as opening the popup and navigating through the options.

```
<input
  ngComboboxInput
  placeholder="Search..."
  [(value)]="searchString"
/>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/combobox/ComboboxInput>
