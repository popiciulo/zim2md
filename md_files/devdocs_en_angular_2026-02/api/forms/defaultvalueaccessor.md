# DefaultValueAccessor

DefaultValueAccessor



# DefaultValueAccessor

The default [`ControlValueAccessor`](controlvalueaccessor) for writing a value and listening to changes on input elements. The accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

## API

```
class DefaultValueAccessor extends BaseControlValueAccessor implements ControlValueAccessor {
  constructor(renderer: Renderer2, elementRef: ElementRef<any>, _compositionMode: boolean): DefaultValueAccessor;
}
```

### constructor

`DefaultValueAccessor`

@paramrenderer`Renderer2`

@paramelementRef`ElementRef<any>`

@param\_compositionMode`boolean`

@returns`DefaultValueAccessor`

## Description

The default [`ControlValueAccessor`](controlvalueaccessor) for writing a value and listening to changes on input elements. The accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using the default value accessor

The following example shows how to use an input element that activates the default value accessor (in this case, a text field).

```
const firstNameControl = new FormControl();
```

```
<input type="text" [formControl]="firstNameControl">
```

This value accessor is used by default for `<input type="text">` and `<textarea>` elements, but you could also use it for custom components that have similar behavior and do not require special processing. In order to attach the default value accessor to a custom element, add the `ngDefaultControl` attribute as shown below.

```
<custom-input-component ngDefaultControl [(ngModel)]="value"></custom-input-component>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/DefaultValueAccessor>
