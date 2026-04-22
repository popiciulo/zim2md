# transition

transition



# transition

Declares an animation transition which is played when a certain specified condition is met.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function transition(
  stateChangeExpr:
    | string
    | ((
        fromState: string,
        toState: string,
        element?: any,
        params?: { [key: string]: any } | undefined,
      ) => boolean),
  steps: AnimationMetadata | AnimationMetadata[],
  options?: AnimationOptions | null,
): AnimationTransitionMetadata;
```

### transition

`AnimationTransitionMetadata`

Declares an animation transition which is played when a certain specified condition is met.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramstateChangeExpr`string | ((fromState: string, toState: string, element?: any, params?: { [key: string]: any; } | undefined) => boolean)`

A string with a specific format or a function that specifies when the animation transition should occur (see [State Change Expression](#state-change-expression)).

@paramsteps`AnimationMetadata | AnimationMetadata[]`

One or more animation objects that represent the animation's instructions.

@paramoptions`AnimationOptions | null`

An options object that can be used to specify a delay for the animation or provide custom parameters for it.

@returns`AnimationTransitionMetadata`

Usage notes

### State Change Expression

The State Change Expression instructs Angular when to run the transition's animations, it can either be

- a string with a specific syntax
- or a function that compares the previous and current state (value of the expression bound to the element's trigger) and returns `true` if the transition should occur or `false` otherwise

The string format can be:

- `fromState => toState`, which indicates that the transition's animations should occur then the expression bound to the trigger's element goes from `fromState` to `toState`

  *Example:*

  ```
      transition('open => closed', animate('.5s ease-out', style({ height: 0 }) ))
  ```
- `fromState <=> toState`, which indicates that the transition's animations should occur then the expression bound to the trigger's element goes from `fromState` to `toState` or vice versa

  *Example:*

  ```
      transition('enabled <=> disabled', animate('1s cubic-bezier(0.8,0.3,0,1)'))
  ```
- `:enter`/`:leave`, which indicates that the transition's animations should occur when the element enters or exists the DOM

  *Example:*

  ```
      transition(':enter', [
        style({ opacity: 0 }),
        animate('500ms', style({ opacity: 1 }))
      ])
  ```
- `:increment`/`:decrement`, which indicates that the transition's animations should occur when the numerical expression bound to the trigger's element has increased in value or decreased

  *Example:*

  ```
      transition(':increment', query('@counter', animateChild()))
  ```
- a sequence of any of the above divided by commas, which indicates that transition's animations should occur whenever one of the state change expressions matches

  *Example:*

  ```
      transition(':increment, * => enabled, :enter', animate('1s ease', keyframes([
        style({ transform: 'scale(1)', offset: 0}),
        style({ transform: 'scale(1.1)', offset: 0.7}),
        style({ transform: 'scale(1)', offset: 1})
      ]))),
  ```

Also note that in such context:

- `void` can be used to indicate the absence of the element
- asterisks can be used as wildcards that match any state
- (as a consequence of the above, `void => *` is equivalent to `:enter` and `* => void` is equivalent to `:leave`)
- `true` and `false` also match expression values of `1` and `0` respectively (but do not match *truthy* and *falsy* values)

Be careful about entering end leaving elements as their transitions present a common pitfall for developers.

Note that when an element with a trigger enters the DOM its `:enter` transition always gets executed, but its `:leave` transition will not be executed if the element is removed alongside its parent (as it will be removed "without warning" before its transition has a chance to be executed, the only way that such transition can occur is if the element is exiting the DOM on its own).

### Animating to a Final State

If the final step in a transition is a call to [`animate()`](animate) that uses a timing value with no `style` data, that step is automatically considered the final animation arc, for the element to reach the final state, in such case Angular automatically adds or removes CSS styles to ensure that the element is in the correct final state.

### Usage Examples

- Transition animations applied based on the trigger's expression value

```
  <div [@myAnimationTrigger]="myStatusExp">
   ...
  </div>
```

```
  trigger("myAnimationTrigger", [
    ..., // states
    transition("on => off, open => closed", animate(500)),
    transition("* <=> error", query('.indicator', animateChild()))
  ])
