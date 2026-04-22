# SelectControlValueAccessor

SelectControlValueAccessor



# SelectControlValueAccessor

The [`ControlValueAccessor`](controlvalueaccessor) for writing select control values and listening to select control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

## API

```
class SelectControlValueAccessor extends BuiltInControlValueAccessor implements ControlValueAccessor {
  @Input() set compareWith(value: (o1: any, o2: any) => boolean);
}
```

### compareWith

`(o1: any, o2: any) => boolean`

Tracks the option comparison algorithm for tracking identities when checking for changes.

## Description

The [`ControlValueAccessor`](controlvalueaccessor) for writing select control values and listening to select control changes. The value accessor is used by the [`FormControlDirective`](formcontroldirective), [`FormControlName`](formcontrolname), and [`NgModel`](ngmodel) directives.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

## Usage Notes

### Using select controls in a reactive form

The following examples show how to use a select control in a reactive form.

```
import {Component} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form [formGroup]="form">
      <select formControlName="state">
        @for (state of states; track $index) {
          <option [ngValue]="state">{{ state.abbrev }}</option>
        }
      </select>
    </form>

    <p>Form value: {{ form.value | json }}</p>
    <!-- {state: {name: 'New York', abbrev: 'NY'} } -->
  `,
  standalone: false,
})
export class ReactiveSelectComp {
  states = [
    {name: 'Arizona', abbrev: 'AZ'},
    {name: 'California', abbrev: 'CA'},
    {name: 'Colorado', abbrev: 'CO'},
    {name: 'New York', abbrev: 'NY'},
    {name: 'Pennsylvania', abbrev: 'PA'},
  ];

  form = new FormGroup({
    state: new FormControl(this.states[3]),
  });
}
```

### Using select controls in a template-driven form

To use a select in a template-driven form, simply add an `ngModel` and a `name` attribute to the main `<select>` tag.

```
import {Component} from '@angular/core';

@Component({
  selector: 'example-app',
  template: `
    <form #f="ngForm">
      <select name="state" ngModel>
        <option value="" disabled>Choose a state</option>
        @for (state of states; track $index) {
          <option [ngValue]="state">{{ state.abbrev }}</option>
        }
      </select>
    </form>

    <p>Form value: {{ f.value | json }}</p>
    <!-- example value: {state: {name: 'New York', abbrev: 'NY'} } -->
  `,
  standalone: false,
})
export class SelectControlComp {
  states = [
    {name: 'Arizona', abbrev: 'AZ'},
    {name: 'California', abbrev: 'CA'},
    {name: 'Colorado', abbrev: 'CO'},
    {name: 'New York', abbrev: 'NY'},
    {name: 'Pennsylvania', abbrev: 'PA'},
  ];
}
```

### Customizing option selection

Angular uses object identity to select option. It's possible for the identities of items to change while the data does not. This can happen, for example, if the items are produced from an RPC to the server, and that RPC is re-run. Even if the data hasn't changed, the second response will produce objects with different identities.

To customize the default option comparison algorithm, `<select>` supports `compareWith` input. `compareWith` takes a **function** which has two arguments: `option1` and `option2`. If `compareWith` is given, Angular selects option by the return value of the function.

```
const selectedCountriesControl = new FormControl();
```

```
<select [compareWith]="compareFn"  [formControl]="selectedCountriesControl">
   @for(country of countries; track $index) {
       <option[ngValue]="country">{{country.name}}</option>
   }
</select>

compareFn(c1: Country, c2: Country): boolean {
    return c1 && c2 ? c1.id === c2.id : c1 === c2;
}
```

**Note:** We listen to the 'change' event because 'input' events aren't fired for selects in IE, see: <https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event#browser_compatibility>

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/SelectControlValueAccessor>
