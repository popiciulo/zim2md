# NgForm

NgForm



# NgForm

Creates a top-level [`FormGroup`](formgroup) instance and binds it to a form to track aggregate form value and validation status.

## API

```
class NgForm extends ControlContainer implements Form ,AfterViewInit {
  constructor(validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[], callSetDisabledState?: SetDisabledStateOption | undefined): NgForm;
  readonly submitted: boolean;
  form: FormGroup<any>;
  @Output() ngSubmit: EventEmitter<any>;
  @Input('ngFormOptions') options: { updateOn?: FormHooks | undefined; };
  readonly formDirective: Form;
  readonly control: FormGroup<any>;
  readonly path: string[];
  readonly controls: { [key: string]: AbstractControl<any, any, any>; };
  addControl(dir: NgModel): void;
  getControl(dir: NgModel): FormControl<any>;
  removeControl(dir: NgModel): void;
  addFormGroup(dir: NgModelGroup): void;
  removeFormGroup(dir: NgModelGroup): void;
  getFormGroup(dir: NgModelGroup): FormGroup<any>;
  updateModel(dir: NgControl, value: any): void;
  setValue(value: { [key: string]: any; }): void;
  onSubmit($event: Event): boolean;
  onReset(): void;
  resetForm(value?: any): void;
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

`NgForm`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@paramcallSetDisabledState`SetDisabledStateOption | undefined`

@returns`NgForm`

### submitted

`boolean`

Returns whether the form submission has been triggered.

### form

`FormGroup<any>`

The [`FormGroup`](formgroup) instance created for this form.

### ngSubmit

`EventEmitter<any>`

Event emitter for the "ngSubmit" event

### options

`{ updateOn?: FormHooks | undefined; }`

Tracks options for the [`NgForm`](ngform) instance.

**updateOn**: Sets the default `updateOn` value for all child `NgModels` below it unless explicitly set by a child [`NgModel`](ngmodel) using `ngModelOptions`). Defaults to 'change'. Possible values: `'change'` | `'blur'` | `'submit'`.

### formDirective

`Form`

The directive instance.

### control

`FormGroup<any>`

The internal [`FormGroup`](formgroup) instance.

### path

`string[]`

Returns an array representing the path to this group. Because this directive always lives at the top level of a form, it is always an empty array.

### controls

`{ [key: string]: AbstractControl<any, any, any>; }`

Returns a map of the controls in this group.

### addControl

`void`

Method that sets up the control directive in this group, re-calculates its value and validity, and adds the instance to the internal list of directives.

@paramdir`NgModel`

The [`NgModel`](ngmodel) directive instance.

@returns`void`

### getControl

`FormControl<any>`

Retrieves the [`FormControl`](formcontrol) instance from the provided [`NgModel`](ngmodel) directive.

@paramdir`NgModel`

The [`NgModel`](ngmodel) directive instance.

@returns`FormControl<any>`

### removeControl

`void`

Removes the [`NgModel`](ngmodel) instance from the internal list of directives

@paramdir`NgModel`

The [`NgModel`](ngmodel) directive instance.

@returns`void`

### addFormGroup

`void`

Adds a new [`NgModelGroup`](ngmodelgroup) directive instance to the form.

@paramdir`NgModelGroup`

The [`NgModelGroup`](ngmodelgroup) directive instance.

@returns`void`

### removeFormGroup

`void`

Removes the [`NgModelGroup`](ngmodelgroup) directive instance from the form.

@paramdir`NgModelGroup`

The [`NgModelGroup`](ngmodelgroup) directive instance.

@returns`void`

### getFormGroup

`FormGroup<any>`

Retrieves the [`FormGroup`](formgroup) for a provided [`NgModelGroup`](ngmodelgroup) directive instance

@paramdir`NgModelGroup`

The [`NgModelGroup`](ngmodelgroup) directive instance.

@returns`FormGroup<any>`

### updateModel

`void`

Sets the new value for the provided [`NgControl`](ngcontrol) directive.

@paramdir`NgControl`

The [`NgControl`](ngcontrol) directive instance.

@paramvalue`any`

The new value for the directive's control.

@returns`void`

### setValue

`void`

Sets the value for this [`FormGroup`](formgroup).

@paramvalue`{ [key: string]: any; }`

The new value

@returns`void`

### onSubmit

`boolean`

Method called when the "submit" event is triggered on the form. Triggers the `ngSubmit` emitter to emit the "submit" event as its payload.

@param$event`Event`

The "submit" event object

@returns`boolean`

### onReset

`void`

Method called when the "reset" event is triggered on the form.

@returns`void`

### resetForm

`void`

Resets the form to an initial value and resets its submitted status.

@paramvalue`any`

The new value for the form.

@returns`void`

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

## Description

Creates a top-level [`FormGroup`](formgroup) instance and binds it to a form to track aggregate form value and validation status.

As soon as you import the [`FormsModule`](formsmodule), this directive becomes active by default on all `<form>` tags. You don't need to add a special selector.

You optionally export the directive into a local template variable using `ngForm` as the key (ex: `#myForm="ngForm"`). This is optional, but useful. Many properties from the underlying [`FormGroup`](formgroup) instance are duplicated on the directive itself, so a reference to it gives you access to the aggregate value and validity status of the form, as well as user interaction properties like `dirty` and `touched`.

To register child controls with the form, use [`NgModel`](ngmodel) with a `name` attribute. You may use [`NgModelGroup`](ngmodelgroup) to create sub-groups within the form.

If necessary, listen to the directive's `ngSubmit` event to be notified when the user has triggered a form submission. The `ngSubmit` event emits the original form submission event.

In template driven forms, all `<form>` tags are automatically tagged as [`NgForm`](ngform). To import the [`FormsModule`](formsmodule) but skip its usage in some forms, for example, to use native HTML5 validation, add the `ngNoForm` and the `<form>` tags won't create an [`NgForm`](ngform) directive. In reactive forms, using `ngNoForm` is unnecessary because the `<form>` tags are inert. In that case, you would refrain from using the `formGroup` directive.

---

## Exported by

- `FormsModule`

## Usage Notes

### Listening for form submission

The following example shows how to capture the form values from the "ngSubmit" event.

```
import {Component} from '@angular/core';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form #f="ngForm" (ngSubmit)="onSubmit(f)" novalidate>
      <input name="first" ngModel required #first="ngModel" />
      <input name="last" ngModel />
      <button>Submit</button>
    </form>

    <p>First name value: {{ first.value }}</p>
    <p>First name valid: {{ first.valid }}</p>
    <p>Form value: {{ f.value | json }}</p>
    <p>Form valid: {{ f.valid }}</p>
  `,
  standalone: false,
})
export class SimpleFormComp {
  onSubmit(f: NgForm) {
    console.log(f.value); // { first: '', last: '' }
    console.log(f.valid); // false
  }
}
```

### Setting the update options

The following example shows you how to change the "updateOn" option from its default using ngFormOptions.

```
<form [ngFormOptions]="{updateOn: 'blur'}">
   <input name="one" ngModel>  <!-- this ngModel will update on blur -->
</form>
```

### Native DOM validation UI

In order to prevent the native DOM form validation UI from interfering with Angular's form validation, Angular automatically adds the `novalidate` attribute on any `<form>` whenever `FormModule` or `ReactiveFormModule` are imported into the application. If you want to explicitly enable native DOM validation UI with Angular forms, you can add the `ngNativeValidate` attribute to the `<form>` element:

```
<form ngNativeValidate>
  ...
</form>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgForm>
