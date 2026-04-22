# AsyncValidatorFn

AsyncValidatorFn



# AsyncValidatorFn

A function that receives a control and returns a Promise or observable that emits validation errors if present, otherwise null.

[Creating asynchronous validators](../../guide/forms/form-validation#creating-asynchronous-validators)

## API

```
interface AsyncValidatorFn {
  (control: AbstractControl<any, any, any>): any;
}
```

`any`

@paramcontrol`AbstractControl<any, any, any>`

@returns`any`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/AsyncValidatorFn>
