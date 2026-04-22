# Validators

Validators



# Validators

Provides a set of built-in validators that can be used by form controls.

[Form Validation](../../guide/forms/form-validation)

## API

```
class Validators {
  static min(min: number): ValidatorFn;
  static max(max: number): ValidatorFn;
  static required(control: AbstractControl<any, any, any>): ValidationErrors | null;
  static requiredTrue(control: AbstractControl<any, any, any>): ValidationErrors | null;
  static email(control: AbstractControl<any, any, any>): ValidationErrors | null;
  static minLength(minLength: number): ValidatorFn;
  static maxLength(maxLength: number): ValidatorFn;
  static pattern(pattern: string | RegExp): ValidatorFn;
  static nullValidator(control: AbstractControl<any, any, any>): ValidationErrors | null;
  static compose(validators: null): null;
  static compose(validators: (ValidatorFn | null | undefined)[]): ValidatorFn | null;
  static composeAsync(validators: (AsyncValidatorFn | null)[]): AsyncValidatorFn | null;
}
```

### min

`ValidatorFn`

Validator that requires the control's value to be greater than or equal to the provided number.

@parammin`number`

@returns`ValidatorFn`

Usage notes

### Validate against a minimum of 3

```
const control = new FormControl(2, Validators.min(3));

console.log(control.errors); // {min: {min: 3, actual: 2}}
```

### max

`ValidatorFn`

Validator that requires the control's value to be less than or equal to the provided number.

@parammax`number`

@returns`ValidatorFn`

Usage notes

### Validate against a maximum of 15

```
const control = new FormControl(16, Validators.max(15));

console.log(control.errors); // {max: {max: 15, actual: 16}}
```

### required

`ValidationErrors | null`

Validator that requires the control have a non-empty value.

@paramcontrol`AbstractControl<any, any, any>`

@returns`ValidationErrors | null`

Usage notes

### Validate that the field is non-empty

```
const control = new FormControl('', Validators.required);

console.log(control.errors); // {required: true}
```

### requiredTrue

`ValidationErrors | null`

Validator that requires the control's value be true. This validator is commonly used for required checkboxes.

@paramcontrol`AbstractControl<any, any, any>`

@returns`ValidationErrors | null`

Usage notes

### Validate that the field value is true

```
const control = new FormControl('some value', Validators.requiredTrue);

console.log(control.errors); // {required: true}
```

### email

`ValidationErrors | null`

Validator that requires the control's value pass an email validation test.

Tests the value using a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) pattern suitable for common use cases. The pattern is based on the definition of a valid email address in the [WHATWG HTML specification](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) with some enhancements to incorporate more RFC rules (such as rules related to domain names and the lengths of different parts of the address).

The differences from the WHATWG version include:

- Disallow `local-part` (the part before the `@` symbol) to begin or end with a period (`.`).
- Disallow `local-part` to be longer than 64 characters.
- Disallow the whole address to be longer than 254 characters.

If this pattern does not satisfy your business needs, you can use [`Validators.pattern()`](validators#pattern) to validate the value against a different pattern.

@paramcontrol`AbstractControl<any, any, any>`

@returns`ValidationErrors | null`

Usage notes

### Validate that the field matches a valid email pattern

```
const control = new FormControl('bad@', Validators.email);

console.log(control.errors); // {email: true}
```

### minLength

`ValidatorFn`

Validator that requires the number of items in the control's value to be greater than or equal to the provided minimum length. This validator is also provided by default if you use the HTML5 `minlength` attribute. Note that the `minLength` validator is intended to be used only for types that have a numeric `length` or `size` property, such as strings, arrays or sets. The `minLength` validator logic is also not invoked for values when their `length` or `size` property is 0 (for example in case of an empty string or an empty array), to support optional controls. You can use the standard `required` validator if empty values should not be considered valid.

@paramminLength`number`

@returns`ValidatorFn`

Usage notes

### Validate that the field has a minimum of 3 characters

```
const control = new FormControl('ng', Validators.minLength(3));

console.log(control.errors); // {minlength: {requiredLength: 3, actualLength: 2}}
```

```
<input minlength="5">
```

### maxLength

`ValidatorFn`

Validator that requires the number of items in the control's value to be less than or equal to the provided maximum length. This validator is also provided by default if you use the HTML5 `maxlength` attribute. Note that the `maxLength` validator is intended to be used only for types that have a numeric `length` or `size` property, such as strings, arrays or sets.

@parammaxLength`number`

@returns`ValidatorFn`

Usage notes

### Validate that the field has maximum of 5 characters

```
const control = new FormControl('Angular', Validators.maxLength(5));

console.log(control.errors); // {maxlength: {requiredLength: 5, actualLength: 7}}
```

```
<input maxlength="5">
```

### pattern

`ValidatorFn`

Validator that requires the control's value to match a regex pattern. This validator is also provided by default if you use the HTML5 `pattern` attribute.

@parampattern`string | RegExp`

A regular expression to be used as is to test the values, or a string. If a string is passed, the `^` character is prepended and the `$` character is appended to the provided string (if not already present), and the resulting regular expression is used to test the values.

@returns`ValidatorFn`

Usage notes

### Validate that the field only contains letters or spaces

```
const control = new FormControl('1', Validators.pattern('[a-zA-Z ]*'));

console.log(control.errors); // {pattern: {requiredPattern: '^[a-zA-Z ]*$', actualValue: '1'}}
```

```
<input pattern="[a-zA-Z ]*">
```

### Pattern matching with the global or sticky flag

`RegExp` objects created with the `g` or `y` flags that are passed into [`Validators.pattern`](validators#pattern) can produce different results on the same input when validations are run consecutively. This is due to how the behavior of `RegExp.prototype.test` is specified in [ECMA-262](https://tc39.es/ecma262/#sec-regexpbuiltinexec) (`RegExp` preserves the index of the last match when the global or sticky flag is used). Due to this behavior, it is recommended that when using [`Validators.pattern`](validators#pattern) you **do not** pass in a `RegExp` object with either the global or sticky flag enabled.

```
// Not recommended (since the `g` flag is used)
const controlOne = new FormControl('1', Validators.pattern(/foo/g));

// Good
const controlTwo = new FormControl('1', Validators.pattern(/foo/));
```

### nullValidator

`ValidationErrors | null`

Validator that performs no operation.

@paramcontrol`AbstractControl<any, any, any>`

@returns`ValidationErrors | null`

### compose

2 overloads

Compose multiple validators into a single function that returns the union of the individual error maps for the provided control.

@paramvalidators`null`

@returns`null`

@paramvalidators`(ValidatorFn | null | undefined)[]`

@returns`ValidatorFn | null`

### composeAsync

`AsyncValidatorFn | null`

Compose multiple async validators into a single function that returns the union of the individual error objects for the provided control.

@paramvalidators`(AsyncValidatorFn | null)[]`

@returns`AsyncValidatorFn | null`

## Description

Provides a set of built-in validators that can be used by form controls.

A validator is a function that processes a [`FormControl`](formcontrol) or collection of controls and returns an error map or null. A null map means that validation has passed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/Validators>
