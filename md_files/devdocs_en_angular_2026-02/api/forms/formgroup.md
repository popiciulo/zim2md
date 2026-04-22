# FormGroup

FormGroup



# FormGroup

Tracks the value and validity state of a group of [`FormControl`](formcontrol) instances.

[Grouping form controls](../../guide/forms/reactive-forms#grouping-form-controls)[FormGroup and FormRecord](../../guide/forms/typed-forms#formgroup-and-formrecord)

## API

```
class FormGroup<TControl extends {[K in keyof TControl]: AbstractControl<any>} = any> extends AbstractControl<
  ɵTypedOrUntyped<TControl, ɵFormGroupValue<TControl>, any>,
  ɵTypedOrUntyped<TControl, ɵFormGroupRawValue<TControl>, any>,
  ɵTypedOrUntyped<TControl, ɵFormGroupArgumentValue<TControl>, any>
> {
  constructor(controls: TControl, validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormGroup<TControl>;
  controls: ɵTypedOrUntyped<TControl, TControl, { [key: string]: AbstractControl<any, any, any>; }>;
  registerControl<K extends string & keyof TControl>(name: K, control: TControl[K]): TControl[K];
  registerControl(this: FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>, name: string, control: AbstractControl<any, any, any>): AbstractControl<any, any, any>;
  addControl(this: FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>, name: string, control: AbstractControl<any, any, any>, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  addControl<K extends string & keyof TControl>(name: K, control: Required<TControl>[K], options?: { emitEvent?: boolean | undefined; } | undefined): void;
  removeControl(this: FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>, name: string, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  removeControl<S extends string>(name: ɵOptionalKeys<TControl> & S, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  setControl<K extends string & keyof TControl>(name: K, control: TControl[K], options?: { emitEvent?: boolean | undefined; } | undefined): void;
  setControl(this: FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>, name: string, control: AbstractControl<any, any, any>, options?: { emitEvent?: boolean | undefined; } | undefined): void;
  contains<K extends string>(controlName: K): boolean;
  contains(this: FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>, controlName: string): boolean;
  setValue(value: ɵIsAny<TControl, { [key: string]: any; }, { [K in keyof TControl]: ɵRawValue<TControl[K]>; }>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  patchValue(value: ɵIsAny<TControl, { [key: string]: any; }, Partial<{ [K in keyof TControl]: ɵValue<TControl[K]>; }>>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }): void;
  reset(value?: ɵTypedOrUntyped<TControl, ɵIsAny<TControl, { [key: string]: any; }, Partial<{ [K in keyof TControl]: ɵValue<TControl[K]> | FormControlState<ɵValue<TControl[K]>>; }>>, any>, options?: { onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; overwriteDefaultValue?: boolean | undefined; }): void;
  getRawValue(): ɵTypedOrUntyped<TControl, ɵIsAny<TControl, { [key: string]: any; }, { [K in keyof TControl]: ɵRawValue<TControl[K]>; }>, any>;
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

`FormGroup<TControl>`

Creates a new [`FormGroup`](formgroup) instance.

@paramcontrols`TControl`

A collection of child controls. The key for each child is the name under which it is registered.

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

A synchronous validator function, or an array of such functions, or an [`AbstractControlOptions`](abstractcontroloptions) object that contains validation functions and a validation trigger.

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

A single async validator or array of async validator functions

@returns`FormGroup<TControl>`

### controls

`ɵTypedOrUntyped<TControl, TControl, { [key: string]: AbstractControl<any, any, any>; }>`

### registerControl

2 overloads

Registers a control with the group's list of controls. In a strongly-typed group, the control must be in the group's type (possibly as an optional key).

This method does not update the value or validity of the control. Use [`addControl`](formgroup#addControl) instead.

@paramname`K`

The control name to register in the collection

@paramcontrol`TControl[K]`

Provides the control for the given name

@returns`TControl[K]`

@paramthis`FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>`

@paramname`string`

@paramcontrol`AbstractControl<any, any, any>`

@returns`AbstractControl<any, any, any>`

### addControl

2 overloads

Add a control to this group. In a strongly-typed group, the control must be in the group's type (possibly as an optional key).

If a control with a given name already exists, it would *not* be replaced with a new one. If you want to replace an existing control, use the [`setControl`](formgroup#setControl) method instead. This method also updates the value and validity of the control.

@paramthis`FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>`

@paramname`string`

The control name to add to the collection

@paramcontrol`AbstractControl<any, any, any>`

Provides the control for the given name

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

Specifies whether this FormGroup instance should emit events after a new control is added.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is added. When false, no events are emitted.

@returns`void`

@paramname`K`

@paramcontrol`Required<TControl>[K]`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### removeControl

2 overloads

@paramthis`FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>`

@paramname`string`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

@paramname`ɵOptionalKeys<TControl> & S`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### setControl

2 overloads

Replace an existing control. In a strongly-typed group, the control must be in the group's type (possibly as an optional key).

If a control with a given name does not exist in this [`FormGroup`](formgroup), it will be added.

@paramname`K`

The control name to replace in the collection

@paramcontrol`TControl[K]`

Provides the control for the given name

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

Specifies whether this FormGroup instance should emit events after an existing control is replaced.

- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is replaced with a new one. When false, no events are emitted.

@returns`void`

@paramthis`FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>`

@paramname`string`

@paramcontrol`AbstractControl<any, any, any>`

@paramoptions`{ emitEvent?: boolean | undefined; } | undefined`

@returns`void`

### contains

2 overloads

Check whether there is an enabled control with the given name in the group.

Reports false for disabled controls. If you'd like to check for existence in the group only, use [`get`](abstractcontrol#get) instead.

@paramcontrolName`K`

The control name to check for existence in the collection

@returns`boolean`

@paramthis`FormGroup<{ [key: string]: AbstractControl<any, any, any>; }>`

@paramcontrolName`string`

@returns`boolean`

### setValue

`void`

Sets the value of the [`FormGroup`](formgroup). It accepts an object that matches the structure of the group, with control names as keys.

@paramvalue`ɵIsAny<TControl, { [key: string]: any; }, { [K in keyof TControl]: ɵRawValue<TControl[K]>; }>`

The new value for the control that matches the structure of the group.

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

Configuration options that determine how the control propagates changes and emits events after the value changes. The configuration options are passed to the [`* updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

- `onlySelf`: When true, each change only affects this control, and not its parent. Default is false.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control value is updated. When false, no events are emitted.

@returns`void`

Usage notes

### Set the complete value for the form group

```
const form = new FormGroup({
  first: new FormControl(),
  last: new FormControl()
});

console.log(form.value);   // {first: null, last: null}

form.setValue({first: 'Nancy', last: 'Drew'});
console.log(form.value);   // {first: 'Nancy', last: 'Drew'}
```

### patchValue

`void`

Patches the value of the [`FormGroup`](formgroup). It accepts an object with control names as keys, and does its best to match the values to the correct controls in the group.

It accepts both super-sets and sub-sets of the group without throwing an error.

@paramvalue`ɵIsAny<TControl, { [key: string]: any; }, Partial<{ [K in keyof TControl]: ɵValue<TControl[K]>; }>>`

The object that matches the structure of the group.

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; }`

Configuration options that determine how the control propagates changes and emits events after the value is patched.

- `onlySelf`: When true, each change only affects this control and not its parent. Default is true.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control value is updated. When false, no events are emitted. The configuration options are passed to the [`updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

