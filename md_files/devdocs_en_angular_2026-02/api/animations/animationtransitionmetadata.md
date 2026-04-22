# AnimationTransitionMetadata

AnimationTransitionMetadata



# AnimationTransitionMetadata

Encapsulates an animation transition. Instantiated and returned by the [`transition()`](transition) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationTransitionMetadata extends AnimationMetadata {
  expr: string | ((fromState: string, toState: string, element?: any, params?: { [key: string]: any; } | undefined) => boolean);
  animation: AnimationMetadata | AnimationMetadata[];
  options: AnimationOptions | null;
  override type: AnimationMetadataType;
}
```

### expr

`string | ((fromState: string, toState: string, element?: any, params?: { [key: string]: any; } | undefined) => boolean)`

An expression that describes a state change.

### animation

`AnimationMetadata | AnimationMetadata[]`

One or more animation objects to which this transition applies.

### options

`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation. Default delay is 0.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationTransitionMetadata>
