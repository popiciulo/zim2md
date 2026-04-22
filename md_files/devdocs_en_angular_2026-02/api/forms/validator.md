# Validator

Validator



# Validator

An interface implemented by classes that perform synchronous validation.

## API

```
interface Validator {
  validate(control: AbstractControl<any, any, any>): ValidationErrors | null;
  optional registerOnValidatorChange(fn: () => void): void;
}
```

### validate

`ValidationErrors | null`

Method that performs synchronous validation against the provided control.

@paramcontrol`AbstractControl<any, any, any>`

The control to validate against.

@returns`ValidationErrors | null`

### registerOnValidatorChange

`void`

Registers a callback function to call when the validator inputs change.

@paramfn`() => void`

The callback function

@returns`void`

## Usage Notes

### Provide a custom validator

The following example implements the [`Validator`](validator) interface to create a validator directive with a custom error key.

```
@Directive({
  selector: '[customValidator]',
  providers: [{provide: NG_VALIDATORS, useExisting: forwardRef(() => CustomValidatorDirective), multi: true}]
})
class CustomValidatorDirective implements Validator {
  validate(control: AbstractControl): ValidationErrors|null {
    return {'custom': true};
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/Validator>
