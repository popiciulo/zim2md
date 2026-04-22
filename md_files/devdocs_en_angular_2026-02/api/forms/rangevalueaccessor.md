# RangeValueAccessor

RangeValueAccessor



# RangeValueAccessor

The [`ControlValueAccessor`](controlvalueaccessor) for writing a range value and listening to range input changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

## API

```
class RangeValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor {
}
```

## Description

The [`ControlValueAccessor`](controlvalueaccessor) for writing a range value and listening to range input changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using a range input with a reactive form

The following example shows how to use a range input with a reactive form.

```
const ageControl = new FormControl();
```

```
<input type="range" [formControl]="ageControl">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/RangeValueAccessor>
