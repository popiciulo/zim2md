# EmailValidator

EmailValidator



# EmailValidator

A directive that adds the `email` validator to controls marked with the `email` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

[Form Validation](../../guide/forms/form-validation)

## API

```
class EmailValidator extends AbstractValidatorDirective {
  @Input() email: string | boolean;
}
```

### email

`string | boolean`

Tracks changes to the email attribute bound to this directive.

## Description

A directive that adds the `email` validator to controls marked with the `email` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

The email validation is based on the WHATWG HTML specification with some enhancements to incorporate more RFC rules. More information can be found on the [Validators.email page](validators#email).

---

## Exported by

- `FormsModule`
- `ReactiveFormsModule`

## Usage Notes

### Adding an email validator

The following example shows how to add an email validator to an input attached to an ngModel binding.

```
<input type="email" name="email" ngModel email>
<input type="email" name="email" ngModel email="true">
<input type="email" name="email" ngModel [email]="true">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/EmailValidator>
