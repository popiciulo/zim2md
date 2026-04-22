# FormArrayName

FormArrayName



# FormArrayName

Syncs a nested [`FormArray`](formarray) to a DOM element.

[Reactive Forms Guide](../../guide/forms/reactive-forms)[AbstractControl](abstractcontrol)

## API

```
class FormArrayName extends ControlContainer implements OnInit ,OnDestroy {
  constructor(parent: ControlContainer, validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[]): FormArrayName;
  @Input('formArrayName') name: string | number | null;
  readonly control: FormArray<any>;
  readonly formDirective: AbstractFormDirective | null;
  readonly path: string[];
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

`FormArrayName`

@paramparent`ControlContainer`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@returns`FormArrayName`

### name

`string | number | null`

Tracks the name of the [`FormArray`](formarray) bound to the directive. The name corresponds to a key in the parent [`FormGroup`](formgroup) or [`FormArray`](formarray). Accepts a name as a string or a number. The name in the form of a string is useful for individual forms, while the numerical form allows for form arrays to be bound to indices when iterating over arrays in a [`FormArray`](formarray).

### control

`FormArray<any>`

The [`FormArray`](formarray) bound to this directive.

### formDirective

`AbstractFormDirective | null`

The top-level directive for this group if present, otherwise null.

### path

`string[]`

Returns an array that represents the path from the top-level form to this control. Each index is the string name of the control on that level.

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

Syncs a nested [`FormArray`](formarray) to a DOM element.

This directive is designed to be used with a parent [`FormGroupDirective`](formgroupdirective)/[`FormArrayDirective`](formarraydirective) (selector: `[formGroup]`/`[formArray]`).

It accepts the string name of the nested [`FormArray`](formarray) you want to link, and will look for a [`FormArray`](formarray) registered with that name in the parent [`FormGroup`](formgroup)/[`FormArray`](formarray) instance you passed into [`FormGroupDirective`](formgroupdirective)/[`FormArrayDirective`](formarraydirective).

---

## Exported by

- `ReactiveFormsModule`

## Usage Notes

### Example

```
import {Component} from '@angular/core';
import {FormArray, FormControl, FormGroup} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <div formArrayName="cities">
        @for(city of cities.controls; track city;) {
          <input [formControlName]="$index" placeholder="City" />
        }
      </div>
      <button>Submit</button>
    </form>

    <button (click)="addCity()">Add City</button>
    <button (click)="setPreset()">Set preset</button>
  `,
  standalone: false,
})
export class NestedFormArray {
  form = new FormGroup({
    cities: new FormArray([new FormControl('SF'), new FormControl('NY')]),
  });

  get cities(): FormArray {
    return this.form.get('cities') as FormArray;
  }

  addCity() {
    this.cities.push(new FormControl());
  }

  onSubmit() {
    console.log(this.cities.value); // ['SF', 'NY']
    console.log(this.form.value); // { cities: ['SF', 'NY'] }
  }

  setPreset() {
    this.cities.patchValue(['LA', 'MTV']);
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormArrayName>
