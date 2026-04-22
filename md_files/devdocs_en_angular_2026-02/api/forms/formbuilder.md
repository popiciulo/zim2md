# FormBuilder

FormBuilder



# FormBuilder

Creates an [`AbstractControl`](abstractcontrol) from a user-specified configuration.

[Reactive Forms Guide](../../guide/forms/reactive-forms)

## API

```
class FormBuilder {
  readonly nonNullable: NonNullableFormBuilder;
  group<T extends {}>(controls: T, options?: AbstractControlOptions | null | undefined): FormGroup<ɵNullableFormControls<T>>;
  group(controls: { [key: string]: any; }, options: { [key: string]: any; }): FormGroup<any>;
  record<T>(controls: { [key: string]: T; }, options?: AbstractControlOptions | null): FormRecord<ɵElement<T, null>>;
  control<T>(formState: T | FormControlState<T>, opts: FormControlOptions & { initialValueIsDefault: true; }): FormControl<T>;
  control<T>(formState: T | FormControlState<T>, opts: FormControlOptions & { nonNullable: true; }): FormControl<T>;
  control<T>(formState: T | FormControlState<T>, opts: FormControlOptions, asyncValidator: AsyncValidatorFn | AsyncValidatorFn[]): FormControl<T | null>;
  control<T>(formState: T | FormControlState<T>, validatorOrOpts?: ValidatorFn | FormControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormControl<T | null>;
  array<T>(controls: T[], validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormArray<ɵElement<T, null>>;
}
```

### nonNullable

`NonNullableFormBuilder`

Returns a FormBuilder in which automatically constructed [`FormControl`](formcontrol) elements have `{nonNullable: true}` and are non-nullable.

**Constructing non-nullable controls**

When constructing a control, it will be non-nullable, and will reset to its initial value.

```
let nnfb = new FormBuilder().nonNullable;
let name = nnfb.control('Alex'); // FormControl<string>
name.reset();
console.log(name); // 'Alex'
```

**Constructing non-nullable groups or arrays**

When constructing a group or array, all automatically created inner controls will be non-nullable, and will reset to their initial values.

```
let nnfb = new FormBuilder().nonNullable;
let name = nnfb.group({who: 'Alex'}); // FormGroup<{who: FormControl<string>}>
name.reset();
console.log(name); // {who: 'Alex'}
```

**Constructing *nullable* fields on groups or arrays**

It is still possible to have a nullable field. In particular, any [`FormControl`](formcontrol) which is *already* constructed will not be altered. For example:

```
let nnfb = new FormBuilder().nonNullable;
// FormGroup<{who: FormControl<string|null>}>
let name = nnfb.group({who: new FormControl('Alex')});
name.reset(); console.log(name); // {who: null}
```

Because the inner control is constructed explicitly by the caller, the builder has no control over how it is created, and cannot exclude the `null`.

### group

2 overloads

Constructs a new [`FormGroup`](formgroup) instance. Accepts a single generic argument, which is an object containing all the keys and corresponding inner control types.

@paramcontrols`T`

A collection of child controls. The key for each child is the name under which it is registered.

@paramoptions`AbstractControlOptions | null | undefined`

Configuration options object for the [`FormGroup`](formgroup). The object should have the [`AbstractControlOptions`](abstractcontroloptions) type and might contain the following fields:

- `validators`: A synchronous validator function, or an array of validator functions.
- `asyncValidators`: A single async validator or array of async validator functions.
- `updateOn`: The event upon which the control should be updated (options: 'change' | 'blur' | submit').

@returns`FormGroup<ɵNullableFormControls<T>>`

Constructs a new [`FormGroup`](formgroup) instance.

@deprecated

This API is not typesafe and can result in issues with Closure Compiler renaming. Use the [`FormBuilder#group`](formbuilder#group) overload with [`AbstractControlOptions`](abstractcontroloptions) instead. Note that [`AbstractControlOptions`](abstractcontroloptions) expects `validators` and `asyncValidators` to be valid validators. If you have custom validators, make sure their validation function parameter is [`AbstractControl`](abstractcontrol) and not a sub-class, such as [`FormGroup`](formgroup). These functions will be called with an object of type [`AbstractControl`](abstractcontrol) and that cannot be automatically downcast to a subclass, so TypeScript sees this as an error. For example, change the `(group: FormGroup) => ValidationErrors|null` signature to be `(group: AbstractControl) => ValidationErrors|null`.

@paramcontrols`{ [key: string]: any; }`

A record of child controls. The key for each child is the name under which the control is registered.

@paramoptions`{ [key: string]: any; }`

Configuration options object for the [`FormGroup`](formgroup). The legacy configuration object consists of:

- `validator`: A synchronous validator function, or an array of validator functions.
- `asyncValidator`: A single async validator or array of async validator functions Note: the legacy format is deprecated and might be removed in one of the next major versions of Angular.

@returns`FormGroup<any>`

### record

`FormRecord<ɵElement<T, null>>`

Constructs a new [`FormRecord`](formrecord) instance. Accepts a single generic argument, which is an object containing all the keys and corresponding inner control types.

@paramcontrols`{ [key: string]: T; }`

A collection of child controls. The key for each child is the name under which it is registered.

@paramoptions`AbstractControlOptions | null`

Configuration options object for the [`FormRecord`](formrecord). The object should have the [`AbstractControlOptions`](abstractcontroloptions) type and might contain the following fields:

- `validators`: A synchronous validator function, or an array of validator functions.
- `asyncValidators`: A single async validator or array of async validator functions.
- `updateOn`: The event upon which the control should be updated (options: 'change' | 'blur' | submit').

@returns`FormRecord<ɵElement<T, null>>`

### control

4 overloads

@deprecated

Use `nonNullable` instead.

@paramformState`T | FormControlState<T>`

@paramopts`FormControlOptions & { initialValueIsDefault: true; }`

@returns`FormControl<T>`

@paramformState`T | FormControlState<T>`

@paramopts`FormControlOptions & { nonNullable: true; }`

@returns`FormControl<T>`

@deprecated

When passing an `options` argument, the `asyncValidator` argument has no effect.

@paramformState`T | FormControlState<T>`

@paramopts`FormControlOptions`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[]`

@returns`FormControl<T | null>`

@paramformState`T | FormControlState<T>`

@paramvalidatorOrOpts`ValidatorFn | FormControlOptions | ValidatorFn[] | null | undefined`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

@returns`FormControl<T | null>`

### array

`FormArray<ɵElement<T, null>>`

Constructs a new [`FormArray`](formarray) from the given array of configurations, validators and options. Accepts a single generic argument, which is the type of each control inside the array.

@paramcontrols`T[]`

An array of child controls or control configs. Each child control is given an index when it is registered.

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

A synchronous validator function, or an array of such functions, or an [`AbstractControlOptions`](abstractcontroloptions) object that contains validation functions and a validation trigger.

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

A single async validator or array of async validator functions.

@returns`FormArray<ɵElement<T, null>>`

## Description

Creates an [`AbstractControl`](abstractcontrol) from a user-specified configuration.

The [`FormBuilder`](formbuilder) provides syntactic sugar that shortens creating instances of a [`FormControl`](formcontrol), [`FormGroup`](formgroup), or [`FormArray`](formarray). It reduces the amount of boilerplate needed to build complex forms.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormBuilder>
