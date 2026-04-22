# FormControlName

FormControlName



# FormControlName

Syncs a [`FormControl`](formcontrol) in an existing [`FormGroup`](formgroup) to a form control element by name.

[Reactive Forms Guide](../../guide/forms/reactive-forms)[FormControl](formcontrol)[AbstractControl](abstractcontrol)

## API

```
class FormControlName extends NgControl implements OnChanges ,OnDestroy {
  constructor(parent: ControlContainer, validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[], valueAccessors: ControlValueAccessor[], _ngModelWarningConfig: string | null): FormControlName;
  readonly control: FormControl<any>;
  @Input('formControlName') name: string | number | null;
  @Input('disabled') set isDisabled(value: boolean);
  @Input('ngModel') model: any;
  @Output('ngModelChange') update: EventEmitter<any>;
  viewToModelUpdate(newValue: any): void;
  readonly path: string[];
  readonly formDirective: any;
  override valueAccessor: ControlValueAccessor | null;
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

`FormControlName`

@paramparent`ControlContainer`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@paramvalueAccessors`ControlValueAccessor[]`

@param\_ngModelWarningConfig`string | null`

@returns`FormControlName`

### control

`FormControl<any>`

Tracks the [`FormControl`](formcontrol) instance bound to the directive.

### name

`string | number | null`

Tracks the name of the [`FormControl`](formcontrol) bound to the directive. The name corresponds to a key in the parent [`FormGroup`](formgroup) or [`FormArray`](formarray). Accepts a name as a string or a number. The name in the form of a string is useful for individual forms, while the numerical form allows for form controls to be bound to indices when iterating over controls in a [`FormArray`](formarray).

### isDisabled

`boolean`

Triggers a warning in dev mode that this input should not be used with reactive forms.

### model

`any`

@deprecated

as of v6

### update

`EventEmitter<any>`

@deprecated

as of v6

### viewToModelUpdate

`void`

Sets the new value for the view model and emits an `ngModelChange` event.

@paramnewValue`any`

The new value for the view model.

@returns`void`

### path

`string[]`

Returns an array that represents the path from the top-level form to this control. Each index is the string name of the control on that level.

### formDirective

`any`

The top-level directive for this group if present, otherwise null.

### valueAccessor

`ControlValueAccessor | null`

The value accessor for the control

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

Syncs a [`FormControl`](formcontrol) in an existing [`FormGroup`](formgroup) to a form control element by name.

---

## Exported by

- `ReactiveFormsModule`

## Usage Notes

### Register FormControl within a group

The following example shows how to register multiple form controls within a form group and set their value.

```
import {Component} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      @if(first.invalid) {
        <div>Name is too short.</div>
      }
      <input formControlName="first" placeholder="First name" />
      <input formControlName="last" placeholder="Last name" />

      <button type="submit">Submit</button>
    </form>
    <button (click)="setValue()">Set preset value</button>
  `,
  standalone: false,
})
export class SimpleFormGroup {
  form = new FormGroup({
    first: new FormControl('Nancy', Validators.minLength(2)),
    last: new FormControl('Drew'),
  });

  get first(): any {
    return this.form.get('first');
  }

  onSubmit(): void {
    console.log(this.form.value); // {first: 'Nancy', last: 'Drew'}
  }

  setValue() {
    this.form.setValue({first: 'Carson', last: 'Drew'});
  }
}
```

To see `formControlName` examples with different form control types, see:

- Radio buttons: [`RadioControlValueAccessor`](radiocontrolvalueaccessor)
- Selects: [`SelectControlValueAccessor`](selectcontrolvalueaccessor)

### Use with ngModel is deprecated

Support for using the `ngModel` input property and `ngModelChange` event with reactive form directives has been deprecated in Angular v6 and is scheduled for removal in a future version of Angular.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormControlName>
