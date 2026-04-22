# NgModelGroup

NgModelGroup



# NgModelGroup

Creates and binds a [`FormGroup`](formgroup) instance to a DOM element.

## API

```
class NgModelGroup extends AbstractFormGroupDirective implements OnInit ,OnDestroy {
  constructor(parent: ControlContainer, validators: (ValidatorFn | Validator)[], asyncValidators: (AsyncValidatorFn | AsyncValidator)[]): NgModelGroup;
  @Input('ngModelGroup') name: string;
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

`NgModelGroup`

@paramparent`ControlContainer`

@paramvalidators`(ValidatorFn | Validator)[]`

@paramasyncValidators`(AsyncValidatorFn | AsyncValidator)[]`

@returns`NgModelGroup`

### name

`string`

Tracks the name of the [`NgModelGroup`](ngmodelgroup) bound to the directive. The name corresponds to a key in the parent [`NgForm`](ngform).

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

Creates and binds a [`FormGroup`](formgroup) instance to a DOM element.

This directive can only be used as a child of [`NgForm`](ngform) (within `<form>` tags).

Use this directive to validate a sub-group of your form separately from the rest of your form, or if some values in your domain model make more sense to consume together in a nested object.

Provide a name for the sub-group and it will become the key for the sub-group in the form's full value. If you need direct access, export the directive into a local template variable using `ngModelGroup` (ex: `#myGroup="ngModelGroup"`).

---

## Exported by

- `FormsModule`

## Usage Notes

### Consuming controls in a grouping

The following example shows you how to combine controls together in a sub-group of the form.

```
import {Component} from '@angular/core';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'example-app',
  template: `
    <form #f="ngForm" (ngSubmit)="onSubmit(f)">
      @if(nameCtrl.invalid) {
        <p>Name is invalid.</p>
      }
      <div ngModelGroup="name" #nameCtrl="ngModelGroup">
        <input name="first" [ngModel]="name.first" minlength="2" />
        <input name="middle" [ngModel]="name.middle" maxlength="2" />
        <input name="last" [ngModel]="name.last" required />
      </div>

      <input name="email" ngModel />
      <button>Submit</button>
    </form>

    <button (click)="setValue()">Set value</button>
  `,
  standalone: false,
})
export class NgModelGroupComp {
  name = {first: 'Nancy', middle: 'J', last: 'Drew'};

  onSubmit(f: NgForm) {
    console.log(f.value); // {name: {first: 'Nancy', middle: 'J', last: 'Drew'}, email: ''}
    console.log(f.valid); // true
  }

  setValue() {
    this.name = {first: 'Bess', middle: 'S', last: 'Marvin'};
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgModelGroup>
