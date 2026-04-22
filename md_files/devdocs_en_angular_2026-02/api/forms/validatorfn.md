# ValidatorFn

ValidatorFn



# ValidatorFn

A function that receives a control and synchronously returns a map of validation errors if present, otherwise null.

[Defining custom validators](../../guide/forms/form-validation#defining-custom-validators)

## API

```
interface ValidatorFn {
  (control: AbstractControl<any, any, any>): ValidationErrors | null;
}
```

`ValidationErrors | null`

@paramcontrol`AbstractControl<any, any, any>`

@returns`ValidationErrors | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/ValidatorFn>
