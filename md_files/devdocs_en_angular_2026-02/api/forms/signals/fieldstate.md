# FieldState

FieldState



# FieldState

Contains all of the state (e.g. value, statuses, etc.) associated with a [`FieldTree`](fieldtree), exposed as signals.

## API

```
interface FieldState<TValue, TKey extends string | number = string | number> extends ɵFieldState<TValue> {
  readonly dirty: Signal<boolean>;
  readonly hidden: Signal<boolean>;
  readonly disabledReasons: Signal<readonly DisabledReason[]>;
  readonly errors: Signal<WithField[]>;
  readonly errorSummary: Signal<WithField[]>;
  readonly valid: Signal<boolean>;
  readonly invalid: Signal<boolean>;
  readonly pending: Signal<boolean>;
  readonly submitting: Signal<boolean>;
  readonly keyInParent: Signal<TKey>;
  readonly fieldBindings: Signal<readonly Field<unknown>[]>;
  metadata<M>(key: AggregateMetadataKey<M, any>): Signal<M>;
  metadata<M>(key: MetadataKey<M>): M | undefined;
  hasMetadata(key: MetadataKey<any> | AggregateMetadataKey<any, any>): boolean;
  reset(value?: TValue | undefined): void;
  readonly override disabled: Signal<boolean>;
  readonly override max?: Signal<number | undefined> | undefined;
  readonly override maxLength?: Signal<number | undefined> | undefined;
  readonly override min?: Signal<number | undefined> | undefined;
  readonly override minLength?: Signal<number | undefined> | undefined;
  readonly override name: Signal<string>;
  readonly override pattern: Signal<readonly RegExp[]>;
  readonly override readonly: Signal<boolean>;
  readonly override required: Signal<boolean>;
  readonly override touched: Signal<boolean>;
  readonly override value: WritableSignal<T>;
  readonly override controlValue: Signal<T>;
  override markAsDirty(): void;
  override markAsTouched(): void;
  override setControlValue(value: T): void;
}
```

### dirty

`Signal<boolean>`

A signal indicating whether field value has been changed by user.

### hidden

`Signal<boolean>`

A signal indicating whether a field is hidden.

When a field is hidden it is ignored when determining the valid, touched, and dirty states.

Note: This doesn't hide the field in the template, that must be done manually.

```
@if (!field.hidden()) {
  ...
}
```

### disabledReasons

`Signal<readonly DisabledReason[]>`

### errors

`Signal<WithField[]>`

### errorSummary

`Signal<WithField[]>`

A signal containing the [`errors`](fieldstate#errors) of the field and its descendants.

### valid

`Signal<boolean>`

A signal indicating whether the field's value is currently valid.

Note: `valid()` is not the same as `!invalid()`.

- `valid()` is `true` when there are no validation errors *and* no pending validators.
- `invalid()` is `true` when there are validation errors, regardless of pending validators.

Ex: consider the situation where a field has 3 validators, 2 of which have no errors and 1 of which is still pending. In this case `valid()` is `false` because of the pending validator. However `invalid()` is also `false` because there are no errors.

### invalid

`Signal<boolean>`

A signal indicating whether the field's value is currently invalid.

Note: `invalid()` is not the same as `!valid()`.

- `invalid()` is `true` when there are validation errors, regardless of pending validators.
- `valid()` is `true` when there are no validation errors *and* no pending validators.

Ex: consider the situation where a field has 3 validators, 2 of which have no errors and 1 of which is still pending. In this case `invalid()` is `false` because there are no errors. However `valid()` is also `false` because of the pending validator.

### pending

`Signal<boolean>`

Whether there are any validators still pending for this field.

### submitting

`Signal<boolean>`

A signal indicating whether the field is currently in the process of being submitted.

### keyInParent

`Signal<TKey>`

The property key in the parent field under which this field is stored. If the parent field is array-valued, for example, this is the index of this field in that array.

### fieldBindings

`Signal<readonly Field<unknown>[]>`

The [`Field`](field) directives that bind this field to a UI control.

### metadata

`Signal<M>`

Reads an aggregate metadata value from the field.

@paramkey`AggregateMetadataKey<M, any>`

The metadata key to read.

@returns`Signal<M>`

### metadata

`M | undefined`

Reads a metadata value from the field.

@paramkey`MetadataKey<M>`

The metadata key to read.

@returns`M | undefined`

### hasMetadata

`boolean`

Checks whether the given metadata key has been defined for this field.

@paramkey`MetadataKey<any> | AggregateMetadataKey<any, any>`

@returns`boolean`

### reset

`void`

Resets the [`touched`](fieldstate#touched) and [`dirty`](fieldstate#dirty) state of the field and its descendants.

Note this does not change the data model, which can be reset directly if desired.

@paramvalue`TValue | undefined`

Optional value to set to the form. If not passed, the value will not be changed.

@returns`void`

### disabled

`Signal<boolean>`

A signal indicating whether the field is currently disabled.

### max

`Signal<number | undefined> | undefined`

A signal indicating the field's maximum value, if applicable.

Applies to `<input>` with a numeric or date `type` attribute and custom controls.

### maxLength

`Signal<number | undefined> | undefined`

A signal indicating the field's maximum string length, if applicable.

Applies to `<input>`, `<textarea>`, and custom controls.

### min

`Signal<number | undefined> | undefined`

A signal indicating the field's minimum value, if applicable.

Applies to `<input>` with a numeric or date `type` attribute and custom controls.

### minLength

`Signal<number | undefined> | undefined`

A signal indicating the field's minimum string length, if applicable.

Applies to `<input>`, `<textarea>`, and custom controls.

### name

`Signal<string>`

A signal of a unique name for the field, by default based on the name of its parent field.

### pattern

`Signal<readonly RegExp[]>`

A signal indicating the patterns the field must match.

### readonly

`Signal<boolean>`

A signal indicating whether the field is currently readonly.

### required

`Signal<boolean>`

A signal indicating whether the field is required.

### touched

`Signal<boolean>`

A signal indicating whether the field has been touched by the user.

### value

`WritableSignal<T>`

A writable signal containing the value for this field.

Updating this signal will update the data model that the field is bound to.

While updates from the UI control are eventually reflected here, they may be delayed if debounced.

### controlValue

`Signal<T>`

A signal containing the value of the control to which this field is bound.

This differs from [`value`](fieldstate#value) in that it's not subject to debouncing, and thus is used to buffer debounced updates from the control to the field. This will also not take into account the [`controlValue`](fieldstate#controlValue) of children.

### markAsDirty

`void`

Sets the dirty status of the field to `true`.

@returns`void`

### markAsTouched

`void`

Sets the touched status of the field to `true`.

@returns`void`

### setControlValue

`void`

Sets [`controlValue`](fieldstate#controlValue) immediately and triggers synchronization to [`value`](fieldstate#value).

@paramvalue`T`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FieldState>
