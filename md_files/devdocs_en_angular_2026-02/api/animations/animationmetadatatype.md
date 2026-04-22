# AnimationMetadataType

AnimationMetadataType



# AnimationMetadataType

Constants for the categories of parameters that can be defined for animations.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
enum AnimationMetadataType {
  State: AnimationMetadataType.State;
  Transition: AnimationMetadataType.Transition;
  Sequence: AnimationMetadataType.Sequence;
  Group: AnimationMetadataType.Group;
  Animate: AnimationMetadataType.Animate;
  Keyframes: AnimationMetadataType.Keyframes;
  Style: AnimationMetadataType.Style;
  Trigger: AnimationMetadataType.Trigger;
  Reference: AnimationMetadataType.Reference;
  AnimateChild: AnimationMetadataType.AnimateChild;
  AnimateRef: AnimationMetadataType.AnimateRef;
  Query: AnimationMetadataType.Query;
  Stagger: AnimationMetadataType.Stagger;
}
```

### State

Associates a named animation state with a set of CSS styles. See [`state()`](state)

### Transition

Data for a transition from one animation state to another. See [`transition()`](transition)

### Sequence

Contains a set of animation steps. See [`sequence()`](sequence)

### Group

Contains a set of animation steps. See [`group()`](group)

### Animate

Contains an animation step. See [`animate()`](animate)

### Keyframes

Contains a set of animation steps. See [`keyframes()`](keyframes)

### Style

Contains a set of CSS property-value pairs into a named style. See [`style()`](style)

### Trigger

Associates an animation with an entry trigger that can be attached to an element. See [`trigger()`](trigger)

### Reference

Contains a re-usable animation. See [`animation()`](animation)

### AnimateChild

Contains data to use in executing child animations returned by a query. See [`animateChild()`](animatechild)

### AnimateRef

Contains animation parameters for a re-usable animation. See [`useAnimation()`](useanimation)

### Query

Contains child-animation query data. See [`query()`](query)

### Stagger

Contains data for staggering an animation sequence. See [`stagger()`](stagger)

## Description

Constants for the categories of parameters that can be defined for animations.

A corresponding function defines a set of parameters for each category, and collects them into a corresponding [`AnimationMetadata`](animationmetadata) object.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationMetadataType>
