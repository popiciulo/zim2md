# TouchedChangeEvent

TouchedChangeEvent



# TouchedChangeEvent

Event fired when the control's touched status changes (touched <=> untouched).

[AbstractControl.events](abstractcontrol#events)

## API

```
class TouchedChangeEvent extends ControlEvent {
  constructor(touched: boolean, source: AbstractControl<any, any, any>): TouchedChangeEvent;
  readonly override touched: boolean;
  readonly override source: AbstractControl<any, any, any>;
}
```

### constructor

`TouchedChangeEvent`

@paramtouched`boolean`

@paramsource`AbstractControl<any, any, any>`

@returns`TouchedChangeEvent`

### touched

`boolean`

### source

`AbstractControl<any, any, any>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/TouchedChangeEvent>
