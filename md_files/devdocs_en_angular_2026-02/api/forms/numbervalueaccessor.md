# NumberValueAccessor

NumberValueAccessor



# NumberValueAccessor

The [`ControlValueAccessor`](controlvalueaccessor) for writing a number value and listening to number input changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

## API

```
class NumberValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor {
}
```

## Description

The [`ControlValueAccessor`](controlvalueaccessor) for writing a number value and listening to number input changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using a number input with a reactive form.

The following example shows how to use a number input with a reactive form.

```
const totalCountControl = new FormControl();
```

```
<input type="number" [formControl]="totalCountControl">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NumberValueAccessor>
