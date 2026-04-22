# useAnimation

useAnimation



# useAnimation

Starts a reusable animation that is created using the [`animation()`](animation) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function useAnimation(
  animation: AnimationReferenceMetadata,
  options?: AnimationOptions | null,
): AnimationAnimateRefMetadata;
```

### useAnimation

`AnimationAnimateRefMetadata`

Starts a reusable animation that is created using the [`animation()`](animation) function.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramanimation`AnimationReferenceMetadata`

The reusable animation to start.

@paramoptions`AnimationOptions | null`

An options object that can contain a delay value for the start of the animation, and additional override values for developer-defined parameters.

@returns`AnimationAnimateRefMetadata`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/useAnimation>
