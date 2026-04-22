# AnimationAnimateMetadata

AnimationAnimateMetadata



# AnimationAnimateMetadata

Encapsulates an animation step. Instantiated and returned by the [`animate()`](animate) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationAnimateMetadata extends AnimationMetadata {
  timings: string | number | AnimateTimings;
  styles: AnimationStyleMetadata | AnimationKeyframesSequenceMetadata | null;
  override type: AnimationMetadataType;
}
```

### timings

`string | number | AnimateTimings`

The timing data for the step.

### styles

`AnimationStyleMetadata | AnimationKeyframesSequenceMetadata | null`

A set of styles used in the step.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationAnimateMetadata>
