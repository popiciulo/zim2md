# AsyncValidator

AsyncValidator



# AsyncValidator

An interface implemented by classes that perform asynchronous validation.

[Creating asynchronous validators](../../guide/forms/form-validation#creating-asynchronous-validators)

## API

```
interface AsyncValidator extends Validator {
  validate(control: AbstractControl<any, any, any>): any;
  optional override registerOnValidatorChange(fn: () => void): void;
}
```

### validate

`any`

Method that performs async validation against the provided control.

@paramcontrol`AbstractControl<any, any, any>`

The control to validate against.

@returns`any`

### registerOnValidatorChange

`void`

Registers a callback function to call when the validator inputs change.

@paramfn`() => void`

The callback function

@returns`void`

## Usage Notes

### Provide a custom async validator directive

The following example implements the [`AsyncValidator`](asyncvalidator) interface to create an async validator directive with a custom error key.

```
import { of } from 'rxjs';

@Directive({
  selector: '[customAsyncValidator]',
  providers: [{provide: NG_ASYNC_VALIDATORS, useExisting: CustomAsyncValidatorDirective, multi:
true}]
})
class CustomAsyncValidatorDirective implements AsyncValidator {
  validate(control: AbstractControl): Observable<ValidationErrors|null> {
    return of({'custom': true});
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/AsyncValidator>
