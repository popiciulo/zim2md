# AnimateChildOptions

AnimateChildOptions



# AnimateChildOptions

Adds duration options to control animation styling and timing for a child animation.

[animateChild](animatechild)

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimateChildOptions extends AnimationOptions {
  duration?: string | number | undefined;
  override delay?: string | number | undefined;
  override params?: { [name: string]: any; } | undefined;
}
```

### duration

`string | number | undefined`

### delay

`string | number | undefined`

Sets a time-delay for initiating an animation action. A number and optional time unit, such as "1s" or "10ms" for one second and 10 milliseconds, respectively.The default unit is milliseconds. Default value is 0, meaning no delay.

### params

`{ [name: string]: any; } | undefined`

A set of developer-defined parameters that modify styling and timing when an animation action starts. An array of key-value pairs, where the provided value is used as a default.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimateChildOptions>
