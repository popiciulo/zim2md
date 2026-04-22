# FormUiControl

FormUiControl



# FormUiControl

The base set of properties shared by all form control contracts.

## API

```
interface FormUiControl {
  readonly errors?: InputSignal<readonly WithOptionalField<ValidationError>[]> | InputSignalWithTransform<readonly WithOptionalField<ValidationError>[], unknown> | undefined;
  readonly disabled?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly disabledReasons?: InputSignal<readonly WithOptionalField<DisabledReason>[]> | InputSignalWithTransform<readonly WithOptionalField<DisabledReason>[], unknown> | undefined;
  readonly readonly?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly hidden?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly invalid?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly pending?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly touched?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | ModelSignal<boolean> | OutputRef<boolean> | undefined;
  readonly dirty?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly name?: InputSignal<string> | InputSignalWithTransform<string, unknown> | undefined;
  readonly required?: InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined;
  readonly min?: InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined;
  readonly minLength?: InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined;
  readonly max?: InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined;
  readonly maxLength?: InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined;
  readonly pattern?: InputSignal<readonly RegExp[]> | InputSignalWithTransform<readonly RegExp[], unknown> | undefined;
}
```

### errors

`InputSignal<readonly WithOptionalField<ValidationError>[]> | InputSignalWithTransform<readonly WithOptionalField<ValidationError>[], unknown> | undefined`

An input to receive the errors for the field. If implemented, the [`Field`](field) directive will automatically bind errors from the bound field to this input.

### disabled

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the disabled status for the field. If implemented, the [`Field`](field) directive will automatically bind the disabled status from the bound field to this input.

### disabledReasons

`InputSignal<readonly WithOptionalField<DisabledReason>[]> | InputSignalWithTransform<readonly WithOptionalField<DisabledReason>[], unknown> | undefined`

An input to receive the reasons for the disablement of the field. If implemented, the [`Field`](field) directive will automatically bind the disabled reason from the bound field to this input.

### readonly

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the readonly status for the field. If implemented, the [`Field`](field) directive will automatically bind the readonly status from the bound field to this input.

### hidden

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the hidden status for the field. If implemented, the [`Field`](field) directive will automatically bind the hidden status from the bound field to this input.

### invalid

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the invalid status for the field. If implemented, the [`Field`](field) directive will automatically bind the invalid status from the bound field to this input.

### pending

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the pending status for the field. If implemented, the [`Field`](field) directive will automatically bind the pending status from the bound field to this input.

### touched

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | ModelSignal<boolean> | OutputRef<boolean> | undefined`

An input to receive the touched status for the field. If implemented, the [`Field`](field) directive will automatically bind the touched status from the bound field to this input.

### dirty

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the dirty status for the field. If implemented, the [`Field`](field) directive will automatically bind the dirty status from the bound field to this input.

### name

`InputSignal<string> | InputSignalWithTransform<string, unknown> | undefined`

An input to receive the name for the field. If implemented, the [`Field`](field) directive will automatically bind the name from the bound field to this input.

### required

`InputSignal<boolean> | InputSignalWithTransform<boolean, unknown> | undefined`

An input to receive the required status for the field. If implemented, the [`Field`](field) directive will automatically bind the required status from the bound field to this input.

### min

`InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined`

An input to receive the min value for the field. If implemented, the [`Field`](field) directive will automatically bind the min value from the bound field to this input.

### minLength

`InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined`

An input to receive the min length for the field. If implemented, the [`Field`](field) directive will automatically bind the min length from the bound field to this input.

### max

`InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined`

An input to receive the max value for the field. If implemented, the [`Field`](field) directive will automatically bind the max value from the bound field to this input.

### maxLength

`InputSignal<number | undefined> | InputSignalWithTransform<number | undefined, unknown> | undefined`

An input to receive the max length for the field. If implemented, the [`Field`](field) directive will automatically bind the max length from the bound field to this input.

### pattern

`InputSignal<readonly RegExp[]> | InputSignalWithTransform<readonly RegExp[], unknown> | undefined`

An input to receive the value patterns for the field. If implemented, the [`Field`](field) directive will automatically bind the value patterns from the bound field to this input.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FormUiControl>
