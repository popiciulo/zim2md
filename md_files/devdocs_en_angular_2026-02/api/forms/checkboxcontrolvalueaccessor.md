# CheckboxControlValueAccessor

CheckboxControlValueAccessor



# CheckboxControlValueAccessor

A [`ControlValueAccessor`](controlvalueaccessor) for writing a value and listening to changes on a checkbox input element.

## API

```
class CheckboxControlValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor {
}
```

## Description

A [`ControlValueAccessor`](controlvalueaccessor) for writing a value and listening to changes on a checkbox input element.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using a checkbox with a reactive form.

The following example shows how to use a checkbox with a reactive form.

```
const rememberLoginControl = new FormControl();
```

```
<input type="checkbox" [formControl]="rememberLoginControl">
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/CheckboxControlValueAccessor>
