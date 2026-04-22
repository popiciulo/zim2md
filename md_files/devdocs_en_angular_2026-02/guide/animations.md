# Animating your applications with animate.enter and animate.leave

Animating your applications with animate.enter and animate.leave



# Animating your applications with `animate.enter` and `animate.leave`

  

Well-designed animations can make your application more fun and straightforward to use, but they aren't just cosmetic. Animations can improve your application and user experience in a number of ways:

- Without animations, web page transitions can seem abrupt and jarring
- Motion greatly enhances the user experience, so animations give users a chance to detect the application's response to their actions
- Good animations can smoothly direct the user's attention throughout a workflow

Angular provides `animate.enter` and `animate.leave` to animate your application's elements. These two features apply enter and leave CSS classes at the appropriate times or call functions to apply animations from third party libraries. `animate.enter` and `animate.leave` are not directives. They are special API supported directly by the Angular compiler. They can be used on elements directly and can also be used as a host binding.

## animate.enter

You can use `animate.enter` to animate elements as they *enter* the DOM. You can define enter animations using CSS classes with either transitions or keyframe animations.

```
import {Component, signal} from '@angular/core';

@Component({
  selector: 'app-enter',
  templateUrl: 'enter.html',
  styleUrls: ['enter.css'],
})
export class Enter {
  isShown = signal(false);

  toggle() {
    this.isShown.update((isShown) => !isShown);
  }
}
```

```
<h2><code>animate.enter</code> Example</h2>

<button type="button" (click)="toggle()">Toggle Element</button>

@if (isShown()) {
  <div class="enter-container" animate.enter="enter-animation">
    <p>The box is entering.</p>
  </div>
}
```

```
:host {
  display: block;
  height: 200px;
}

.enter-container {
  border: 1px solid #dddddd;
  margin-top: 1em;
  padding: 20px 20px 0px 20px;
  font-weight: bold;
  font-size: 20px;
}

.enter-animation {
  animation: slide-fade 1s;
}

@keyframes slide-fade {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

When the animation completes, Angular removes the class or classes that you specified in `animate.enter` from the DOM. Animation classes are only be present while the animation is active.

**NOTE:** When using multiple keyframe animations or transition properties on an element, Angular removes all classes only *after* the longest animation has completed.

You can use `animate.enter` with any other Angular features, such as control flow or dynamic expressions. `animate.enter` accepts both a single class string (with multiple classes separated by spaces), or an array of class strings.

A quick note about using CSS transitions: If you choose to use transitions instead of keyframe animations, the classes added to the element with `animate.enter` represent the state that the transition will animate *to*. Your base element CSS is what the element will look like when no animations run, which is likely similar to the end state of the CSS transition. So you would still need to pair it with `@starting-style` to have an appropriate *from* state for your transition to work.

```
import {Component, signal} from '@angular/core';

@Component({
  selector: 'app-enter-binding',
  templateUrl: 'enter-binding.html',
  styleUrls: ['enter-binding.css'],
})
export class EnterBinding {
  isShown = signal(false);

  toggle() {
    this.isShown.update((isShown) => !isShown);
  }

  enterClass = signal('enter-animation');
}
```

```
<h2><code>animate.enter</code> Binding Example</h2>

<button type="button" (click)="toggle()">Toggle Element</button>

@if (isShown()) {
  <div class="enter-container" [animate.enter]="enterClass()">
    <p>The box is entering.</p>
  </div>
}
```

```
:host {
  display: block;
  height: 200px;
}

.enter-container {
  border: 1px solid #dddddd;
  margin-top: 1em;
  padding: 20px 20px 0px 20px;
  font-weight: bold;
  font-size: 20px;
}

.enter-animation {
  animation: slide-fade 1s;
}

