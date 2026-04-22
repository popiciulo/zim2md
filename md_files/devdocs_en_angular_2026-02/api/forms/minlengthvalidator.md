# MinLengthValidator

MinLengthValidator



# MinLengthValidator

A directive that adds minimum length validation to controls marked with the `minlength` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

[Form Validation](../../guide/forms/form-validation)

## API

```
class MinLengthValidator extends AbstractValidatorDirective {
  @Input() minlength: string | number | null;
  override enabled(input: unknown): boolean;
}
```

### minlength

`string | number | null`

Tracks changes to the minimum length bound to this directive.

### enabled

`boolean`

Determines whether this validator should be active or not based on an input. Base class implementation checks whether an input is defined (if the value is different from `null` and `undefined`). Validator classes that extend this base class can override this function with the logic specific to a particular validator directive.

@paraminput`unknown`

@returns`boolean`

## Description

A directive that adds minimum length validation to controls marked with the `minlength` attribute. The directive is provided with the [`NG_VALIDATORS`](ng_validators) multi-provider list.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Adding a minimum length validator

The following example shows how to add a minimum length validator to an input attached to an ngModel binding.

```
<input name="firstName" ngModel minlength="4">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/MinLengthValidator>
