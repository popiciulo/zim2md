# CheckboxRequiredValidator

CheckboxRequiredValidator



# CheckboxRequiredValidator

A Directive that adds the `required` validator to checkbox controls marked with the `required` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

[Form Validation](../../guide/forms/form-validation)

## API

```
class CheckboxRequiredValidator extends RequiredValidator {
  override required: string | boolean;
}
```

### required

`string | boolean`

Tracks changes to the required attribute bound to this directive.

## Description

A Directive that adds the `required` validator to checkbox controls marked with the `required` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

---

## Exported by

- `FormsModule`
- `ReactiveFormsModule`

## Usage Notes

### Adding a required checkbox validator using template-driven forms

The following example shows how to add a checkbox required validator to an input attached to an ngModel binding.

```
<input type="checkbox" name="active" ngModel required>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/CheckboxRequiredValidator>
