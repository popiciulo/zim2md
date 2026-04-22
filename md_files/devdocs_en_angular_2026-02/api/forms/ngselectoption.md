# NgSelectOption

NgSelectOption



# NgSelectOption

Marks `<option>` as dynamic, so Angular can be notified when options change.

[SelectControlValueAccessor](selectcontrolvalueaccessor)

## API

```
class NgSelectOption implements OnDestroy {
  constructor(_element: ElementRef<any>, _renderer: Renderer2, _select: SelectControlValueAccessor): NgSelectOption;
  id: string;
  @Input() set ngValue(value: any);
  @Input() set value(value: any);
}
```

### constructor

`NgSelectOption`

@param\_element`ElementRef<any>`

@param\_renderer`Renderer2`

@param\_select`SelectControlValueAccessor`

@returns`NgSelectOption`

### id

`string`

ID of the option element

### ngValue

`any`

Tracks the value bound to the option element. Unlike the value binding, ngValue supports binding to objects.

### value

`any`

Tracks simple string values bound to the option element. For objects, use the `ngValue` input binding.

## Description

Marks `<option>` as dynamic, so Angular can be notified when options change.

---

## Exported by

- `ReactiveFormsModule`
- `FormsModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/NgSelectOption>
