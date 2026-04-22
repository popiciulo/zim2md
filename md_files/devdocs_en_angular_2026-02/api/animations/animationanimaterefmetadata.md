# AnimationAnimateRefMetadata

AnimationAnimateRefMetadata



# AnimationAnimateRefMetadata

Encapsulates a reusable animation. Instantiated and returned by the [`useAnimation()`](useanimation) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationAnimateRefMetadata extends AnimationMetadata {
  animation: AnimationReferenceMetadata;
  options: AnimationOptions | null;
  override type: AnimationMetadataType;
}
```

### animation

`AnimationReferenceMetadata`

An animation reference object.

### options

`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation. Default delay is 0.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationAnimateRefMetadata>
