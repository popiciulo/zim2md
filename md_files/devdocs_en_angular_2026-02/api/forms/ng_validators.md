# NG_VALIDATORS

NG\_VALIDATORS



# NG\_VALIDATORS

An [`InjectionToken`](../core/injectiontoken) for registering additional synchronous validators used with [`AbstractControl`](abstractcontrol)s.

[NG\_ASYNC\_VALIDATORS](ng_async_validators)[Defining custom validators](../../guide/forms/form-validation#defining-custom-validators)

## API

```
const NG_VALIDATORS: InjectionToken<readonly (Function | Validator)[]>;
```

## Usage Notes

### Providing a custom validator

The following example registers a custom validator directive. Adding the validator to the existing collection of validators requires the `multi: true` option.

```
@Directive({
  selector: '[customValidator]',
  providers: [{provide: NG_VALIDATORS, useExisting: forwardRef(() => CustomValidatorDirective), multi: true}]
})
class CustomValidatorDirective implements Validator {
  validate(control: AbstractControl): ValidationErrors | null {
    return { 'custom': true };
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NG_VALIDATORS>
