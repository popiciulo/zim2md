# AnimationGroupMetadata

AnimationGroupMetadata



# AnimationGroupMetadata

Encapsulates an animation group. Instantiated and returned by the [`group()`](group) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationGroupMetadata extends AnimationMetadata {
  steps: AnimationMetadata[];
  options: AnimationOptions | null;
  override type: AnimationMetadataType;
}
```

### steps

`AnimationMetadata[]`

One or more animation or style steps that form this group.

### options

`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation. Default delay is 0.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationGroupMetadata>
