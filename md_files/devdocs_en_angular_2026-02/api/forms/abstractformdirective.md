# AbstractFormDirective

AbstractFormDirective



# AbstractFormDirective

Abstract class for top-level form directives (FormArrayDirective, FormGroupDirective) who bind an existing [`Form`](form) to a DOM element.

## API

```
abstract class AbstractFormDirective extends ControlContainer implements Form ,OnChanges ,OnDestroy {
  constructor(validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[], callSetDisabledState?: SetDisabledStateOption | undefined): AbstractFormDirective;
  readonly submitted: boolean;
  directives: FormControlName[];
  abstract form: AbstractControl<any, any, any>;
  abstract ngSubmit: EventEmitter<any>;
  protected onChanges(changes: { [propName: string]: SimpleChange<any>; }): void;
  protected onDestroy(): void;
  readonly formDirective: Form;
  abstract readonly control: AbstractControl<any, any, any>;
  readonly path: string[];
  addControl(dir: FormControlName): FormControl<any>;
  getControl(dir: FormControlName): FormControl<any>;
  removeControl(dir: FormControlName): void;
  addFormGroup(dir: FormGroupName): void;
  removeFormGroup(dir: FormGroupName): void;
  getFormGroup(dir: FormGroupName): FormGroup<any>;
  getFormArray(dir: FormArrayName): FormArray<any>;
  addFormArray(dir: FormArrayName): void;
  removeFormArray(dir: FormArrayName): void;
  updateModel(dir: FormControlName, value: any): void;
  onReset(): void;
  resetForm(value?: any, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  onSubmit($event: Event): boolean;
  override name: string | number | null;
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

`AbstractFormDirective`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@paramcallSetDisabledState`SetDisabledStateOption | undefined`

@returns`AbstractFormDirective`

### submitted

`boolean`

Reports whether the form submission has been triggered.

### directives

`FormControlName[]`

Tracks the list of added [`FormControlName`](formcontrolname) instances

### form

`AbstractControl<any, any, any>`

Tracks the form bound to this directive.

### ngSubmit

`EventEmitter<any>`

Emits an event when the form submission has been triggered.

### ngOnChanges

`void`

@paramchanges`{ [propName: string]: SimpleChange<any>; }`

@returns`void`

### ngOnDestroy

`void`

@returns`void`

### onChanges

`void`

@paramchanges`{ [propName: string]: SimpleChange<any>; }`

@returns`void`

### onDestroy

`void`

@returns`void`

### formDirective

`Form`

Returns this directive's instance.

### control

`AbstractControl<any, any, any>`

Returns the Form bound to this directive.

### path

`string[]`

Returns an array representing the path to this group. Because this directive always lives at the top level of a form, it always an empty array.

### addControl

`FormControl<any>`

Method that sets up the control directive in this group, re-calculates its value and validity, and adds the instance to the internal list of directives.

@paramdir`FormControlName`

The [`FormControlName`](formcontrolname) directive instance.

@returns`FormControl<any>`

### getControl

`FormControl<any>`

Retrieves the [`FormControl`](formcontrol) instance from the provided [`FormControlName`](formcontrolname) directive

@paramdir`FormControlName`

The [`FormControlName`](formcontrolname) directive instance.

@returns`FormControl<any>`

### removeControl

`void`

Removes the [`FormControlName`](formcontrolname) instance from the internal list of directives

@paramdir`FormControlName`

The [`FormControlName`](formcontrolname) directive instance.

@returns`void`

### addFormGroup

`void`

Adds a new [`FormGroupName`](formgroupname) directive instance to the form.

@paramdir`FormGroupName`

The [`FormGroupName`](formgroupname) directive instance.

@returns`void`

### removeFormGroup

`void`

Performs the necessary cleanup when a [`FormGroupName`](formgroupname) directive instance is removed from the view.

@paramdir`FormGroupName`

The [`FormGroupName`](formgroupname) directive instance.

@returns`void`

### getFormGroup

`FormGroup<any>`

Retrieves the [`FormGroup`](formgroup) for a provided [`FormGroupName`](formgroupname) directive instance

@paramdir`FormGroupName`

The [`FormGroupName`](formgroupname) directive instance.

@returns`FormGroup<any>`

### getFormArray

`FormArray<any>`

Retrieves the [`FormArray`](formarray) for a provided [`FormArrayName`](formarrayname) directive instance.

@paramdir`FormArrayName`

The [`FormArrayName`](formarrayname) directive instance.

@returns`FormArray<any>`

### addFormArray

`void`

Performs the necessary setup when a [`FormArrayName`](formarrayname) directive instance is added to the view.

@paramdir`FormArrayName`

The [`FormArrayName`](formarrayname) directive instance.

@returns`void`

### removeFormArray

`void`

Performs the necessary cleanup when a [`FormArrayName`](formarrayname) directive instance is removed from the view.

@paramdir`FormArrayName`

The [`FormArrayName`](formarrayname) directive instance.

@returns`void`

### updateModel

`void`

Sets the new value for the provided [`FormControlName`](formcontrolname) directive.

@paramdir`FormControlName`

The [`FormControlName`](formcontrolname) directive instance.

@paramvalue`any`

The new value for the directive's control.

@returns`void`

### onReset

`void`

Method called when the "reset" event is triggered on the form.

@returns`void`

### resetForm

`void`

Resets the form to an initial value and resets its submitted status.

@paramvalue`any`

The new value for the form.

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

@returns`void`

### onSubmit

`boolean`

Method called with the "submit" event is triggered on the form. Triggers the `ngSubmit` emitter to emit the "submit" event as its payload.

@param$event`Event`

The "submit" event object

@returns`boolean`

### name

`string | number | null`

The name for the control

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

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/AbstractFormDirective>
