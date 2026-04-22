# state

state



# state

Declares an animation state within a trigger attached to an element.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function state(
  name: string,
  styles: AnimationStyleMetadata,
  options?: { params: { [name: string]: any } } | undefined,
): AnimationStateMetadata;
```

### state

`AnimationStateMetadata`

Declares an animation state within a trigger attached to an element.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramname`string`

One or more names for the defined state in a comma-separated string. The following reserved state names can be supplied to define a style for specific use cases:

- `void` You can associate styles with this name to be used when the element is detached from the application. For example, when an `ngIf` evaluates to false, the state of the associated element is void.
- `*` (asterisk) Indicates the default state. You can associate styles with this name to be used as the fallback when the state that is being animated is not declared within the trigger.

@paramstyles`AnimationStyleMetadata`

A set of CSS styles associated with this state, created using the [`style()`](style) function. This set of styles persists on the element once the state has been reached.

@paramoptions`{ params: { [name: string]: any; }; } | undefined`

Parameters that can be passed to the state when it is invoked. 0 or more key-value pairs.

@returns`AnimationStateMetadata`

Usage notes

Use the [`trigger()`](trigger) function to register states to an animation trigger. Use the [`transition()`](transition) function to animate between states. When a state is active within a component, its associated styles persist on the element, even when the animation ends.

## Usage Notes

Use the [`trigger()`](trigger) function to register states to an animation trigger. Use the [`transition()`](transition) function to animate between states. When a state is active within a component, its associated styles persist on the element, even when the animation ends.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/state>
