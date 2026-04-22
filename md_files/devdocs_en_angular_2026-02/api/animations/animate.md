# animate

animate



# animate

Defines an animation step that combines styling information with timing information.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function animate(
  timings: string | number,
  styles?: AnimationStyleMetadata | AnimationKeyframesSequenceMetadata | null,
): AnimationAnimateMetadata;
```

### animate

`AnimationAnimateMetadata`

Defines an animation step that combines styling information with timing information.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramtimings`string | number`

Sets [`AnimateTimings`](animatetimings) for the parent animation. A string in the format "duration [delay] [easing]".

- Duration and delay are expressed as a number and optional time unit, such as "1s" or "10ms" for one second and 10 milliseconds, respectively. The default unit is milliseconds.
- The easing value controls how the animation accelerates and decelerates during its runtime. Value is one of `ease`, `ease-in`, `ease-out`, `ease-in-out`, or a `cubic-bezier()` function call. If not supplied, no easing is applied.

For example, the string "1s 100ms ease-out" specifies a duration of 1000 milliseconds, and delay of 100 ms, and the "ease-out" easing style, which decelerates near the end of the duration.

@paramstyles`AnimationStyleMetadata | AnimationKeyframesSequenceMetadata | null`

Sets AnimationStyles for the parent animation. A function call to either [`style()`](style) or [`keyframes()`](keyframes) that returns a collection of CSS style entries to be applied to the parent animation. When null, uses the styles from the destination state. This is useful when describing an animation step that will complete an animation; see "Animating to the final state" in `transitions()`.

@returns`AnimationAnimateMetadata`

Usage notes

Call within an animation [`sequence()`](sequence), [`group()`](group), or [`transition()`](transition) call to specify an animation step that applies given style data to the parent animation for a given amount of time.

### Syntax Examples

**Timing examples**

The following examples show various `timings` specifications.

- `animate(500)` : Duration is 500 milliseconds.
- `animate("1s")` : Duration is 1000 milliseconds.
- `animate("100ms 0.5s")` : Duration is 100 milliseconds, delay is 500 milliseconds.
- `animate("5s ease-in")` : Duration is 5000 milliseconds, easing in.
- `animate("5s 10ms cubic-bezier(.17,.67,.88,.1)")` : Duration is 5000 milliseconds, delay is 10 milliseconds, easing according to a bezier curve.

**Style examples**

The following example calls [`style()`](style) to set a single CSS style.

```
animate(500, style({ background: "red" }))
```

The following example calls [`keyframes()`](keyframes) to set a CSS style to different values for successive keyframes.

```
animate(500, keyframes(
 [
  style({ background: "blue" }),
  style({ background: "red" })
 ])
```

## Usage Notes

Call within an animation [`sequence()`](sequence), [`group()`](group), or [`transition()`](transition) call to specify an animation step that applies given style data to the parent animation for a given amount of time.

### Syntax Examples

**Timing examples**

The following examples show various `timings` specifications.

- `animate(500)` : Duration is 500 milliseconds.
- `animate("1s")` : Duration is 1000 milliseconds.
- `animate("100ms 0.5s")` : Duration is 100 milliseconds, delay is 500 milliseconds.
- `animate("5s ease-in")` : Duration is 5000 milliseconds, easing in.
- `animate("5s 10ms cubic-bezier(.17,.67,.88,.1)")` : Duration is 5000 milliseconds, delay is 10 milliseconds, easing according to a bezier curve.

**Style examples**

The following example calls [`style()`](style) to set a single CSS style.

```
animate(500, style({ background: "red" }))
```

The following example calls [`keyframes()`](keyframes) to set a CSS style to different values for successive keyframes.

```
animate(500, keyframes(
 [
  style({ background: "blue" }),
  style({ background: "red" })
 ])
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/animate>
