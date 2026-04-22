# UntypedFormBuilder

UntypedFormBuilder



# UntypedFormBuilder

UntypedFormBuilder is the same as [`FormBuilder`](formbuilder), but it provides untyped controls.

## API

```
class UntypedFormBuilder extends FormBuilder {
  group(controlsConfig: { [key: string]: any; }, options?: AbstractControlOptions | null | undefined): UntypedFormGroup;
  group(controlsConfig: { [key: string]: any; }, options: { [key: string]: any; }): UntypedFormGroup;
  control(formState: any, validatorOrOpts?: ValidatorFn | FormControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): UntypedFormControl;
  array(controlsConfig: any[], validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): UntypedFormArray;
  override readonly nonNullable: NonNullableFormBuilder;
  override record<T>(controls: { [key: string]: T; }, options?: AbstractControlOptions | null): FormRecord<ɵElement<T, null>>;
}
```

### group

2 overloads

Like [`FormBuilder#group`](formbuilder#group), except the resulting group is untyped.

@paramcontrolsConfig`{ [key: string]: any; }`

@paramoptions`AbstractControlOptions | null | undefined`

@returns`UntypedFormGroup`

@deprecated

This API is not typesafe and can result in issues with Closure Compiler renaming. Use the [`FormBuilder#group`](formbuilder#group) overload with [`AbstractControlOptions`](abstractcontroloptions) instead.

@paramcontrolsConfig`{ [key: string]: any; }`

@paramoptions`{ [key: string]: any; }`

@returns`UntypedFormGroup`

### control

`UntypedFormControl`

Like [`FormBuilder#control`](formbuilder#control), except the resulting control is untyped.

@paramformState`any`

@paramvalidatorOrOpts`ValidatorFn | FormControlOptions | ValidatorFn[] | null | undefined`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

@returns`UntypedFormControl`

### array

`UntypedFormArray`

Like [`FormBuilder#array`](formbuilder#array), except the resulting array is untyped.

@paramcontrolsConfig`any[]`

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

@returns`UntypedFormArray`

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

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/UntypedFormBuilder>
