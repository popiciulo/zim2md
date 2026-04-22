# NonNullableFormBuilder

NonNullableFormBuilder



# NonNullableFormBuilder

[`NonNullableFormBuilder`](nonnullableformbuilder) is similar to [`FormBuilder`](formbuilder), but automatically constructed [`FormControl`](formcontrol) elements have `{nonNullable: true}` and are non-nullable.

[FormBuilder and NonNullableFormBuilder](../../guide/forms/typed-forms#formbuilder-and-nonnullableformbuilder)

## API

```
abstract class NonNullableFormBuilder {
  abstract group<T extends {}>(controls: T, options?: AbstractControlOptions | null | undefined): FormGroup<ɵNonNullableFormControls<T>>;
  abstract record<T>(controls: { [key: string]: T; }, options?: AbstractControlOptions | null | undefined): FormRecord<ɵElement<T, never>>;
  abstract array<T>(controls: T[], validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormArray<ɵElement<T, never>>;
  abstract control<T>(formState: T | FormControlState<T>, validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined, asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined): FormControl<T>;
}
```

### group

`FormGroup<ɵNonNullableFormControls<T>>`

Similar to [`FormBuilder#group`](formbuilder#group), except any implicitly constructed [`FormControl`](formcontrol) will be non-nullable (i.e. it will have `nonNullable` set to true). Note that already-constructed controls will not be altered.

@paramcontrols`T`

@paramoptions`AbstractControlOptions | null | undefined`

@returns`FormGroup<ɵNonNullableFormControls<T>>`

### record

`FormRecord<ɵElement<T, never>>`

Similar to [`FormBuilder#record`](formbuilder#record), except any implicitly constructed [`FormControl`](formcontrol) will be non-nullable (i.e. it will have `nonNullable` set to true). Note that already-constructed controls will not be altered.

@paramcontrols`{ [key: string]: T; }`

@paramoptions`AbstractControlOptions | null | undefined`

@returns`FormRecord<ɵElement<T, never>>`

### array

`FormArray<ɵElement<T, never>>`

Similar to [`FormBuilder#array`](formbuilder#array), except any implicitly constructed [`FormControl`](formcontrol) will be non-nullable (i.e. it will have `nonNullable` set to true). Note that already-constructed controls will not be altered.

@paramcontrols`T[]`

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

@returns`FormArray<ɵElement<T, never>>`

### control

`FormControl<T>`

Similar to [`FormBuilder#control`](formbuilder#control), except this overridden version of `control` forces `nonNullable` to be `true`, resulting in the control always being non-nullable.

@paramformState`T | FormControlState<T>`

@paramvalidatorOrOpts`ValidatorFn | AbstractControlOptions | ValidatorFn[] | null | undefined`

@paramasyncValidator`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

@returns`FormControl<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NonNullableFormBuilder>
