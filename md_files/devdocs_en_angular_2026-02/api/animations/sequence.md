# sequence

sequence



# sequence

Defines a list of animation steps to be run sequentially, one by one.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function sequence(
  steps: AnimationMetadata[],
  options?: AnimationOptions | null,
): AnimationSequenceMetadata;
```

### sequence

`AnimationSequenceMetadata`

Defines a list of animation steps to be run sequentially, one by one.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramsteps`AnimationMetadata[]`

An array of animation step objects.

- Steps defined by [`style()`](style) calls apply the styling data immediately.
- Steps defined by [`animate()`](animate) calls apply the styling data over time as specified by the timing data.

```
sequence([
style({ opacity: 0 }),
animate("1s", style({ opacity: 1 }))
])
```

@paramoptions`AnimationOptions | null`

An options object containing a delay and developer-defined parameters that provide styling defaults and can be overridden on invocation.

@returns`AnimationSequenceMetadata`

Usage notes

When you pass an array of steps to a [`transition()`](transition) call, the steps run sequentially by default. Compare this to the [`group()`](group) call, which runs animation steps in parallel.

When a sequence is used within a [`group()`](group) or a [`transition()`](transition) call, execution continues to the next instruction only after each of the inner animation steps have completed.

## Usage Notes

When you pass an array of steps to a [`transition()`](transition) call, the steps run sequentially by default. Compare this to the [`group()`](group) call, which runs animation steps in parallel.

When a sequence is used within a [`group()`](group) or a [`transition()`](transition) call, execution continues to the next instruction only after each of the inner animation steps have completed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/sequence>
