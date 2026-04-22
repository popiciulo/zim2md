# AnimationStaggerMetadata

AnimationStaggerMetadata



# AnimationStaggerMetadata

Encapsulates parameters for staggering the start times of a set of animation steps. Instantiated and returned by the [`stagger()`](stagger) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationStaggerMetadata extends AnimationMetadata {
  timings: string | number;
  animation: AnimationMetadata | AnimationMetadata[];
  override type: AnimationMetadataType;
}
```

### timings

`string | number`

The timing data for the steps.

### animation

`AnimationMetadata | AnimationMetadata[]`

One or more animation steps.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationStaggerMetadata>
