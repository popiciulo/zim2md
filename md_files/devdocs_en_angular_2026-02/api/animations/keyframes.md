# keyframes

keyframes



# keyframes

Defines a set of animation styles, associating each style with an optional `offset` value.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function keyframes(
  steps: AnimationStyleMetadata[],
): AnimationKeyframesSequenceMetadata;
```

### keyframes

`AnimationKeyframesSequenceMetadata`

Defines a set of animation styles, associating each style with an optional `offset` value.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramsteps`AnimationStyleMetadata[]`

A set of animation styles with optional offset data. The optional `offset` value for a style specifies a percentage of the total animation time at which that style is applied.

@returns`AnimationKeyframesSequenceMetadata`

Usage notes

Use with the [`animate()`](animate) call. Instead of applying animations from the current state to the destination state, keyframes describe how each style entry is applied and at what point within the animation arc. Compare [CSS Keyframe Animations](https://www.w3schools.com/css/css3_animations.asp).

### Usage

In the following example, the offset values describe when each `backgroundColor` value is applied. The color is red at the start, and changes to blue when 20% of the total time has elapsed.

```
// the provided offset values
animate("5s", keyframes([
  style({ backgroundColor: "red", offset: 0 }),
  style({ backgroundColor: "blue", offset: 0.2 }),
  style({ backgroundColor: "orange", offset: 0.3 }),
  style({ backgroundColor: "black", offset: 1 })
]))
```

If there are no `offset` values specified in the style entries, the offsets are calculated automatically.

```
animate("5s", keyframes([
  style({ backgroundColor: "red" }) // offset = 0
  style({ backgroundColor: "blue" }) // offset = 0.33
  style({ backgroundColor: "orange" }) // offset = 0.66
  style({ backgroundColor: "black" }) // offset = 1
]))
```

## Usage Notes

Use with the [`animate()`](animate) call. Instead of applying animations from the current state to the destination state, keyframes describe how each style entry is applied and at what point within the animation arc. Compare [CSS Keyframe Animations](https://www.w3schools.com/css/css3_animations.asp).

### Usage

In the following example, the offset values describe when each `backgroundColor` value is applied. The color is red at the start, and changes to blue when 20% of the total time has elapsed.

```
// the provided offset values
animate("5s", keyframes([
  style({ backgroundColor: "red", offset: 0 }),
  style({ backgroundColor: "blue", offset: 0.2 }),
  style({ backgroundColor: "orange", offset: 0.3 }),
  style({ backgroundColor: "black", offset: 1 })
]))
```

If there are no `offset` values specified in the style entries, the offsets are calculated automatically.

```
animate("5s", keyframes([
  style({ backgroundColor: "red" }) // offset = 0
  style({ backgroundColor: "blue" }) // offset = 0.33
  style({ backgroundColor: "orange" }) // offset = 0.66
  style({ backgroundColor: "black" }) // offset = 1
]))
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/keyframes>
