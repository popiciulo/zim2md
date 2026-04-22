# AnimationPlayer

AnimationPlayer



# AnimationPlayer

Provides programmatic control of a reusable animation sequence, built using the `AnimationBuilder.build()` method which returns an [`AnimationFactory`](animationfactory), whose `create()` method instantiates and initializes this interface.

[AnimationBuilder](animationbuilder)[AnimationFactory](animationfactory)[animate](animationplayer#animate)

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationPlayer {
  onDone(fn: () => void): void;
  onStart(fn: () => void): void;
  onDestroy(fn: () => void): void;
  init(): void;
  hasStarted(): boolean;
  play(): void;
  pause(): void;
  restart(): void;
  finish(): void;
  destroy(): void;
  reset(): void;
  setPosition(position: number): void;
  getPosition(): number;
  parentPlayer: AnimationPlayer | null;
  readonly totalTime: number;
  beforeDestroy?: (() => any) | undefined;
}
```

### onDone

`void`

Provides a callback to invoke when the animation finishes.

@paramfn`() => void`

The callback function.

@returns`void`

### onStart

`void`

Provides a callback to invoke when the animation starts.

@paramfn`() => void`

The callback function.

@returns`void`

### onDestroy

`void`

Provides a callback to invoke after the animation is destroyed.

@paramfn`() => void`

The callback function.

@returns`void`

### init

`void`

Initializes the animation.

@returns`void`

### hasStarted

`boolean`

Reports whether the animation has started.

@returns`boolean`

### play

`void`

Runs the animation, invoking the `onStart()` callback.

@returns`void`

### pause

`void`

Pauses the animation.

@returns`void`

### restart

`void`

Restarts the paused animation.

@returns`void`

### finish

`void`

Ends the animation, invoking the `onDone()` callback.

@returns`void`

### destroy

`void`

Destroys the animation, after invoking the `beforeDestroy()` callback. Calls the `onDestroy()` callback when destruction is completed.

@returns`void`

### reset

`void`

Resets the animation to its initial state.

@returns`void`

### setPosition

`void`

Sets the position of the animation.

@paramposition`number`

A fractional value, representing the progress through the animation.

@returns`void`

### getPosition

`number`

Reports the current position of the animation.

@returns`number`

### parentPlayer

`AnimationPlayer | null`

The parent of this player, if any.

### totalTime

`number`

The total run time of the animation, in milliseconds.

### beforeDestroy

`(() => any) | undefined`

Provides a callback to invoke before the animation is destroyed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationPlayer>
