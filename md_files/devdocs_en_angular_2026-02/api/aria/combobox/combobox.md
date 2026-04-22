# Combobox

Combobox



# Combobox

The container element that wraps a combobox input and popup, and orchestrates its behavior.

## API

```
class Combobox<V> {
  protected textDirection: any;
  readonly element: HTMLElement;
  readonly popup: any;
  filterMode: any;
  readonly disabled: any;
  readonly readonly: any;
  readonly firstMatch: any;
  readonly expanded: any;
  readonly alwaysExpanded: any;
  readonly inputElement: any;
  open(): void;
  close(): void;
}
```

### textDirection

`any`

A signal wrapper for directionality.

### element

`HTMLElement`

A reference to the combobox element.

### popup

`any`

The combobox popup.

### filterMode

`any`

The filter mode for the combobox.

- `manual`: The consumer is responsible for filtering the options.
- `auto-select`: The combobox automatically selects the first matching option.
- `highlight`: The combobox highlights matching text in the options without changing selection.

### disabled

`any`

Whether the combobox is disabled.

### readonly

`any`

Whether the combobox is read-only.

### firstMatch

`any`

The value of the first matching item in the popup.

### expanded

`any`

Whether the combobox is expanded.

### alwaysExpanded

`any`

Whether the combobox popup should always be expanded, regardless of user interaction.

### inputElement

`any`

Input element connected to the combobox, if any.

### open

`void`

Opens the combobox to the selected item.

@returns`void`

### close

`void`

Closes the combobox.

@returns`void`

## Description

The container element that wraps a combobox input and popup, and orchestrates its behavior.

The `ngCombobox` directive is the main entry point for creating a combobox and customizing its behavior. It coordinates the interactions between the `ngComboboxInput` and the popup, which is defined by a `ng-template` with the `ngComboboxPopupContainer` directive. If using the `CdkOverlay`, the `cdkConnectedOverlay` directive takes the place of `ngComboboxPopupContainer`.

```
<div ngCombobox filterMode="highlight">
  <input
    ngComboboxInput
    placeholder="Search for a state..."
    [(value)]="searchString"
  />

  <ng-template ngComboboxPopupContainer>
    <div ngListbox [(value)]="selectedValue">
      @for (option of filteredOptions(); track option) {
        <div ngOption [value]="option" [label]="option">
          <span>{{option}}</span>
        </div>
      }
    </div>
  </ng-template>
</div>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/combobox/Combobox>
