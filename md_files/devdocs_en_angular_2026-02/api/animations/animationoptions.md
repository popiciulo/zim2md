# AnimationOptions

AnimationOptions



# AnimationOptions

Options that control animation styling and timing.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationOptions {
  delay?: string | number | undefined;
  params?: { [name: string]: any; } | undefined;
}
```

### delay

`string | number | undefined`

Sets a time-delay for initiating an animation action. A number and optional time unit, such as "1s" or "10ms" for one second and 10 milliseconds, respectively.The default unit is milliseconds. Default value is 0, meaning no delay.

### params

`{ [name: string]: any; } | undefined`

A set of developer-defined parameters that modify styling and timing when an animation action starts. An array of key-value pairs, where the provided value is used as a default.

## Description

Options that control animation styling and timing.

The following animation functions accept [`AnimationOptions`](animationoptions) data:

- [`transition()`](transition)
- [`sequence()`](sequence)
- [`group()`](group)
- [`query()`](query)
- [`animation()`](animation)
- [`useAnimation()`](useanimation)
- [`animateChild()`](animatechild)

Programmatic animations built using the [`AnimationBuilder`](animationbuilder) service also make use of [`AnimationOptions`](animationoptions).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationOptions>
