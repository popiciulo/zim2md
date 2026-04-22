# AnimationReferenceMetadata

AnimationReferenceMetadata



# AnimationReferenceMetadata

Encapsulates a reusable animation, which is a collection of individual animation steps. Instantiated and returned by the [`animation()`](animation) function, and passed to the [`useAnimation()`](useanimation) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationReferenceMetadata extends AnimationMetadata {
  animation: AnimationMetadata | AnimationMetadata[];
  options: AnimationOptions | null;
  override type: AnimationMetadataType;
}
```

### animation

`AnimationMetadata | AnimationMetadata[]`

One or more animation step objects.

### options

`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation. Default delay is 0.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationReferenceMetadata>
