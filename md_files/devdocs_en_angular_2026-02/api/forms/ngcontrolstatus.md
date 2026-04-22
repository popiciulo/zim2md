# NgControlStatus

NgControlStatus



# NgControlStatus

Directive automatically applied to Angular form controls that sets CSS classes based on control status.

## API

```
class NgControlStatus extends AbstractControlStatus {
  constructor(cd: NgControl): NgControlStatus;
  protected override readonly isTouched: boolean;
  protected override readonly isUntouched: boolean;
  protected override readonly isPristine: boolean;
  protected override readonly isDirty: boolean;
  protected override readonly isValid: boolean;
  protected override readonly isInvalid: boolean;
  protected override readonly isPending: boolean;
  protected override readonly isSubmitted: boolean;
}
```

### constructor

`NgControlStatus`

@paramcd`NgControl`

@returns`NgControlStatus`

### isTouched

`boolean`

### isUntouched

`boolean`

### isPristine

`boolean`

### isDirty

`boolean`

### isValid

`boolean`

### isInvalid

`boolean`

### isPending

`boolean`

### isSubmitted

`boolean`

## Description

Directive automatically applied to Angular form controls that sets CSS classes based on control status.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### CSS classes applied

The following classes are applied as the properties become true:

- ng-valid
- ng-invalid
- ng-pending
- ng-pristine
- ng-dirty
- ng-untouched
- ng-touched

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgControlStatus>
