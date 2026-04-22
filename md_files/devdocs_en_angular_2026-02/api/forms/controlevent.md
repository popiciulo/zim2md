# ControlEvent

ControlEvent



# ControlEvent

Base class for every event sent by [`AbstractControl.events()`](abstractcontrol#events)

## API

```
abstract class ControlEvent<T = any> {
  abstract readonly source: AbstractControl<unknown, unknown, any>;
}
```

### source

`AbstractControl<unknown, unknown, any>`

Form control from which this event is originated.

Note: the type of the control can't be infered from T as the event can be emitted by any of child controls

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/ControlEvent>
