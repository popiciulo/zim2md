# RadioControlValueAccessor

RadioControlValueAccessor



# RadioControlValueAccessor

The [`ControlValueAccessor`](controlvalueaccessor) for writing radio control values and listening to radio control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

## API

```
class RadioControlValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor ,OnDestroy ,OnInit {
  constructor(renderer: Renderer2, elementRef: ElementRef<any>, _registry: RadioControlRegistry, _injector: Injector): RadioControlValueAccessor;
  @Input() name: string;
  @Input() formControlName: string;
  @Input() value: any;
  fireUncheck(value: any): void;
}
```

### constructor

`RadioControlValueAccessor`

@paramrenderer`Renderer2`

@paramelementRef`ElementRef<any>`

@param\_registry`RadioControlRegistry`

@param\_injector`Injector`

@returns`RadioControlValueAccessor`

### name

`string`

Tracks the name of the radio input element.

### formControlName

`string`

Tracks the name of the [`FormControl`](formcontrol) bound to the directive. The name corresponds to a key in the parent [`FormGroup`](formgroup) or [`FormArray`](formarray).

### value

`any`

Tracks the value of the radio input element

### fireUncheck

`void`

Sets the "value" on the radio input element and unchecks it.

@paramvalue`any`

@returns`void`

## Description

The [`ControlValueAccessor`](controlvalueaccessor) for writing radio control values and listening to radio control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using radio buttons with reactive form directives

The follow example shows how to use radio buttons in a reactive form. When using radio buttons in a reactive form, radio buttons in the same group should have the same `formControlName`. Providing a `name` attribute is optional.

```
import {Component} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form [formGroup]="form">
      <input type="radio" formControlName="food" value="beef" /> Beef
      <input type="radio" formControlName="food" value="lamb" /> Lamb
      <input type="radio" formControlName="food" value="fish" /> Fish
    </form>

    <p>Form value: {{ form.value | json }}</p>
    <!-- {food: 'lamb' } -->
  `,
  standalone: false,
})
export class ReactiveRadioButtonComp {
  form = new FormGroup({
    food: new FormControl('lamb'),
  });
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/RadioControlValueAccessor>
