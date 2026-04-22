# ControlConfig

ControlConfig



# ControlConfig

ControlConfig is a tuple containing a value of type T, plus optional validators and async validators.

## API

```
type ControlConfig<T> = [
  T | FormControlState<T>,
  (ValidatorFn | ValidatorFn[])?,
  (AsyncValidatorFn | AsyncValidatorFn[])?,
]
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/ControlConfig>
