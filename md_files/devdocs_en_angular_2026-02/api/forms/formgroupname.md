# FormGroupName

FormGroupName



# FormGroupName

Syncs a nested [`FormGroup`](formgroup) or [`FormRecord`](formrecord) to a DOM element.

[Reactive Forms Guide](../../guide/forms/reactive-forms)

## API

```
class FormGroupName extends AbstractFormGroupDirective implements OnInit ,OnDestroy {
  constructor(parent: ControlContainer, validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[]): FormGroupName;
  @Input('formGroupName') name: string | number | null;
  override readonly control: FormGroup<any>;
  override readonly path: string[];
  override readonly formDirective: Form | null;
  override readonly value: any;
  override readonly valid: boolean | null;
  override readonly invalid: boolean | null;
  override readonly pending: boolean | null;
  override readonly disabled: boolean | null;
  override readonly enabled: boolean | null;
  override readonly errors: ValidationErrors | null;
  override readonly pristine: boolean | null;
  override readonly dirty: boolean | null;
  override readonly touched: boolean | null;
  override readonly status: string | null;
  override readonly untouched: boolean | null;
  override readonly statusChanges: any;
  override readonly valueChanges: any;
  override readonly validator: ValidatorFn | null;
  override readonly asyncValidator: AsyncValidatorFn | null;
  override reset(value?: any): void;
  override hasError(errorCode: string, path?: string | (string | number)[] | undefined): boolean;
  override getError(errorCode: string, path?: string | (string | number)[] | undefined): any;
}
```

### constructor

`FormGroupName`

@paramparent`ControlContainer`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@returns`FormGroupName`

### name

`string | number | null`

Tracks the name of the [`FormGroup`](formgroup) bound to the directive. The name corresponds to a key in the parent [`FormGroup`](formgroup) or [`FormArray`](formarray). Accepts a name as a string or a number. The name in the form of a string is useful for individual forms, while the numerical form allows for form groups to be bound to indices when iterating over groups in a [`FormArray`](formarray).

### control

`FormGroup<any>`

The [`FormGroup`](formgroup) bound to this directive.

### path

`string[]`

The path to this group from the top-level directive.

### formDirective

`Form | null`

The top-level directive for this group if present, otherwise null.

### value

`any`

Reports the value of the control if it is present, otherwise null.

### valid

`boolean | null`

Reports whether the control is valid. A control is considered valid if no validation errors exist with the current value. If the control is not present, null is returned.

### invalid

`boolean | null`

Reports whether the control is invalid, meaning that an error exists in the input value. If the control is not present, null is returned.

### pending

`boolean | null`

Reports whether a control is pending, meaning that async validation is occurring and errors are not yet available for the input value. If the control is not present, null is returned.

### disabled

`boolean | null`

Reports whether the control is disabled, meaning that the control is disabled in the UI and is exempt from validation checks and excluded from aggregate values of ancestor controls. If the control is not present, null is returned.

### enabled

`boolean | null`

Reports whether the control is enabled, meaning that the control is included in ancestor calculations of validity or value. If the control is not present, null is returned.

### errors

`ValidationErrors | null`

Reports the control's validation errors. If the control is not present, null is returned.

### pristine

`boolean | null`

Reports whether the control is pristine, meaning that the user has not yet changed the value in the UI. If the control is not present, null is returned.

### dirty

`boolean | null`

Reports whether the control is dirty, meaning that the user has changed the value in the UI. If the control is not present, null is returned.

### touched

`boolean | null`

Reports whether the control is touched, meaning that the user has triggered a `blur` event on it. If the control is not present, null is returned.

### status

`string | null`

Reports the validation status of the control. Possible values include: 'VALID', 'INVALID', 'DISABLED', and 'PENDING'. If the control is not present, null is returned.

### untouched

`boolean | null`

Reports whether the control is untouched, meaning that the user has not yet triggered a `blur` event on it. If the control is not present, null is returned.

### statusChanges

`any`

Returns a multicasting observable that emits a validation status whenever it is calculated for the control. If the control is not present, null is returned.

### valueChanges

`any`

Returns a multicasting observable of value changes for the control that emits every time the value of the control changes in the UI or programmatically. If the control is not present, null is returned.

