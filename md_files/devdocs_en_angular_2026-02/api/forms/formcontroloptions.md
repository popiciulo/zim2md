# FormControlOptions

FormControlOptions



# FormControlOptions

Interface for options provided to a [`FormControl`](formcontrol).

## API

```
interface FormControlOptions extends AbstractControlOptions {
  nonNullable?: boolean | undefined;
  initialValueIsDefault?: boolean | undefined;
  override validators?: ValidatorFn | ValidatorFn[] | null | undefined;
  override asyncValidators?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined;
  override updateOn?: "change" | "blur" | "submit" | undefined;
}
```

### nonNullable

`boolean | undefined`

Whether to use the initial value used to construct the [`FormControl`](formcontrol) as its default value as well. If this option is false or not provided, the default value of a FormControl is `null`. When a FormControl is reset without an explicit value, its value reverts to its default value.

### initialValueIsDefault

`boolean | undefined`

@deprecated

Use `nonNullable` instead.

### validators

`ValidatorFn | ValidatorFn[] | null | undefined`

The list of validators applied to a control.

### asyncValidators

`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

The list of async validators applied to control.

### updateOn

`"change" | "blur" | "submit" | undefined`

The event name for control to update upon.

## Description

Interface for options provided to a [`FormControl`](formcontrol).

This interface extends all options from [`AbstractControlOptions`](abstractcontroloptions), plus some options unique to [`FormControl`](formcontrol).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormControlOptions>
