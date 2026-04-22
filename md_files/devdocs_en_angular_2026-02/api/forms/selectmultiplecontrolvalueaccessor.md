# SelectMultipleControlValueAccessor

SelectMultipleControlValueAccessor



# SelectMultipleControlValueAccessor

The [`ControlValueAccessor`](controlvalueaccessor) for writing multi-select control values and listening to multi-select control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

[SelectControlValueAccessor](selectcontrolvalueaccessor)

## API

```
class SelectMultipleControlValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor {
  @Input() set compareWith(value: (o1: any, o2: any) => boolean);
}
```

### compareWith

`(o1: any, o2: any) => boolean`

Tracks the option comparison algorithm for tracking identities when checking for changes.

## Description

The [`ControlValueAccessor`](controlvalueaccessor) for writing multi-select control values and listening to multi-select control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using a multi-select control

The follow example shows you how to use a multi-select control with a reactive form.

```
const countryControl = new FormControl();
```

```
<select multiple name="countries" [formControl]="countryControl">
  @for(country of countries; track $index) {
     <option [ngValue]="country">{{ country.name }}</option>
  }
</select>
```

### Customizing option selection

To customize the default option comparison algorithm, `<select>` supports `compareWith` input. See the [`SelectControlValueAccessor`](selectcontrolvalueaccessor) for usage.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/SelectMultipleControlValueAccessor>