### validator

`ValidatorFn | null`

Synchronous validator function composed of all the synchronous validators registered with this directive.

### asyncValidator

`AsyncValidatorFn | null`

Asynchronous validator function composed of all the asynchronous validators registered with this directive.

### reset

`void`

Resets the control with the provided value if the control is present.

@paramvalue`any`

@returns`void`

### hasError

`boolean`

Reports whether the control with the given path has the error specified.

@paramerrorCode`string`

The code of the error to check

@parampath`string | (string | number)[] | undefined`

A list of control names that designates how to move from the current control to the control that should be queried for errors.

@returns`boolean`

Usage notes

For example, for the following [`FormGroup`](formgroup):

```
form = new FormGroup({
  address: new FormGroup({ street: new FormControl() })
});
```

The path to the 'street' control from the root form would be 'address' -> 'street'.

It can be provided to this method in one of two formats:

1. An array of string control names, e.g. `['address', 'street']`
2. A period-delimited list of control names in one string, e.g. `'address.street'`

If no path is given, this method checks for the error on the current control.

### getError

`any`

Reports error data for the control with the given path.

@paramerrorCode`string`

The code of the error to check

@parampath`string | (string | number)[] | undefined`

A list of control names that designates how to move from the current control to the control that should be queried for errors.

@returns`any`

Usage notes

For example, for the following [`FormGroup`](formgroup):

```
form = new FormGroup({
  address: new FormGroup({ street: new FormControl() })
});
```

The path to the 'street' control from the root form would be 'address' -> 'street'.

It can be provided to this method in one of two formats:

1. An array of string control names, e.g. `['address', 'street']`
2. A period-delimited list of control names in one string, e.g. `'address.street'`

## Description

Syncs a nested [`FormGroup`](formgroup) or [`FormRecord`](formrecord) to a DOM element.

This directive can only be used with a parent [`FormGroupDirective`](formgroupdirective).

It accepts the string name of the nested [`FormGroup`](formgroup) or [`FormRecord`](formrecord) to link, and looks for a [`FormGroup`](formgroup) or [`FormRecord`](formrecord) registered with that name in the parent [`FormGroup`](formgroup) instance you passed into [`FormGroupDirective`](formgroupdirective).

Use nested form groups to validate a sub-group of a form separately from the rest or to group the values of certain controls into their own nested object.

---

## Exported by

- `ReactiveFormsModule`

## Usage Notes

### Access the group by name

The following example uses the [`AbstractControl.get`](abstractcontrol#get) method to access the associated [`FormGroup`](formgroup)

```
  this.form.get('name');
```

### Access individual controls in the group

The following example uses the [`AbstractControl.get`](abstractcontrol#get) method to access individual controls within the group using dot syntax.

```
  this.form.get('name.first');
```

### Register a nested FormGroup.

The following example registers a nested *name* [`FormGroup`](formgroup) within an existing [`FormGroup`](formgroup), and provides methods to retrieve the nested [`FormGroup`](formgroup) and individual controls.

```
import {Component} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      @if(name.invalid) {
        <p>Name is invalid.</p>
      }
      <div formGroupName="name">
        <input formControlName="first" placeholder="First name" />
        <input formControlName="last" placeholder="Last name" />
      </div>
      <input formControlName="email" placeholder="Email" />
      <button type="submit">Submit</button>
    </form>

    <button (click)="setPreset()">Set preset</button>
  `,
  standalone: false,
})
export class NestedFormGroupComp {
  form = new FormGroup({
    name: new FormGroup({
      first: new FormControl('Nancy', Validators.minLength(2)),
      last: new FormControl('Drew', Validators.required),
    }),
    email: new FormControl(),
  });

  get first(): any {
    return this.form.get('name.first');
  }

  get name(): any {
    return this.form.get('name');
  }

  onSubmit() {
    console.log(this.first.value); // 'Nancy'
    console.log(this.name.value); // {first: 'Nancy', last: 'Drew'}
    console.log(this.form.value); // {name: {first: 'Nancy', last: 'Drew'}, email: ''}
    console.log(this.form.status); // VALID
  }

  setPreset() {
    this.name.setValue({first: 'Bess', last: 'Marvin'});
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormGroupName>
