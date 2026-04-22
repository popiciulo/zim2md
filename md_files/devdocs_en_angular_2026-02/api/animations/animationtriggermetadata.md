# AnimationTriggerMetadata

AnimationTriggerMetadata



# AnimationTriggerMetadata

Contains an animation trigger. Instantiated and returned by the [`trigger()`](trigger) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationTriggerMetadata extends AnimationMetadata {
  name: string;
  definitions: AnimationMetadata[];
  options: { params?: { [name: string]: any; } | undefined; } | null;
  override type: AnimationMetadataType;
}
```

### name

`string`

The trigger name, used to associate it with an element. Unique within the component.

### definitions

`AnimationMetadata[]`

An animation definition object, containing an array of state and transition declarations.

### options

`{ params?: { [name: string]: any; } | undefined; } | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation. Default delay is 0.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationTriggerMetadata>
