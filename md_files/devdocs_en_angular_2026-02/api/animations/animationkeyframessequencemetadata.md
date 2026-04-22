# AnimationKeyframesSequenceMetadata

AnimationKeyframesSequenceMetadata



# AnimationKeyframesSequenceMetadata

Encapsulates a keyframes sequence. Instantiated and returned by the [`keyframes()`](keyframes) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationKeyframesSequenceMetadata extends AnimationMetadata {
  steps: AnimationStyleMetadata[];
  override type: AnimationMetadataType;
}
```

### steps

`AnimationStyleMetadata[]`

An array of animation styles.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationKeyframesSequenceMetadata>
