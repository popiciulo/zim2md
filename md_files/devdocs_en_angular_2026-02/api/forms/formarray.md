# FormArray

FormArray



# FormArray

Tracks the value and validity state of an array of [`FormControl`](formcontrol), [`FormGroup`](formgroup) or [`FormArray`](formarray) instances.

[FormArray: Dynamic, Homogenous Collections](../../guide/forms/typed-forms#formcontrol-getting-started)[Creating dynamic forms](../../guide/forms/reactive-forms#creating-dynamic-forms)

## API

```
class FormArray<TControl extends AbstractControl<any> = any> extends AbstractControl<
  ɵTypedOrUntyped<TControl, ɵFormArrayValue<TControl>, any>,
  ɵTypedOrUntyped<TControl, ɵFormArrayRawValue<TControl>, any>
> {
  constructor(controls: TControl[], validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormArray<TControl>;
  controls: ɵTypedOrUntyped<TControl, TControl[], AbstractControl<any, any, any>[]>;
  at(index: number): ɵTypedOrUntyped<TControl, TControl, AbstractControl<any, any, any>>;
  push(control: TControl | TControl[], options?: { emitEvent?: boolean | undefined; }): void;
  insert(index: number, control: TControl, options?: { emitEvent?: boolean | undefined; }): void;
  removeAt(index: number, options?: { emitEvent?: boolean | undefined; }): void;
  setControl(index: number, control: TControl, options?: { emitEvent?: boolean | undefined; }): void;
  readonly length: number;
  setValue(value: ɵIsAny<TControl, any[], ɵRawValue<TControl>[]>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  patchValue(value: ɵIsAny<TControl, any[], ɵValue<TControl>[]>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  reset(value?: ɵTypedOrUntyped<TControl, ɵIsAny<TControl, any[], ɵValue<TControl>[]>, any>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; overwriteDefaultValue?: boolean | undefined; }): void;
  getRawValue(): ɵIsAny<TControl, any[], ɵRawValue<TControl>[]>;
  clear(options?: { emitEvent?: boolean | undefined; }): void;
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

### constructor

`FormArray<TControl>`

Creates a new [`FormArray`](formarray) instance.

@paramcontrols`TControl[]`

An array of child controls. Each child control is given an index where it is registered.

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

A synchronous validator function, or an array of such functions, or an [`AbstractControlOptions`](abstractcontroloptions) object that contains validation functions and a validation trigger.

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

A single async validator or array of async validator functions

@returns`FormArray<TControl>`

### controls

`ɵTypedOrUntyped<TControl, TControl[], AbstractControl<any, any, any>[]>`

### at

`ɵTypedOrUntyped<TControl, TControl, AbstractControl<any, any, any>>`

Get the [`AbstractControl`](abstractcontrol) at the given `index` in the array.

@paramindex`number`

Index in the array to retrieve the control. If `index` is negative, it will wrap around from the back, and if index is greatly negative (less than `-length`), the result is undefined. This behavior is the same as `Array.at(index)`.

@returns`ɵTypedOrUntyped<TControl, TControl, AbstractControl<any, any, any>>`

### push

`void`

Insert a new [`AbstractControl`](abstractcontrol) at the end of the array.

@paramcontrol`TControl | TControl[]`

Form control to be inserted

@paramoptions`{ emitEvent?: boolean | undefined; }`

Specifies whether this FormArray instance should emit events after a new control is added.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is inserted. When false, no events are emitted.

**NOTE:** Pushing to the FormArray will not mark it dirty. If you want to mark if dirty, call `markAsDirty()`.

@returns`void`

### insert

`void`

Insert a new [`AbstractControl`](abstractcontrol) at the given `index` in the array.

@paramindex`number`

Index in the array to insert the control. If `index` is negative, wraps around from the back. If `index` is greatly negative (less than `-length`), prepends to the array. This behavior is the same as `Array.splice(index, 0, control)`.

@paramcontrol`TControl`

Form control to be inserted

@paramoptions`{ emitEvent?: boolean | undefined; }`

Specifies whether this FormArray instance should emit events after a new control is inserted.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is inserted. When false, no events are emitted.

**NOTE:** Inserting to the FormArray will not mark it dirty. If you want to mark if dirty, call `markAsDirty()`.

@returns`void`

### removeAt

`void`

Remove the control at the given `index` in the array.

@paramindex`number`

Index in the array to remove the control. If `index` is negative, wraps around from the back. If `index` is greatly negative (less than `-length`), removes the first element. This behavior is the same as `Array.splice(index, 1)`.

@paramoptions`{ emitEvent?: boolean | undefined; }`

Specifies whether this FormArray instance should emit events after a control is removed.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is removed. When false, no events are emitted.

**NOTE:** Removing the FormArray will not mark it dirty. If you want to mark if dirty, call `markAsDirty()`.

@returns`void`

### setControl

`void`

Replace an existing control.

@paramindex`number`

Index in the array to replace the control. If `index` is negative, wraps around from the back. If `index` is greatly negative (less than `-length`), replaces the first element. This behavior is the same as `Array.splice(index, 1, control)`.

@paramcontrol`TControl`

The [`AbstractControl`](abstractcontrol) control to replace the existing control

@paramoptions`{ emitEvent?: boolean | undefined; }`

Specifies whether this FormArray instance should emit events after an existing control is replaced with a new one.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is replaced with a new one. When false, no events are emitted.

@returns`void`

### length

`number`

Length of the control array.

### setValue

`void`

Sets the value of the [`FormArray`](formarray). It accepts an array that matches the structure of the control.

This method performs strict checks, and throws an error if you try to set the value of a control that doesn't exist or if you exclude the value of a control.

@paramvalue`ɵIsAny<TControl, any[], ɵRawValue<TControl>[]>`

Array of values for the controls

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

Configure options that determine how the control propagates changes and emits events after the value changes

- `onlySelf`: When true, each change only affects this control, and not its parent. Default is false.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control value is updated. When false, no events are emitted. The configuration options are passed to the [`* updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

@returns`void`

Usage notes

### Set the values for the controls in the form array

```
const arr = new FormArray([
  new FormControl(),
  new FormControl()
]);
console.log(arr.value);   // [null, null]

arr.setValue(['Nancy', 'Drew']);
console.log(arr.value);   // ['Nancy', 'Drew']
```

### patchValue

`void`

Patches the value of the [`FormArray`](formarray). It accepts an array that matches the structure of the control, and does its best to match the values to the correct controls in the group.

It accepts both super-sets and sub-sets of the array without throwing an error.

@paramvalue`ɵIsAny<TControl, any[], ɵValue<TControl>[]>`

Array of latest values for the controls

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

Configure options that determine how the control propagates changes and emits events after the value changes

- `onlySelf`: When true, each change only affects this control, and not its parent. Default is false.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control value is updated. When false, no events are emitted. The configuration options are passed to the [`updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

@returns`void`

Usage notes

### Patch the values for controls in a form array

```
const arr = new FormArray([
   new FormControl(),
   new FormControl()
]);
console.log(arr.value);   // [null, null]

arr.patchValue(['Nancy']);
console.log(arr.value);   // ['Nancy', null]
```

### reset

`void`

Resets the [`FormArray`](formarray) and all descendants are marked `pristine` and `untouched`, and the value of all descendants to null or null maps.

You reset to a specific form state by passing in an array of states that matches the structure of the control. The state is a standalone value or a form state object with both a value and a disabled status.

@paramvalue`ɵTypedOrUntyped<TControl, ɵIsAny<TControl, any[], ɵValue<TControl>[]>, any>`

Array of values for the controls

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; overwriteDefaultValue?: boolean | undefined; }`

Configure options that determine how the control propagates changes and emits events after the value changes

- `onlySelf`: When true, each change only affects this control, and not its parent. Default is false.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is reset. When false, no events are emitted. The configuration options are passed to the [`* updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

@returns`void`

Usage notes

### Reset the values in a form array

```
const arr = new FormArray([
   new FormControl(),
   new FormControl()
]);
arr.reset(['name', 'last name']);

console.log(arr.value);  // ['name', 'last name']
```

### Reset the values in a form array and the disabled status for the first control

```
arr.reset([
  {value: 'name', disabled: true},
  'last'
]);

console.log(arr.value);  // ['last']
console.log(arr.at(0).status);  // 'DISABLED'
```

### getRawValue

`ɵIsAny<TControl, any[], ɵRawValue<TControl>[]>`

The aggregate value of the array, including any disabled controls.

Reports all values regardless of disabled status.

@returns`ɵIsAny<TControl, any[], ɵRawValue<TControl>[]>`

### clear

`void`

Remove all controls in the [`FormArray`](formarray).

@paramoptions`{ emitEvent?: boolean | undefined; }`

Specifies whether this FormArray instance should emit events after all controls are removed.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when all controls in this FormArray instance are removed. When false, no events are emitted.

@returns`void`

Usage notes

### Remove all elements from a FormArray

```
const arr = new FormArray([
   new FormControl(),
   new FormControl()
]);
console.log(arr.length);  // 2

arr.clear();
console.log(arr.length);  // 0
```

It's a simpler and more efficient alternative to removing all elements one by one:

```
const arr = new FormArray([
   new FormControl(),
   new FormControl()
]);

while (arr.length) {
   arr.removeAt(0);
}
```

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

Tracks the value and validity state of an array of [`FormControl`](formcontrol), [`FormGroup`](formgroup) or [`FormArray`](formarray) instances.

A [`FormArray`](formarray) aggregates the values of each child [`FormControl`](formcontrol) into an array. It calculates its status by reducing the status values of its children. For example, if one of the controls in a [`FormArray`](formarray) is invalid, the entire array becomes invalid.

[`FormArray`](formarray) accepts one generic argument, which is the type of the controls inside. If you need a heterogenous array, use [`UntypedFormArray`](untypedformarray).

[`FormArray`](formarray) is one of the four fundamental building blocks used to define forms in Angular, along with [`FormControl`](formcontrol), [`FormGroup`](formgroup), and [`FormRecord`](formrecord).

## Usage Notes

### Create an array of form controls

```
const arr = new FormArray([
  new FormControl('Nancy', Validators.minLength(2)),
  new FormControl('Drew'),
]);

console.log(arr.value);   // ['Nancy', 'Drew']
console.log(arr.status);  // 'VALID'
```

### Create a form array with array-level validators

You include array-level validators and async validators. These come in handy when you want to perform validation that considers the value of more than one child control.

The two types of validators are passed in separately as the second and third arg respectively, or together as part of an options object.

```
const arr = new FormArray([
  new FormControl('Nancy'),
  new FormControl('Drew')
], {validators: myValidator, asyncValidators: myAsyncValidator});
```

### Set the updateOn property for all controls in a form array

The options object is used to set a default value for each child control's `updateOn` property. If you set `updateOn` to `'blur'` at the array level, all child controls default to 'blur', unless the child has explicitly specified a different `updateOn` value.

```
const arr = new FormArray([
   new FormControl()
], {updateOn: 'blur'});
```

### Adding or removing controls from a form array

To change the controls in the array, use the `push`, `insert`, `removeAt` or `clear` methods in [`FormArray`](formarray) itself. These methods ensure the controls are properly tracked in the form's hierarchy. Do not modify the array of [`AbstractControl`](abstractcontrol)s used to instantiate the [`FormArray`](formarray) directly, as that result in strange and unexpected behavior such as broken change detection.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormArray>
