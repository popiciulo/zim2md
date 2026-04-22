# ComboboxDialog

ComboboxDialog



# ComboboxDialog

Integrates a native `<dialog>` element with the combobox, allowing for a modal or non-modal popup experience. It handles the opening and closing of the dialog based on the combobox's expanded state.

## API

```
class ComboboxDialog {
  readonly element: HTMLElement;
  readonly combobox: any;
  close(): void;
}
```

### element

`HTMLElement`

A reference to the dialog element.

### combobox

`any`

The combobox that the dialog belongs to.

### close

`void`

@returns`void`

## Description

Integrates a native `<dialog>` element with the combobox, allowing for a modal or non-modal popup experience. It handles the opening and closing of the dialog based on the combobox's expanded state.

```
<ng-template ngComboboxPopupContainer>
  <dialog ngComboboxDialog class="example-dialog">
    <!-- ... dialog content ... -->
  </dialog>
</ng-template>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/combobox/ComboboxDialog>
