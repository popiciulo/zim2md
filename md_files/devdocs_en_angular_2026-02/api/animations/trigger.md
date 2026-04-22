# trigger

trigger



# trigger

Creates a named animation trigger, containing a list of [`state()`](state) and [`transition()`](transition) entries to be evaluated when the expression bound to the trigger changes.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function trigger(
  name: string,
  definitions: AnimationMetadata[],
): AnimationTriggerMetadata;
```

### trigger

`AnimationTriggerMetadata`

Creates a named animation trigger, containing a list of [`state()`](state) and [`transition()`](transition) entries to be evaluated when the expression bound to the trigger changes.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramname`string`

An identifying string.

@paramdefinitions`AnimationMetadata[]`

An animation definition object, containing an array of [`state()`](state) and [`transition()`](transition) declarations.

@returns`AnimationTriggerMetadata`

Usage notes

Define an animation trigger in the `animations` section of `@Component` metadata. In the template, reference the trigger by name and bind it to a trigger expression that evaluates to a defined animation state, using the following format:

`[@triggerName]="expression"`

Animation trigger bindings convert all values to strings, and then match the previous and current values against any linked transitions. Booleans can be specified as `1` or `true` and `0` or `false`.

### Usage Example

The following example creates an animation trigger reference based on the provided name value. The provided animation value is expected to be an array consisting of state and transition declarations.

```
@Component({
  selector: "my-component",
  templateUrl: "my-component-tpl.html",
  animations: [
    trigger("myAnimationTrigger", [
      state(...),
      state(...),
      transition(...),
      transition(...)
    ])
  ]
})
class MyComponent {
  myStatusExp = "something";
}
```

The template associated with this component makes use of the defined trigger by binding to an element within its template code.

```
<!-- somewhere inside of my-component-tpl.html -->
<div [@myAnimationTrigger]="myStatusExp">...</div>
```

### Using an inline function

The [`transition`](transition) animation method also supports reading an inline function which can decide if its associated animation should be run.

```
// this method is run each time the `myAnimationTrigger` trigger value changes.
function myInlineMatcherFn(fromState: string, toState: string, element: any, params: {[key:
string]: any}): boolean {
  // notice that `element` and `params` are also available here
  return toState == 'yes-please-animate';
}

@Component({
  selector: 'my-component',
  templateUrl: 'my-component-tpl.html',
  animations: [
    trigger('myAnimationTrigger', [
      transition(myInlineMatcherFn, [
        // the animation sequence code
      ]),
    ])
  ]
})
class MyComponent {
  myStatusExp = "yes-please-animate";
}
```

### Disabling Animations

When true, the special animation control binding `@.disabled` binding prevents all animations from rendering. Place the `@.disabled` binding on an element to disable animations on the element itself, as well as any inner animation triggers within the element.

The following example shows how to use this feature:

```
@Component({
  selector: 'my-component',
  template: `
    <div [@.disabled]="isDisabled">
      <div [@childAnimation]="exp"></div>
    </div>
  `,
  animations: [
    trigger("childAnimation", [
      // ...
    ])
  ]
})
class MyComponent {
  isDisabled = true;
  exp = '...';
}
```

When `@.disabled` is true, it prevents the `@childAnimation` trigger from animating, along with any inner animations.

### Disable animations application-wide

When an area of the template is set to have animations disabled, **all** inner components have their animations disabled as well. This means that you can disable all animations for an app by placing a host binding set on `@.disabled` on the topmost Angular component.

```
import {Component, HostBinding} from '@angular/core';

@Component({
  selector: 'app-component',
  templateUrl: 'app.component.html',
})
class AppComponent {
  @HostBinding('@.disabled')
  public animationsDisabled = true;
}
```

### Overriding disablement of inner animations

Despite inner animations being disabled, a parent animation can [`query()`](query) for inner elements located in disabled areas of the template and still animate them if needed. This is also the case for when a sub animation is queried by a parent and then later animated using [`animateChild()`](animatechild).

### Detecting when an animation is disabled

If a region of the DOM (or the entire application) has its animations disabled, the animation trigger callbacks still fire, but for zero seconds. When the callback fires, it provides an instance of an [`AnimationEvent`](animationevent). If animations are disabled, the `.disabled` flag on the event is true.

## Usage Notes

Define an animation trigger in the `animations` section of `@Component` metadata. In the template, reference the trigger by name and bind it to a trigger expression that evaluates to a defined animation state, using the following format:

`[@triggerName]="expression"`

Animation trigger bindings convert all values to strings, and then match the previous and current values against any linked transitions. Booleans can be specified as `1` or `true` and `0` or `false`.

### Usage Example

The following example creates an animation trigger reference based on the provided name value. The provided animation value is expected to be an array consisting of state and transition declarations.

```
@Component({
  selector: "my-component",
  templateUrl: "my-component-tpl.html",
  animations: [
    trigger("myAnimationTrigger", [
      state(...),
      state(...),
      transition(...),
      transition(...)
    ])
  ]
})
class MyComponent {
  myStatusExp = "something";
}
```

The template associated with this component makes use of the defined trigger by binding to an element within its template code.

```
<!-- somewhere inside of my-component-tpl.html -->
<div [@myAnimationTrigger]="myStatusExp">...</div>
```

### Using an inline function

The [`transition`](transition) animation method also supports reading an inline function which can decide if its associated animation should be run.

```
// this method is run each time the `myAnimationTrigger` trigger value changes.
function myInlineMatcherFn(fromState: string, toState: string, element: any, params: {[key:
string]: any}): boolean {
  // notice that `element` and `params` are also available here
  return toState == 'yes-please-animate';
}

@Component({
  selector: 'my-component',
  templateUrl: 'my-component-tpl.html',
  animations: [
    trigger('myAnimationTrigger', [
      transition(myInlineMatcherFn, [
        // the animation sequence code
      ]),
    ])
  ]
})
class MyComponent {
  myStatusExp = "yes-please-animate";
}
```

### Disabling Animations

When true, the special animation control binding `@.disabled` binding prevents all animations from rendering. Place the `@.disabled` binding on an element to disable animations on the element itself, as well as any inner animation triggers within the element.

The following example shows how to use this feature:

```
@Component({
  selector: 'my-component',
  template: `
    <div [@.disabled]="isDisabled">
      <div [@childAnimation]="exp"></div>
    </div>
  `,
  animations: [
    trigger("childAnimation", [
      // ...
    ])
  ]
})
class MyComponent {
  isDisabled = true;
  exp = '...';
}
```

When `@.disabled` is true, it prevents the `@childAnimation` trigger from animating, along with any inner animations.

### Disable animations application-wide

When an area of the template is set to have animations disabled, **all** inner components have their animations disabled as well. This means that you can disable all animations for an app by placing a host binding set on `@.disabled` on the topmost Angular component.

```
import {Component, HostBinding} from '@angular/core';

@Component({
  selector: 'app-component',
  templateUrl: 'app.component.html',
})
class AppComponent {
  @HostBinding('@.disabled')
  public animationsDisabled = true;
}
```

### Overriding disablement of inner animations

Despite inner animations being disabled, a parent animation can [`query()`](query) for inner elements located in disabled areas of the template and still animate them if needed. This is also the case for when a sub animation is queried by a parent and then later animated using [`animateChild()`](animatechild).

### Detecting when an animation is disabled

If a region of the DOM (or the entire application) has its animations disabled, the animation trigger callbacks still fire, but for zero seconds. When the callback fires, it provides an instance of an [`AnimationEvent`](animationevent). If animations are disabled, the `.disabled` flag on the event is true.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/trigger>
