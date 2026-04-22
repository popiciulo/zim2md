# PristineChangeEvent

PristineChangeEvent



# PristineChangeEvent

Event fired when the control's pristine state changes (pristine <=> dirty).

[AbstractControl.events](abstractcontrol#events)

## API

```
class PristineChangeEvent extends ControlEvent {
  constructor(pristine: boolean, source: AbstractControl<any, any, any>): PristineChangeEvent;
  readonly override pristine: boolean;
  readonly override source: AbstractControl<any, any, any>;
}
```

### constructor

`PristineChangeEvent`

@parampristine`boolean`

@paramsource`AbstractControl<any, any, any>`

@returns`PristineChangeEvent`

### pristine

`boolean`

### source

`AbstractControl<any, any, any>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/PristineChangeEvent>
