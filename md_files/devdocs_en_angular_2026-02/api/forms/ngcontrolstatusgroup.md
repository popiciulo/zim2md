# NgControlStatusGroup

NgControlStatusGroup



# NgControlStatusGroup

Directive automatically applied to Angular form groups that sets CSS classes based on control status (valid/invalid/dirty/etc). On groups, this includes the additional class ng-submitted.

[NgControlStatus](ngcontrolstatus)

## API

```
class NgControlStatusGroup extends AbstractControlStatus {
  constructor(cd: ControlContainer): NgControlStatusGroup;
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

`NgControlStatusGroup`

@paramcd`ControlContainer`

@returns`NgControlStatusGroup`

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

Directive automatically applied to Angular form groups that sets CSS classes based on control status (valid/invalid/dirty/etc). On groups, this includes the additional class ng-submitted.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgControlStatusGroup>
