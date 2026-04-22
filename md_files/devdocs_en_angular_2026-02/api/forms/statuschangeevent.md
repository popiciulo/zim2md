# StatusChangeEvent

StatusChangeEvent



# StatusChangeEvent

Event fired when the control's status changes.

[AbstractControl.events](abstractcontrol#events)

## API

```
class StatusChangeEvent extends ControlEvent {
  constructor(status: FormControlStatus, source: AbstractControl<any, any, any>): StatusChangeEvent;
  readonly override status: FormControlStatus;
  readonly override source: AbstractControl<any, any, any>;
}
```

### constructor

`StatusChangeEvent`

@paramstatus`FormControlStatus`

@paramsource`AbstractControl<any, any, any>`

@returns`StatusChangeEvent`

### status

`FormControlStatus`

### source

`AbstractControl<any, any, any>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/StatusChangeEvent>
