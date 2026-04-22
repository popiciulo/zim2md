# ControlValueAccessor

ControlValueAccessor



# ControlValueAccessor

Defines an interface that acts as a bridge between the Angular forms API and a native element in the DOM.

[DefaultValueAccessor](defaultvalueaccessor)

## API

```
interface ControlValueAccessor {
  writeValue(obj: any): void;
  registerOnChange(fn: any): void;
  registerOnTouched(fn: any): void;
  optional setDisabledState(isDisabled: boolean): void;
}
```

### writeValue

`void`

Writes a new value to the element.

This method is called by the forms API to write to the view when programmatic changes from model to view are requested.

@paramobj`any`

The new value for the element

@returns`void`

Usage notes

### Write a value to the element

The following example writes a value to the native DOM element.

```
writeValue(value: any): void {
  this._renderer.setProperty(this._elementRef.nativeElement, 'value', value);
}
```

### registerOnChange

`void`

Registers a callback function that is called when the control's value changes in the UI.

This method is called by the forms API on initialization to update the form model when values propagate from the view to the model.

When implementing the `registerOnChange` method in your own value accessor, save the given function so your class calls it at the appropriate time.

@paramfn`any`

The callback function to register

@returns`void`

Usage notes

### Store the change function

The following example stores the provided function as an internal method.

```
registerOnChange(fn: (_: any) => void): void {
  this._onChange = fn;
}
```

When the value changes in the UI, call the registered function to allow the forms API to update itself:

```
host: {
   '(change)': '_onChange($event.target.value)'
}
```

### registerOnTouched

`void`

Registers a callback function that is called by the forms API on initialization to update the form model on blur.

When implementing `registerOnTouched` in your own value accessor, save the given function so your class calls it when the control should be considered blurred or "touched".

@paramfn`any`

The callback function to register

@returns`void`

Usage notes

### Store the callback function

The following example stores the provided function as an internal method.

```
registerOnTouched(fn: any): void {
  this._onTouched = fn;
}
```

On blur (or equivalent), your class should call the registered function to allow the forms API to update itself:

```
host: {
   '(blur)': '_onTouched()'
}
```

### setDisabledState

`void`

Function that is called by the forms API when the control status changes to or from 'DISABLED'. Depending on the status, it enables or disables the appropriate DOM element.

@paramisDisabled`boolean`

The disabled status to set on the element

@returns`void`

Usage notes

The following is an example of writing the disabled property to a native DOM element:

```
setDisabledState(isDisabled: boolean): void {
  this._renderer.setProperty(this._elementRef.nativeElement, 'disabled', isDisabled);
}
```

## Description

Defines an interface that acts as a bridge between the Angular forms API and a native element in the DOM.

Implement this interface to create a custom form control directive that integrates with Angular forms.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/ControlValueAccessor>
