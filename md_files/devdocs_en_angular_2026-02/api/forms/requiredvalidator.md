# RequiredValidator

RequiredValidator



# RequiredValidator

A directive that adds the `required` validator to any controls marked with the `required` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

[Form Validation](../../guide/forms/form-validation)

## API

```
class RequiredValidator extends AbstractValidatorDirective {
  @Input() required: string | boolean;
}
```

### required

`string | boolean`

Tracks changes to the required attribute bound to this directive.

## Description

A directive that adds the `required` validator to any controls marked with the `required` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

---

## Exported by

- `FormsModule`
- `ReactiveFormsModule`

## Usage Notes

### Adding a required validator using template-driven forms

```
<input name="fullName" ngModel required>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/RequiredValidator>
