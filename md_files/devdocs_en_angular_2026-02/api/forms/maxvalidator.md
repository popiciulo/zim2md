# MaxValidator

MaxValidator



# MaxValidator

A directive which installs the [`MaxValidator`](maxvalidator) for any `formControlName`, `formControl`, or control with `ngModel` that also has a `max` attribute.

[Form Validation](../../guide/forms/form-validation)

## API

```
class MaxValidator extends AbstractValidatorDirective {
  @Input() max: string | number | null;
  override enabled(input: unknown): boolean;
}
```

### max

`string | number | null`

Tracks changes to the max bound to this directive.

### enabled

`boolean`

Determines whether this validator should be active or not based on an input. Base class implementation checks whether an input is defined (if the value is different from `null` and `undefined`). Validator classes that extend this base class can override this function with the logic specific to a particular validator directive.

@paraminput`unknown`

@returns`boolean`

## Description

A directive which installs the [`MaxValidator`](maxvalidator) for any `formControlName`, `formControl`, or control with `ngModel` that also has a `max` attribute.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Adding a max validator

The following example shows how to add a max validator to an input attached to an ngModel binding.

```
<input type="number" ngModel max="4">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/MaxValidator>
