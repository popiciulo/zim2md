# AnimationEvent

AnimationEvent



# AnimationEvent

An instance of this class is returned as an event parameter when an animation callback is captured for an animation either during the start or done phase.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationEvent {
  fromState: string;
  toState: string;
  totalTime: number;
  phaseName: string;
  element: any;
  triggerName: string;
  disabled: boolean;
}
```

### fromState

`string`

The name of the state from which the animation is triggered.

### toState

`string`

The name of the state in which the animation completes.

### totalTime

`number`

The time it takes the animation to complete, in milliseconds.

### phaseName

`string`

The animation phase in which the callback was invoked, one of "start" or "done".

### element

`any`

The element to which the animation is attached.

### triggerName

`string`

Internal.

### disabled

`boolean`

Internal.

## Description

An instance of this class is returned as an event parameter when an animation callback is captured for an animation either during the start or done phase.

```
@Component({
  host: {
    '[@myAnimationTrigger]': 'someExpression',
    '(@myAnimationTrigger.start)': 'captureStartEvent($event)',
    '(@myAnimationTrigger.done)': 'captureDoneEvent($event)',
  },
  animations: [
    trigger("myAnimationTrigger", [
       // ...
    ])
  ]
})
class MyComponent {
  someExpression: any = false;
  captureStartEvent(event: AnimationEvent) {
    // the toState, fromState and totalTime data is accessible from the event variable
  }

  captureDoneEvent(event: AnimationEvent) {
    // the toState, fromState and totalTime data is accessible from the event variable
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationEvent>
