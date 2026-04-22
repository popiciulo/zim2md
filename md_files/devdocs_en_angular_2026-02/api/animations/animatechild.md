# animateChild

animateChild



# animateChild

Executes a queried inner animation element within an animation sequence.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function animateChild(
  options?: AnimateChildOptions | null,
): AnimationAnimateChildMetadata;
```

### animateChild

`AnimationAnimateChildMetadata`

Executes a queried inner animation element within an animation sequence.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramoptions`AnimateChildOptions | null`

An options object that can contain a delay value for the start of the animation, and additional override values for developer-defined parameters.

@returns`AnimationAnimateChildMetadata`

Usage notes

Each time an animation is triggered in Angular, the parent animation has priority and any child animations are blocked. In order for a child animation to run, the parent animation must query each of the elements containing child animations, and run them using this function.

Note that this feature is designed to be used with [`query()`](query) and it will only work with animations that are assigned using the Angular animation library. CSS keyframes and transitions are not handled by this API.

## Usage Notes

Each time an animation is triggered in Angular, the parent animation has priority and any child animations are blocked. In order for a child animation to run, the parent animation must query each of the elements containing child animations, and run them using this function.

Note that this feature is designed to be used with [`query()`](query) and it will only work with animations that are assigned using the Angular animation library. CSS keyframes and transitions are not handled by this API.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/animateChild>
