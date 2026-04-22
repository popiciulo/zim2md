# group

group



# group

Defines a list of animation steps to be run in parallel.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function group(
  steps: AnimationMetadata[],
  options?: AnimationOptions | null,
): AnimationGroupMetadata;
```

### group

`AnimationGroupMetadata`

Defines a list of animation steps to be run in parallel.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramsteps`AnimationMetadata[]`

An array of animation step objects.

- When steps are defined by [`style()`](style) or [`animate()`](animate) function calls, each call within the group is executed instantly.
- To specify offset styles to be applied at a later time, define steps with [`keyframes()`](keyframes), or use [`animate()`](animate) calls with a delay value. For example:

```
group([
animate("1s", style({ background: "black" })),
animate("2s", style({ color: "white" }))
])
```

@paramoptions`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation.

@returns`AnimationGroupMetadata`

Usage notes

Grouped animations are useful when a series of styles must be animated at different starting times and closed off at different ending times.

When called within a [`sequence()`](sequence) or a [`transition()`](transition) call, does not continue to the next instruction until all of the inner animation steps have completed.

## Usage Notes

Grouped animations are useful when a series of styles must be animated at different starting times and closed off at different ending times.

When called within a [`sequence()`](sequence) or a [`transition()`](transition) call, does not continue to the next instruction until all of the inner animation steps have completed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/group>
