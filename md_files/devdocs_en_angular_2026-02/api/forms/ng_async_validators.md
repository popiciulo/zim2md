# NG_ASYNC_VALIDATORS

NG\_ASYNC\_VALIDATORS



# NG\_ASYNC\_VALIDATORS

An [`InjectionToken`](../core/injectiontoken) for registering additional asynchronous validators used with [`AbstractControl`](abstractcontrol)s.

[NG\_VALIDATORS](ng_validators)[Implementing a custom async validator](../../guide/forms/form-validation#implementing-a-custom-async-validator)

## API

```
const NG_ASYNC_VALIDATORS: InjectionToken<readonly (Function | Validator)[]>;
```

## Usage Notes

### Provide a custom async validator directive

The following example implements the [`AsyncValidator`](asyncvalidator) interface to create an async validator directive with a custom error key.

```
@Directive({
  selector: '[customAsyncValidator]',
  providers: [{provide: NG_ASYNC_VALIDATORS, useExisting: CustomAsyncValidatorDirective, multi:
true}]
})
class CustomAsyncValidatorDirective implements AsyncValidator {
  validate(control: AbstractControl): Promise<ValidationErrors|null> {
    return Promise.resolve({'custom': true});
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NG_ASYNC_VALIDATORS>
