# NgModel

NgModel



# NgModel

Creates a [`FormControl`](formcontrol) instance from a [domain model](https://en.wikipedia.org/wiki/Domain_model) and binds it to a form control element.

[RadioControlValueAccessor](radiocontrolvalueaccessor)[SelectControlValueAccessor](selectcontrolvalueaccessor)

## API

```
class NgModel extends NgControl implements OnChanges ,OnDestroy {
  constructor(parent: ControlContainer, validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[], valueAccessors: ControlValueAccessor[], _changeDetectorRef?: ChangeDetectorRef | null | undefined, callSetDisabledState?: SetDisabledStateOption | undefined): NgModel;
  readonly control: FormControl<any>;
  @Input() name: string;
  @Input('disabled') isDisabled: boolean;
  @Input('ngModel') model: any;
  @Input('ngModelOptions') options: { name?: string | undefined; standalone?: boolean | undefined; updateOn?: FormHooks | undefined; };
  @Output('ngModelChange') update: EventEmitter<any>;
  readonly path: string[];
  readonly formDirective: any;
  viewToModelUpdate(newValue: any): void;
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

`NgModel`

@paramparent`ControlContainer`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@paramvalueAccessors`ControlValueAccessor[]`

@param\_changeDetectorRef`ChangeDetectorRef | null | undefined`

@paramcallSetDisabledState`SetDisabledStateOption | undefined`

@returns`NgModel`

### control

`FormControl<any>`

### name

`string`

Tracks the name bound to the directive. If a parent form exists, it uses this name as a key to retrieve this control's value.

### isDisabled

`boolean`

Tracks whether the control is disabled.

### model

`any`

Tracks the value bound to this directive.

### options

`{ name?: string | undefined; standalone?: boolean | undefined; updateOn?: FormHooks | undefined; }`

Tracks the configuration options for this `ngModel` instance.

**name**: An alternative to setting the name attribute on the form control element. See the [example](ngmodel#using-ngmodel-on-a-standalone-control) for using [`NgModel`](ngmodel) as a standalone control.

**standalone**: When set to true, the `ngModel` will not register itself with its parent form, and acts as if it's not in the form. Defaults to false. If no parent form exists, this option has no effect.

**updateOn**: Defines the event upon which the form control value and validity update. Defaults to 'change'. Possible values: `'change'` | `'blur'` | `'submit'`.

### update

`EventEmitter<any>`

Event emitter for producing the `ngModelChange` event after the view model updates.

### path

`string[]`

Returns an array that represents the path from the top-level form to this control. Each index is the string name of the control on that level.

### formDirective

`any`

The top-level directive for this control if present, otherwise null.

### viewToModelUpdate

`void`

Sets the new value for the view model and emits an `ngModelChange` event.

@paramnewValue`any`

The new value emitted by `ngModelChange`.

@returns`void`

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

Creates a [`FormControl`](formcontrol) instance from a [domain model](https://en.wikipedia.org/wiki/Domain_model) and binds it to a form control element.

The [`FormControl`](formcontrol) instance tracks the value, user interaction, and validation status of the control and keeps the view synced with the model. If used within a parent form, the directive also registers itself with the form as a child control.

This directive is used by itself or as part of a larger form. Use the `ngModel` selector to activate it.

It accepts a domain model as an optional [`Input`](../core/input). If you have a one-way binding to `ngModel` with `[]` syntax, changing the domain model's value in the component class sets the value in the view. If you have a two-way binding with `[()]` syntax (also known as 'banana-in-a-box syntax'), the value in the UI always syncs back to the domain model in your class.

To inspect the properties of the associated [`FormControl`](formcontrol) (like the validity state), export the directive into a local template variable using `ngModel` as the key (ex: `#myVar="ngModel"`). You can then access the control using the directive's `field` property. However, the most commonly used properties (like `valid` and `dirty`) also exist on the control for direct access. See a full list of properties directly available in [`AbstractControlDirective`](abstractcontroldirective).

---

## Exported by

- `FormsModule`

## Usage Notes

### Using ngModel on a standalone control

The following examples show a simple standalone control using `ngModel`:

```
import {Component} from '@angular/core';

@Component({
  selector: 'example-app',
  template: `
    <input [(ngModel)]="name" #ctrl="ngModel" required />

    <p>Value: {{ name }}</p>
    <p>Valid: {{ ctrl.valid }}</p>

    <button (click)="setValue()">Set value</button>
  `,
  standalone: false,
})
export class SimpleNgModelComp {
  name: string = '';

  setValue() {
    this.name = 'Nancy';
  }
}
```

When using the `ngModel` within `<form>` tags, you'll also need to supply a `name` attribute so that the control can be registered with the parent form under that name.

In the context of a parent form, it's often unnecessary to include one-way or two-way binding, as the parent form syncs the value for you. You access its properties by exporting it into a local template variable using `ngForm` such as (`#f="ngForm"`). Use the variable where needed on form submission.

If you do need to populate initial values into your form, using a one-way binding for `ngModel` tends to be sufficient as long as you use the exported form's value rather than the domain model's value on submit.

### Using ngModel within a form

The following example shows controls using `ngModel` within a form:

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

### Using a standalone ngModel within a group

The following example shows you how to use a standalone ngModel control within a form. This controls the display of the form, but doesn't contain form data.

```
<form>
  <input name="login" ngModel placeholder="Login">
  <input type="checkbox" ngModel [ngModelOptions]="{standalone: true}"> Show more options?
</form>
<!-- form value: {login: ''} -->
```

### Setting the ngModel name attribute through options

The following example shows you an alternate way to set the name attribute. Here, an attribute identified as name is used within a custom form control component. To still be able to specify the NgModel's name, you must specify it using the `ngModelOptions` input instead.

```
<form>
  <my-custom-form-control name="Nancy" ngModel [ngModelOptions]="{name: 'user'}">
  </my-custom-form-control>
</form>
<!-- form value: {user: ''} -->
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgModel>
