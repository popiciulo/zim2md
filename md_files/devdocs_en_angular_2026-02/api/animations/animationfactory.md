# AnimationFactory

AnimationFactory



# AnimationFactory

A factory object returned from the `AnimationBuilder.build()` method.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
abstract class AnimationFactory {
  abstract create(element: any, options?: AnimationOptions | undefined): AnimationPlayer;
}
```

### create

`AnimationPlayer`

Creates an [`AnimationPlayer`](animationplayer) instance for the reusable animation defined by the `AnimationBuilder.build()` method that created this factory and attaches the new player a DOM element.

@paramelement`any`

The DOM element to which to attach the player.

@paramoptions`AnimationOptions | undefined`

A set of options that can include a time delay and additional developer-defined parameters.

@returns`AnimationPlayer`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationFactory>
