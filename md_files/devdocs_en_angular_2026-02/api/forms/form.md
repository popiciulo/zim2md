# Form

Form



# Form

An interface implemented by [`FormGroupDirective`](formgroupdirective) and [`NgForm`](ngform) directives.

## API

```
interface Form {
  addControl(dir: NgControl): void;
  removeControl(dir: NgControl): void;
  getControl(dir: NgControl): FormControl<any>;
  addFormGroup(dir: AbstractFormGroupDirective): void;
  removeFormGroup(dir: AbstractFormGroupDirective): void;
  getFormGroup(dir: AbstractFormGroupDirective): FormGroup<any>;
  updateModel(dir: NgControl, value: any): void;
}
```

### addControl

`void`

Add a control to this form.

@paramdir`NgControl`

The control directive to add to the form.

@returns`void`

### removeControl

`void`

Remove a control from this form.

@paramdir`NgControl`

: The control directive to remove from the form.

@returns`void`

### getControl

`FormControl<any>`

The control directive from which to get the [`FormControl`](formcontrol).

@paramdir`NgControl`

: The control directive.

@returns`FormControl<any>`

### addFormGroup

`void`

Add a group of controls to this form.

@paramdir`AbstractFormGroupDirective`

: The control group directive to add.

@returns`void`

### removeFormGroup

`void`

Remove a group of controls to this form.

@paramdir`AbstractFormGroupDirective`

: The control group directive to remove.

@returns`void`

### getFormGroup

`FormGroup<any>`

The [`FormGroup`](formgroup) associated with a particular [`AbstractFormGroupDirective`](abstractformgroupdirective).

@paramdir`AbstractFormGroupDirective`

: The form group directive from which to get the [`FormGroup`](formgroup).

@returns`FormGroup<any>`

### updateModel

`void`

Update the model for a particular control with a new value.

@paramdir`NgControl`

: The control directive to update.

@paramvalue`any`

: The new value for the control.

@returns`void`

## Description

An interface implemented by [`FormGroupDirective`](formgroupdirective) and [`NgForm`](ngform) directives.

Only used by the [`ReactiveFormsModule`](reactiveformsmodule) and [`FormsModule`](formsmodule).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/Form>
