# AnimationQueryMetadata

AnimationQueryMetadata



# AnimationQueryMetadata

Encapsulates an animation query. Instantiated and returned by the [`query()`](query) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationQueryMetadata extends AnimationMetadata {
  selector: string;
  animation: AnimationMetadata | AnimationMetadata[];
  options: AnimationQueryOptions | null;
  override type: AnimationMetadataType;
}
```

### selector

`string`

The CSS selector for this query.

### animation

`AnimationMetadata | AnimationMetadata[]`

One or more animation step objects.

### options

`AnimationQueryOptions | null`

A query options object.

### type

`AnimationMetadataType`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationQueryMetadata>