@returns`void`

Usage notes

### Patch the value for a form group

```
const form = new FormGroup({
   first: new FormControl(),
   last: new FormControl()
});
console.log(form.value);   // {first: null, last: null}

form.patchValue({first: 'Nancy'});
console.log(form.value);   // {first: 'Nancy', last: null}
```

### reset

`void`

Resets the [`FormGroup`](formgroup), marks all descendants `pristine` and `untouched` and sets the value of all descendants to their default values, or null if no defaults were provided.

You reset to a specific form state by passing in a map of states that matches the structure of your form, with control names as keys. The state is a standalone value or a form state object with both a value and a disabled status.

@paramvalue`ɵTypedOrUntyped<TControl, ɵIsAny<TControl, { [key: string]: any; }, Partial<{ [K in keyof TControl]: ɵValue<TControl[K]> | FormControlState<ɵValue<TControl[K]>>; }>>, any>`

Resets the control with an initial value, or an object that defines the initial value and disabled state.

@paramoptions`{ onlySelf?: boolean | undefined; emitEvent?: boolean | undefined; overwriteDefaultValue?: boolean | undefined; }`

Configuration options that determine how the control propagates changes and emits events when the group is reset.

- `onlySelf`: When true, each change only affects this control, and not its parent. Default is false.
- `emitEvent`: When true or not supplied (the default), both the `statusChanges` and `valueChanges` observables emit events with the latest status and value when the control is reset. When false, no events are emitted. The configuration options are passed to the [`* updateValueAndValidity`](abstractcontrol#updateValueAndValidity) method.

@returns`void`

Usage notes

### Reset the form group values

```
const form = new FormGroup({
  first: new FormControl('first name'),
  last: new FormControl('last name')
});

console.log(form.value);  // {first: 'first name', last: 'last name'}

form.reset({ first: 'name', last: 'last name' });

console.log(form.value);  // {first: 'name', last: 'last name'}
```

### Reset the form group values and disabled status

```
const form = new FormGroup({
  first: new FormControl('first name'),
  last: new FormControl('last name')
});

form.reset({
  first: {value: 'name', disabled: true},
  last: 'last'
});

console.log(form.value);  // {last: 'last'}
console.log(form.get('first').status);  // 'DISABLED'
```

### getRawValue

`ɵTypedOrUntyped<TControl, ɵIsAny<TControl, { [key: string]: any; }, { [K in keyof TControl]: ɵRawValue<TControl[K]>; }>, any>`

The aggregate value of the [`FormGroup`](formgroup), including any disabled controls.

Retrieves all values regardless of disabled status.

@returns`ɵTypedOrUntyped<TControl, ɵIsAny<TControl, { [key: string]: any; }, { [K in keyof TControl]: ɵRawValue<TControl[K]>; }>, any>`

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

Tracks the value and validity state of a group of [`FormControl`](formcontrol) instances.

A [`FormGroup`](formgroup) aggregates the values of each child [`FormControl`](formcontrol) into one object, with each control name as the key. It calculates its status by reducing the status values of its children. For example, if one of the controls in a group is invalid, the entire group becomes invalid.

[`FormGroup`](formgroup) is one of the four fundamental building blocks used to define forms in Angular, along with [`FormControl`](formcontrol), [`FormArray`](formarray), and [`FormRecord`](formrecord).

When instantiating a [`FormGroup`](formgroup), pass in a collection of child controls as the first argument. The key for each child registers the name for the control.

[`FormGroup`](formgroup) is intended for use cases where the keys are known ahead of time. If you need to dynamically add and remove controls, use [`FormRecord`](formrecord) instead.

[`FormGroup`](formgroup) accepts an optional type parameter `TControl`, which is an object type with inner control types as values.

## Usage Notes

### Create a form group with 2 controls

```
const form = new FormGroup({
  first: new FormControl('Nancy', Validators.minLength(2)),
  last: new FormControl('Drew'),
});

console.log(form.value);   // {first: 'Nancy', last; 'Drew'}
console.log(form.status);  // 'VALID'
```

### The type argument, and optional controls

[`FormGroup`](formgroup) accepts one generic argument, which is an object containing its inner controls. This type will usually be inferred automatically, but you can always specify it explicitly if you wish.

If you have controls that are optional (i.e. they can be removed, you can use the `?` in the type):

```
const form = new FormGroup<{
  first: FormControl<string|null>,
  middle?: FormControl<string|null>, // Middle name is optional.
  last: FormControl<string|null>,
}>({
  first: new FormControl('Nancy'),
  last: new FormControl('Drew'),
});
```

### Create a form group with a group-level validator

You include group-level validators as the second arg, or group-level async validators as the third arg. These come in handy when you want to perform validation that considers the value of more than one child control.

```
const form = new FormGroup({
  password: new FormControl('', Validators.minLength(2)),
  passwordConfirm: new FormControl('', Validators.minLength(2)),
}, passwordMatchValidator);


function passwordMatchValidator(g: FormGroup) {
   return g.get('password').value === g.get('passwordConfirm').value
      ? null : {'mismatch': true};
}
```

Like [`FormControl`](formcontrol) instances, you choose to pass in validators and async validators as part of an options object.

```
const form = new FormGroup({
  password: new FormControl('')
  passwordConfirm: new FormControl('')
}, { validators: passwordMatchValidator, asyncValidators: otherValidator });
```

### Set the updateOn property for all controls in a form group

The options object is used to set a default value for each child control's `updateOn` property. If you set `updateOn` to `'blur'` at the group level, all child controls default to 'blur', unless the child has explicitly specified a different `updateOn` value.

```
const c = new FormGroup({
  one: new FormControl()
}, { updateOn: 'blur' });
```

### Using a FormGroup with optional controls

It is possible to have optional controls in a FormGroup. An optional control can be removed later using `removeControl`, and can be omitted when calling `reset`. Optional controls must be declared optional in the group's type.

```
const c = new FormGroup<{one?: FormControl<string>}>({
  one: new FormControl('')
});
```

Notice that `c.value.one` has type `string|null|undefined`. This is because calling `c.reset({})` without providing the optional key `one` will cause it to become `null`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormGroup>
