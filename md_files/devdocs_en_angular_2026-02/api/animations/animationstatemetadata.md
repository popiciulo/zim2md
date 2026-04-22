# AnimationStateMetadata

AnimationStateMetadata



# AnimationStateMetadata

Encapsulates an animation state by associating a state name with a set of CSS styles. Instantiated and returned by the [`state()`](state) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationStateMetadata extends AnimationMetadata {
  name: string;
  styles: AnimationStyleMetadata;
  options?: { params: { [name: string]: any; }; } | undefined;
  override type: AnimationMetadataType;
}
```

### name

`string`

The state name, unique within the component.

### styles

`AnimationStyleMetadata`

The CSS styles associated with this state.

### options

`{ params: { [name: string]: any; }; } | undefined`

An options object containing developer-defined parameters that provide styling defaults and can be overridden on invocation.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationStateMetadata>
