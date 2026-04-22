# AnimationStyleMetadata

AnimationStyleMetadata



# AnimationStyleMetadata

Encapsulates an animation style. Instantiated and returned by the [`style()`](style) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationStyleMetadata extends AnimationMetadata {
  styles: "*" | { [key: string]: string | number; } | ("*" | { [key: string]: string | number; })[];
  offset: number | null;
  override type: AnimationMetadataType;
}
```

### styles

`"*" | { [key: string]: string | number; } | ("*" | { [key: string]: string | number; })[]`

A set of CSS style properties.

### offset

`number | null`

A percentage of the total animate time at which the style is to be applied.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationStyleMetadata>
