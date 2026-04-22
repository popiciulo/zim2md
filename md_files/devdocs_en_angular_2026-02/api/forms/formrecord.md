# FormRecord

FormRecord



# FormRecord

Tracks the value and validity state of a collection of [`FormControl`](formcontrol) instances, each of which has the same value type.

[FormGroup and FormRecord](../../guide/forms/typed-forms#formgroup-and-formrecord)

## API

```
class FormRecord<TControl extends AbstractControl = AbstractControl> extends FormGroup<{
  [key: string]: TControl;
}> {
  override registerControl(name: string, control: TControl): TControl;
  override addControl(name: string, control: TControl, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  override removeControl(name: string, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  override setControl(name: string, control: TControl, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  override contains(controlName: string): boolean;
  override setValue(value: { [key: string]: ɵRawValue<TControl>; }, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override patchValue(value: { [key: string]: ɵValue<TControl>; }, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override reset(value?: { [key: string]: ɵValue<TControl> | FormControlState<ɵValue<TControl>>; } | undefined, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override getRawValue(): { [key: string]: ɵRawValue<TControl>; };
  override controls: ɵTypedOrUntyped<TControl, TControl, { [key: string]: AbstractControl<any, any, any>; }>;
  readonly override value: TValue;
  override get validator(): ValidatorFn | null;
  override get asyncValidator(): AsyncValidatorFn | null;
  override readonly parent: FormGroup<any> | FormArray<any> | null;
  override readonly status: FormControlStatus;
  override readonly valid: boolean;
  override readonly invalid: boolean;
  override readonly pending: boolean;
  override readonly disabled: boolean;
  override readonly enabled: boolean;
  readonly override errors: ValidationErrors | null;
  override readonly pristine: boolean;
  override readonly dirty: boolean;
  override readonly touched: boolean;
  override readonly untouched: boolean;
  readonly override events: any;
  readonly override valueChanges: Observable<TValue>;
  readonly override statusChanges: Observable<FormControlStatus>;
  override readonly updateOn: FormHooks;
  override setValidators(validators: ValidatorFn | ValidatorFn[] | null): void;
  override setAsyncValidators(validators: AsyncValidatorFn | AsyncValidatorFn[] | null): void;
  override addValidators(validators: ValidatorFn | ValidatorFn[]): void;
  override addAsyncValidators(validators: AsyncValidatorFn | AsyncValidatorFn[]): void;
  override removeValidators(validators: ValidatorFn | ValidatorFn[]): void;
  override removeAsyncValidators(validators: AsyncValidatorFn | AsyncValidatorFn[]): void;
  override hasValidator(validator: ValidatorFn): boolean;
  override hasAsyncValidator(validator: AsyncValidatorFn): boolean;
  override clearValidators(): void;
  override clearAsyncValidators(): void;
  override markAsTouched(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override markAsTouched(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; } | undefined): void;
  override markAllAsDirty(opts?: { emitEvent?: boolean | undefined; }): void;
  override markAllAsTouched(opts?: { emitEvent?: boolean | undefined; }): void;
  override markAsUntouched(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override markAsUntouched(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override markAsDirty(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override markAsDirty(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override markAsPristine(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override markAsPristine(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override markAsPending(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override markAsPending(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override disable(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override disable(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override enable(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  override setParent(parent: FormGroup<any> | FormArray<any> | null): void;
  override updateValueAndValidity(opts?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined): void;
  override updateValueAndValidity(opts: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }): void;
  override setErrors(errors: ValidationErrors | null, opts?: { emitEvent?: boolean | undefined; } | undefined): void;
  override setErrors(errors: ValidationErrors | null, opts?: { emitEvent?: boolean | undefined; shouldHaveEmitted?: boolean | undefined; } | undefined): void;
  override get<P extends string | readonly (string | number)[]>(path: P): AbstractControl<ɵGetProperty<TRawValue, P>, ɵGetProperty<TRawValue, P>, any> | null;
  override get<P extends string | Array<string | number>>(path: P): AbstractControl<ɵGetProperty<TRawValue, P>, ɵGetProperty<TRawValue, P>, any> | null;
  override getError(errorCode: string, path?: string | (string | number)[] | undefined): any;
  override hasError(errorCode: string, path?: string | (string | number)[] | undefined): boolean;
  override readonly root: AbstractControl<any, any, any>;
}
```

### registerControl

`TControl`

Registers a control with the records's list of controls.

See [`FormGroup#registerControl`](formgroup#registerControl) for additional information.

@paramname`string`

@paramcontrol`TControl`

@returns`TControl`

### addControl

`void`

Add a control to this group.

See [`FormGroup#addControl`](formgroup#addControl) for additional information.

@paramname`string`

@paramcontrol`TControl`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### removeControl

`void`

Remove a control from this group.

See [`FormGroup#removeControl`](formgroup#removeControl) for additional information.

@paramname`string`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### setControl

`void`

Replace an existing control.

See [`FormGroup#setControl`](formgroup#setControl) for additional information.

@paramname`string`

@paramcontrol`TControl`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### contains

`boolean`

Check whether there is an enabled control with the given name in the group.

See [`FormGroup#contains`](formgroup#contains) for additional information.

@paramcontrolName`string`

@returns`boolean`

### setValue

`void`

Sets the value of the [`FormRecord`](formrecord). It accepts an object that matches the structure of the group, with control names as keys.

See [`FormGroup#setValue`](formgroup#setValue) for additional information.

@paramvalue`{ [key: string]: ɵRawValue<TControl>; }`

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### patchValue

`void`

Patches the value of the [`FormRecord`](formrecord). It accepts an object with control names as keys, and does its best to match the values to the correct controls in the group.

See [`FormGroup#patchValue`](formgroup#patchValue) for additional information.

@paramvalue`{ [key: string]: ɵValue<TControl>; }`

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### reset

`void`

Resets the [`FormRecord`](formrecord), marks all descendants `pristine` and `untouched` and sets the value of all descendants to null.

See [`FormGroup#reset`](formgroup#reset) for additional information.

@paramvalue`{ [key: string]: ɵValue<TControl> | FormControlState<ɵValue<TControl>>; } | undefined`

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### getRawValue

`{ [key: string]: ɵRawValue<TControl>; }`

The aggregate value of the [`FormRecord`](formrecord), including any disabled controls.

See [`FormGroup#getRawValue`](formgroup#getRawValue) for additional information.

@returns`{ [key: string]: ɵRawValue<TControl>; }`

### controls

`ɵTypedOrUntyped<TControl, TControl, { [key: string]: AbstractControl<any, any, any>; }>`

### value

`TValue`

The current value of the control.

- For a [`FormControl`](formcontrol), the current value.
- For an enabled [`FormGroup`](formgroup), the values of enabled controls as an object with a key-value pair for each member of the group.
- For a disabled [`FormGroup`](formgroup), the values of all controls as an object with a key-value pair for each member of the group.
- For a [`FormArray`](formarray), the values of enabled controls as an array.

### validator

`ValidatorFn | null`

Returns the function that is used to determine the validity of this control synchronously. If multiple validators have been added, this will be a single composed function. See [`Validators.compose()`](validators#compose) for additional information.

### validator

`ValidatorFn | null`

### asyncValidator

`AsyncValidatorFn | null`

Returns the function that is used to determine the validity of this control asynchronously. If multiple validators have been added, this will be a single composed function. See [`Validators.compose()`](validators#compose) for additional information.

### asyncValidator

`AsyncValidatorFn | null`

### parent

`FormGroup<any> | FormArray<any> | null`

The parent control.

### status

`FormControlStatus`

The validation status of the control.

### valid

`boolean`

A control is `valid` when its `status` is `VALID`.

### invalid

`boolean`

A control is `invalid` when its `status` is `INVALID`.

### pending

`boolean`

A control is `pending` when its `status` is `PENDING`.

### disabled

`boolean`

A control is `disabled` when its `status` is `DISABLED`.

Disabled controls are exempt from validation checks and are not included in the aggregate value of their ancestor controls.

### enabled

`boolean`

A control is `enabled` as long as its `status` is not `DISABLED`.

### errors

`ValidationErrors | null`

An object containing any errors generated by failing validation, or null if there are no errors.

### pristine

`boolean`

A control is `pristine` if the user has not yet changed the value in the UI.

### dirty

`boolean`

A control is `dirty` if the user has changed the value in the UI.

### touched

`boolean`

True if the control is marked as `touched`.

A control is marked `touched` once the user has triggered a `blur` event on it.

### untouched

`boolean`

True if the control has not been marked as touched

A control is `untouched` if the user has not yet triggered a `blur` event on it.

### events

`any`

A multicasting observable that emits an event every time the state of the control changes. It emits for value, status, pristine or touched changes.

**Note**: On value change, the emit happens right after a value of this control is updated. The value of a parent control (for example if this FormControl is a part of a FormGroup) is updated later, so accessing a value of a parent control (using the `value` property) from the callback of this event might result in getting a value that has not been updated yet. Subscribe to the `events` of the parent control instead. For other event types, the events are emitted after the parent control has been updated.

### valueChanges

`Observable<TValue>`

A multicasting observable that emits an event every time the value of the control changes, in the UI or programmatically. It also emits an event each time you call enable() or disable() without passing along {emitEvent: false} as a function argument.

**Note**: the emit happens right after a value of this control is updated. The value of a parent control (for example if this FormControl is a part of a FormGroup) is updated later, so accessing a value of a parent control (using the `value` property) from the callback of this event might result in getting a value that has not been updated yet. Subscribe to the `valueChanges` event of the parent control instead.

### statusChanges

`Observable<FormControlStatus>`

A multicasting observable that emits an event every time the validation `status` of the control recalculates.

### updateOn

`FormHooks`

Reports the update strategy of the [`AbstractControl`](abstractcontrol) (meaning the event on which the control updates itself). Possible values: `'change'` | `'blur'` | `'submit'` Default value: `'change'`

### setValidators

`void`

Sets the synchronous validators that are active on this control. Calling this overwrites any existing synchronous validators.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

If you want to add a new validator without affecting existing ones, consider using `addValidators()` method instead.

@paramvalidators`ValidatorFn | ValidatorFn[] | null`

@returns`void`

### setAsyncValidators

`void`

Sets the asynchronous validators that are active on this control. Calling this overwrites any existing asynchronous validators.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

If you want to add a new validator without affecting existing ones, consider using `addAsyncValidators()` method instead.

@paramvalidators`AsyncValidatorFn | AsyncValidatorFn[] | null`

@returns`void`

### addValidators

`void`

Add a synchronous validator or validators to this control, without affecting other validators.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

Adding a validator that already exists will have no effect. If duplicate validator functions are present in the `validators` array, only the first instance would be added to a form control.

@paramvalidators`ValidatorFn | ValidatorFn[]`

The new validator function or functions to add to this control.

@returns`void`

### addAsyncValidators

`void`

Add an asynchronous validator or validators to this control, without affecting other validators.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

Adding a validator that already exists will have no effect.

@paramvalidators`AsyncValidatorFn | AsyncValidatorFn[]`

The new asynchronous validator function or functions to add to this control.

@returns`void`

### removeValidators

`void`

Remove a synchronous validator from this control, without affecting other validators. Validators are compared by function reference; you must pass a reference to the exact same validator function as the one that was originally set. If a provided validator is not found, it is ignored.

@paramvalidators`ValidatorFn | ValidatorFn[]`

The validator or validators to remove.

@returns`void`

Usage notes

### Reference to a ValidatorFn

```
// Reference to the RequiredValidator
const ctrl = new FormControl<string | null>('', Validators.required);
ctrl.removeValidators(Validators.required);

// Reference to anonymous function inside MinValidator
const minValidator = Validators.min(3);
const ctrl = new FormControl<string | null>('', minValidator);
expect(ctrl.hasValidator(minValidator)).toEqual(true)
expect(ctrl.hasValidator(Validators.min(3))).toEqual(false)

ctrl.removeValidators(minValidator);
```

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

### removeAsyncValidators

`void`

Remove an asynchronous validator from this control, without affecting other validators. Validators are compared by function reference; you must pass a reference to the exact same validator function as the one that was originally set. If a provided validator is not found, it is ignored.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

@paramvalidators`AsyncValidatorFn | AsyncValidatorFn[]`

The asynchronous validator or validators to remove.

@returns`void`

### hasValidator

`boolean`

Check whether a synchronous validator function is present on this control. The provided validator must be a reference to the exact same function that was provided.

@paramvalidator`ValidatorFn`

The validator to check for presence. Compared by function reference.

@returns`boolean`

Usage notes

### Reference to a ValidatorFn

```
// Reference to the RequiredValidator
const ctrl = new FormControl<number | null>(0, Validators.required);
expect(ctrl.hasValidator(Validators.required)).toEqual(true)

// Reference to anonymous function inside MinValidator
const minValidator = Validators.min(3);
const ctrl = new FormControl<number | null>(0, minValidator);
expect(ctrl.hasValidator(minValidator)).toEqual(true)
expect(ctrl.hasValidator(Validators.min(3))).toEqual(false)
```

### hasAsyncValidator

`boolean`

Check whether an asynchronous validator function is present on this control. The provided validator must be a reference to the exact same function that was provided.

@paramvalidator`AsyncValidatorFn`

The asynchronous validator to check for presence. Compared by function reference.

@returns`boolean`

### clearValidators

`void`

Empties out the synchronous validator list.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

@returns`void`

### clearAsyncValidators

`void`

Empties out the async validator list.

When you add or remove a validator at run time, you must call `updateValueAndValidity()` for the new validation to take effect.

@returns`void`

### markAsTouched

2 overloads

Marks the control as `touched`. A control is touched by focus and blur events that do not change the value.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after marking is applied.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`TouchedChangeEvent`](touchedchangeevent) with the `touched` property being `true`. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; } | undefined`

@returns`void`

### markAllAsDirty

`void`

Marks the control and all its descendant controls as `dirty`.

@paramopts`{ emitEvent?: boolean | undefined; }`

Configuration options that determine how the control propagates changes and emits events after marking is applied.

- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`PristineChangeEvent`](pristinechangeevent) with the `pristine` property being `false`. When false, no events are emitted.

@returns`void`

### markAllAsTouched

`void`

Marks the control and all its descendant controls as `touched`.

@paramopts`{ emitEvent?: boolean | undefined; }`

Configuration options that determine how the control propagates changes and emits events after marking is applied.

- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`TouchedChangeEvent`](touchedchangeevent) with the `touched` property being `true`. When false, no events are emitted.

@returns`void`

### markAsUntouched

2 overloads

Marks the control as `untouched`.

If the control has any children, also marks all children as `untouched` and recalculates the `touched` status of all parent controls.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after the marking is applied.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`TouchedChangeEvent`](touchedchangeevent) with the `touched` property being `false`. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### markAsDirty

2 overloads

Marks the control as `dirty`. A control becomes dirty when the control's value is changed through the UI; compare `markAsTouched`.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after marking is applied.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`PristineChangeEvent`](pristinechangeevent) with the `pristine` property being `false`. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### markAsPristine

2 overloads

Marks the control as `pristine`.

If the control has any children, marks all children as `pristine`, and recalculates the `pristine` status of all parent controls.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control emits events after marking is applied.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `events` observable emits a [`PristineChangeEvent`](pristinechangeevent) with the `pristine` property being `true`. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### markAsPending

2 overloads

Marks the control as `pending`.

A control is pending while the control performs async validation.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after marking is applied.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `statusChanges` observable emits an event with the latest status the control is marked pending and the `events` observable emits a [`StatusChangeEvent`](statuschangeevent) with the `status` property being `PENDING` When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### disable

2 overloads

Disables the control. This means the control is exempt from validation checks and excluded from the aggregate value of any parent. Its status is `DISABLED`.

If the control has children, all children are also disabled.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after the control is disabled.

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `statusChanges`, `valueChanges` and `events` observables emit events with the latest status and value when the control is disabled. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### enable

`void`

Enables the control. This means the control is included in validation checks and the aggregate value of its parent. Its status recalculates based on its value and its validators.

By default, if the control has children, all children are enabled.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

Configure options that control how the control propagates changes and emits events when marked as untouched

- `onlySelf`: When true, mark only this control. When false or not supplied, marks all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `statusChanges`, `valueChanges` and `events` observables emit events with the latest status and value when the control is enabled. When false, no events are emitted.

@returns`void`

### setParent

`void`

Sets the parent of the control

@paramparent`FormGroup<any> | FormArray<any> | null`

The new parent.

@returns`void`

### updateValueAndValidity

2 overloads

Recalculates the value and validation status of the control.

By default, it also updates the value and validity of its ancestors.

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; } | undefined`

Configuration options determine how the control propagates changes and emits events after updates and validity checks are applied.

- `onlySelf`: When true, only update this control. When false or not supplied, update all direct ancestors. Default is false.
- `emitEvent`: When true or not supplied (the default), the `statusChanges`, `valueChanges` and `events` observables emit events with the latest status and value when the control is updated. When false, no events are emitted.

@returns`void`

@paramopts`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; sourceControl?: AbstractControl<any, any, any> | undefined; }`

@returns`void`

### setErrors

2 overloads

Sets errors on a form control when running validations manually, rather than automatically.

Calling `setErrors` also updates the validity of the parent control.

Note: Manually set errors are always overwritten by the results of the next validation run.

@paramerrors`ValidationErrors | null`

@paramopts`{ emitEvent?: boolean | undefined; } | undefined`

Configuration options that determine how the control propagates changes and emits events after the control errors are set.

- `emitEvent`: When true or not supplied (the default), the `statusChanges` observable emits an event after the errors are set.

@returns`void`

Usage notes

### Manually set the errors for a control

```
const login = new FormControl('someLogin');
login.setErrors({
  notUnique: true
});

expect(login.valid).toEqual(false);
expect(login.errors).toEqual({ notUnique: true });

login.setValue('someOtherLogin');

expect(login.valid).toEqual(true);
```

@paramerrors`ValidationErrors | null`

@paramopts`{ emitEvent?: boolean | undefined; shouldHaveEmitted?: boolean | undefined; } | undefined`

@returns`void`

### get

2 overloads

Retrieves a child control given the control's name or path.

This signature for get supports strings and `const` arrays (`.get(['foo', 'bar'] as const)`).

@parampath`P`

@returns`AbstractControl<ɵGetProperty<TRawValue, P>, ɵGetProperty<TRawValue, P>, any> | null`

Retrieves a child control given the control's name or path.

This signature for `get` supports non-const (mutable) arrays. Inferred type information will not be as robust, so prefer to pass a `readonly` array if possible.

@parampath`P`

@returns`AbstractControl<ɵGetProperty<TRawValue, P>, ɵGetProperty<TRawValue, P>, any> | null`

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

### root

`AbstractControl<any, any, any>`

Retrieves the top-level ancestor of this control.

## Description

Tracks the value and validity state of a collection of [`FormControl`](formcontrol) instances, each of which has the same value type.

[`FormRecord`](formrecord) is very similar to [`FormGroup`](formgroup), except it can be used with a dynamic keys, with controls added and removed as needed.

[`FormRecord`](formrecord) accepts one generic argument, which describes the type of the controls it contains.

## Usage Notes

```
let numbers = new FormRecord({bill: new FormControl('415-123-456')});
numbers.addControl('bob', new FormControl('415-234-567'));
numbers.removeControl('bill');
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormRecord>
