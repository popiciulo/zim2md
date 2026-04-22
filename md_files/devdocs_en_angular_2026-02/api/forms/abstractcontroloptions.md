# AbstractControlOptions

AbstractControlOptions



# AbstractControlOptions

Interface for options provided to an [`AbstractControl`](abstractcontrol).

## API

```
interface AbstractControlOptions {
  validators?: ValidatorFn | ValidatorFn[] | null | undefined;
  asyncValidators?: AsyncValidatorFn | AsyncValidatorFn[] | null | undefined;
  updateOn?: "change" | "blur" | "submit" | undefined;
}
```

### validators

`ValidatorFn | ValidatorFn[] | null | undefined`

The list of validators applied to a control.

### asyncValidators

`AsyncValidatorFn | AsyncValidatorFn[] | null | undefined`

The list of async validators applied to control.

### updateOn

`"change" | "blur" | "submit" | undefined`

The event name for control to update upon.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/AbstractControlOptions>
