# ComboboxPopupContainer

ComboboxPopupContainer



# ComboboxPopupContainer

A structural directive that marks the `ng-template` to be used as the popup for a combobox. This content is conditionally rendered.

## API

```
class ComboboxPopupContainer {
}
```

## Description

A structural directive that marks the `ng-template` to be used as the popup for a combobox. This content is conditionally rendered.

The content of the popup can be a `ngListbox`, `ngTree`, or `role="dialog"`, allowing for flexible and complex combobox implementations. The consumer is responsible for implementing the filtering logic based on the `ngComboboxInput`'s value.

```
<ng-template ngComboboxPopupContainer>
  <div ngListbox [(value)]="selectedValue">
    <!-- ... options ... -->
  </div>
</ng-template>
```

When using CdkOverlay, this directive can be replaced by `cdkConnectedOverlay`.

```
<ng-template
    [cdkConnectedOverlay]="{origin: inputElement, usePopover: 'inline' matchWidth: true}"
    [cdkConnectedOverlayOpen]="combobox.expanded()">
  <div ngListbox [(value)]="selectedValue">
    <!-- ... options ... -->
  </div>
</ng-template>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/aria/combobox/ComboboxPopupContainer>