@keyframes slide-fade {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## animate.leave

You can use `animate.leave` to animate elements as they *leave* the DOM. You can define leave animations using CSS classes with either transforms or keyframe animations.

```
import {Component, signal} from '@angular/core';

@Component({
  selector: 'app-leave',
  templateUrl: 'leave.html',
  styleUrls: ['leave.css'],
})
export class Leave {
  isShown = signal(false);

  toggle() {
    this.isShown.update((isShown) => !isShown);
  }
}
```

```
<h2><code>animate.leave</code> Example</h2>

<button type="button" (click)="toggle()">Toggle Element</button>

@if (isShown()) {
  <div class="leave-container" animate.leave="leaving">
    <p>Goodbye</p>
  </div>
}
```

```
:host {
  display: block;
  height: 200px;
}

.leave-container {
  border: 1px solid #dddddd;
  margin-top: 1em;
  padding: 20px 20px 0px 20px;
  font-weight: bold;
  font-size: 20px;
  opacity: 1;
  transition: opacity 200ms ease-in;

  @starting-style {
    opacity: 0;
  }
}

.leaving {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 500ms ease-out, transform 500ms ease-out;
}
```

When the animation completes, Angular automatically removes the animated element from the DOM.

**NOTE:** When using multiple keyframe animations or transition properties on a an element, Angular waits to remove the element only *after* the longest of those animations has completed.

`animate.leave` can also be used with signals, and other bindings. You can use `animate.leave` with a single class or multiple classes. Either specify it as a simple string with spaces or a string array.

```
import {Component, signal} from '@angular/core';

@Component({
  selector: 'app-leave-binding',
  templateUrl: 'leave-binding.html',
  styleUrls: ['leave-binding.css'],
})
export class LeaveBinding {
  isShown = signal(false);

  toggle() {
    this.isShown.update((isShown) => !isShown);
  }

  farewell = signal('leaving');
}
```

```
<h2><code>animate.leave</code> Binding Example</h2>

<button type="button" (click)="toggle()">Toggle Element</button>

@if (isShown()) {
  <div class="leave-container" [animate.leave]="farewell()">
    <p>Goodbye</p>
  </div>
}
```

```
:host {
  display: block;
  height: 200px;
}

.leave-container {
  border: 1px solid #dddddd;
  margin-top: 1em;
  padding: 20px 20px 0px 20px;
  font-weight: bold;
  font-size: 20px;
  opacity: 1;
  transition: opacity 200ms ease-in;

  @starting-style {
    opacity: 0;
  }
}

.leaving {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 500ms ease-out, transform 500ms ease-out;
}
```

## Event Bindings, Functions, and Third-party Libraries

Both `animate.enter` and `animate.leave` support event binding syntax that allows for function calls. You can use this syntax to call a function in your component code or utilize third-party animation libraries, like [GSAP](https://gsap.com/), [anime.js](https://animejs.com/), or any other JavaScript animation library.

```
import {AnimationCallbackEvent, Component, signal} from '@angular/core';

@Component({
  selector: 'app-leave-binding',
  templateUrl: 'leave-event.html',
  styleUrls: ['leave-event.css'],
})
export class LeaveEvent {
  isShown = signal(false);

  toggle() {
    this.isShown.update((isShown) => !isShown);
  }

  leavingFn(event: AnimationCallbackEvent) {
    // Example of calling GSAP
    // gsap.to(event.target, {
    //   duration: 1,
    //   x: 100,
    //   // arrow functions are handy for concise callbacks
    //   onComplete: () => event.animationComplete()
    // });
    event.animationComplete();
  }
}
```

```
<h2><code>animate.leave</code> Function Example</h2>

<button type="button" (click)="toggle()">Toggle Element</button>

@if (isShown()) {
  <div class="leave-container" (animate.leave)="leavingFn($event)">
    <p>Goodbye</p>
  </div>
}
```

```
:host {
  display: block;
  height: 200px;
}

.leave-container {
  border: 1px solid #dddddd;
  margin-top: 1em;
  padding: 20px 20px 0px 20px;
  font-weight: bold;
  font-size: 20px;
  opacity: 1;
  transition: opacity 200ms ease-in;

  @starting-style {
    opacity: 0;
  }
}

.leaving {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 500ms ease-out, transform 500ms ease-out;
}
```

The `$event` object has the type [`AnimationCallbackEvent`](../api/core/animationcallbackevent). It includes the element as the `target` and provides an `animationComplete()` function to notify the framework when the animation finishes.

**IMPORTANT:** You **must** call the `animationComplete()` function when using `animate.leave` for Angular to remove the element.

If you don't call `animationComplete()` when using `animate.leave`, Angular calls the function automatically after a four-second delay. You can configure the duration of the delay by providing the token [`MAX_ANIMATION_TIMEOUT`](../api/core/max_animation_timeout) in milliseconds.

```
  { provide: MAX_ANIMATION_TIMEOUT, useValue: 6000 }
```

## Compatibility with Legacy Angular Animations

You cannot use legacy animations alongside `animate.enter` and `animate.leave` within the same component. Doing so would result in enter classes remaining on the element or leaving nodes not being removed. It is otherwise fine to use both legacy animations and the new `animate.enter` and `animate.leave` animations within the same *application*. The only caveat is content projection. If you are projecting content from one component with legacy animations into another component with `animate.enter` or `animate.leave`, or vice versa, this will result in the same behavior as if they are used together in the same component. This is not supported.

## Testing

TestBed provides built-in support for enabling or disabling animations in your test environment. CSS animations require a browser to run, and many of the APIs are not available in a test environment. By default, TestBed disables animations for you in your test environments.

If you want to test that the animations are animating in a browser test, for example an end-to-end test, you can configure TestBed to enable animations by specifying `animationsEnabled: true` in your test configuration.

```
  TestBed.configureTestingModule({animationsEnabled: true});
```

This will configure animations in your test environment to behave normally.

**NOTE:** Some test environments do not emit animation events like `animationstart`, `animationend` and their transition event equivalents.

## More on Angular animations

You might also be interested in the following:

  [Complex Animations with CSS](animations/css)   [Route transition animations](routing/route-transition-animations)  

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/animations>