```

- Transition animations applied based on custom logic dependent on the trigger's expression value and provided parameters

  ```
  <div [@myAnimationTrigger]="{
   value: stepName,
   params: { target: currentTarget }
  }">
   ...
  </div>
  ```

  ```
  trigger("myAnimationTrigger", [
    ..., // states
    transition(
      (fromState, toState, _element, params) =>
        ['firststep', 'laststep'].includes(fromState.toLowerCase())
        && toState === params?.['target'],
      animate('1s')
    )
  ])
  ```

## Usage Notes

### State Change Expression

The State Change Expression instructs Angular when to run the transition's animations, it can either be

- a string with a specific syntax
- or a function that compares the previous and current state (value of the expression bound to the element's trigger) and returns `true` if the transition should occur or `false` otherwise

The string format can be:

- `fromState => toState`, which indicates that the transition's animations should occur then the expression bound to the trigger's element goes from `fromState` to `toState`

  *Example:*

  ```
      transition('open => closed', animate('.5s ease-out', style({ height: 0 }) ))
  ```
- `fromState <=> toState`, which indicates that the transition's animations should occur then the expression bound to the trigger's element goes from `fromState` to `toState` or vice versa

  *Example:*

  ```
      transition('enabled <=> disabled', animate('1s cubic-bezier(0.8,0.3,0,1)'))
  ```
- `:enter`/`:leave`, which indicates that the transition's animations should occur when the element enters or exists the DOM

  *Example:*

  ```
      transition(':enter', [
        style({ opacity: 0 }),
        animate('500ms', style({ opacity: 1 }))
      ])
  ```
- `:increment`/`:decrement`, which indicates that the transition's animations should occur when the numerical expression bound to the trigger's element has increased in value or decreased

  *Example:*

  ```
      transition(':increment', query('@counter', animateChild()))
  ```
- a sequence of any of the above divided by commas, which indicates that transition's animations should occur whenever one of the state change expressions matches

  *Example:*

  ```
      transition(':increment, * => enabled, :enter', animate('1s ease', keyframes([
        style({ transform: 'scale(1)', offset: 0}),
        style({ transform: 'scale(1.1)', offset: 0.7}),
        style({ transform: 'scale(1)', offset: 1})
      ]))),
  ```

Also note that in such context:

- `void` can be used to indicate the absence of the element
- asterisks can be used as wildcards that match any state
- (as a consequence of the above, `void => *` is equivalent to `:enter` and `* => void` is equivalent to `:leave`)
- `true` and `false` also match expression values of `1` and `0` respectively (but do not match *truthy* and *falsy* values)

Be careful about entering end leaving elements as their transitions present a common pitfall for developers.

Note that when an element with a trigger enters the DOM its `:enter` transition always gets executed, but its `:leave` transition will not be executed if the element is removed alongside its parent (as it will be removed "without warning" before its transition has a chance to be executed, the only way that such transition can occur is if the element is exiting the DOM on its own).

### Animating to a Final State

If the final step in a transition is a call to [`animate()`](animate) that uses a timing value with no `style` data, that step is automatically considered the final animation arc, for the element to reach the final state, in such case Angular automatically adds or removes CSS styles to ensure that the element is in the correct final state.

### Usage Examples

- Transition animations applied based on the trigger's expression value

```
  <div [@myAnimationTrigger]="myStatusExp">
   ...
  </div>
```

```
  trigger("myAnimationTrigger", [
    ..., // states
    transition("on => off, open => closed", animate(500)),
    transition("* <=> error", query('.indicator', animateChild()))
  ])
```

- Transition animations applied based on custom logic dependent on the trigger's expression value and provided parameters

  ```
  <div [@myAnimationTrigger]="{
   value: stepName,
   params: { target: currentTarget }
  }">
   ...
  </div>
  ```

  ```
  trigger("myAnimationTrigger", [
    ..., // states
    transition(
      (fromState, toState, _element, params) =>
        ['firststep', 'laststep'].includes(fromState.toLowerCase())
        && toState === params?.['target'],
      animate('1s')
    )
  ])
  ```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/transition>
