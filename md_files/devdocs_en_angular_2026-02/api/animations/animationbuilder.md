# AnimationBuilder

AnimationBuilder



# AnimationBuilder

An injectable service that produces an animation sequence programmatically within an Angular component or directive. Provided by the `BrowserAnimationsModule` or `NoopAnimationsModule`.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
abstract class AnimationBuilder {
  abstract build(animation: AnimationMetadata | AnimationMetadata[]): AnimationFactory;
}
```

### build

`AnimationFactory`

Builds a factory for producing a defined animation.

@paramanimation`AnimationMetadata | AnimationMetadata[]`

A reusable animation definition.

@returns`AnimationFactory`

## Usage Notes

To use this service, add it to your component or directive as a dependency. The service is instantiated along with your component.

Apps do not typically need to create their own animation players, but if you do need to, follow these steps:

1. Use the `AnimationBuilder.build()` method to create a programmatic animation. The method returns an [`AnimationFactory`](animationfactory) instance.
2. Use the factory object to create an [`AnimationPlayer`](animationplayer) and attach it to a DOM element.
3. Use the player object to control the animation programmatically.

For example:

```
// import the service from BrowserAnimationsModule
import {AnimationBuilder} from '@angular/animations';
// require the service as a dependency
class MyCmp {
  constructor(private _builder: AnimationBuilder) {}

  makeAnimation(element: any) {
    // first define a reusable animation
    const myAnimation = this._builder.build([
      style({ width: 0 }),
      animate(1000, style({ width: '100px' }))
    ]);

    // use the returned factory object to create a player
    const player = myAnimation.create(element);

    player.play();
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationBuilder>
