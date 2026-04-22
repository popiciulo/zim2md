# Field

Field



# Field

Binds a form [`FieldTree`](fieldtree) to a UI control that edits it. A UI control can be one of several things:

1. A native HTML input or textarea
2. A signal forms custom control that implements [`FormValueControl`](formvaluecontrol) or [`FormCheckboxControl`](formcheckboxcontrol)
3. A component that provides a `ControlValueAccessor`. This should only be used for backwards compatibility with reactive forms. Prefer options (1) and (2).

## API

```
class Field<T> implements ɵControl<T> {
  readonly classes: (readonly [string, Signal<boolean>])[];
  readonly @Input() field: InputSignal<FieldTree<T>>;
  readonly state: Signal<[T] extends [AbstractControl] ? CompatFieldState<T, string | number> : FieldState<T, string | number>>;
  protected getOrCreateNgControl(): InteropNgControl;
}
```

### classes

`(readonly [string, Signal<boolean>])[]`

### field

`InputSignal<FieldTree<T>>`

### state

`Signal<[T] extends [AbstractControl] ? CompatFieldState<T, string | number> : FieldState<T, string | number>>`

### getOrCreateNgControl

`InteropNgControl`

Lazily instantiates a fake [`NgControl`](../ngcontrol) for this field.

@returns`InteropNgControl`

## Description

Binds a form [`FieldTree`](fieldtree) to a UI control that edits it. A UI control can be one of several things:

1. A native HTML input or textarea
2. A signal forms custom control that implements [`FormValueControl`](formvaluecontrol) or [`FormCheckboxControl`](formcheckboxcontrol)
3. A component that provides a `ControlValueAccessor`. This should only be used for backwards compatibility with reactive forms. Prefer options (1) and (2).

This directive has several responsibilities:

1. Two-way binds the field's value with the UI control's value
2. Binds additional forms related state on the field to the UI control (disabled, required, etc.)
3. Relays relevant events on the control to the field (e.g. marks field touched on blur)
4. Provides a fake [`NgControl`](../ngcontrol) that implements a subset of the features available on the reactive forms [`NgControl`](../ngcontrol). This is provided to improve interoperability with controls designed to work with reactive forms. It should not be used by controls written for signal forms.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/Field>
