# AnimateTimings

AnimateTimings



# AnimateTimings

Represents animation-step timing parameters for an animation step.

[animate](animatetimings#animate)

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
type AnimateTimings = {
  /**
   * The full duration of an animation step. A number and optional time unit,
   * such as "1s" or "10ms" for one second and 10 milliseconds, respectively.
   * The default unit is milliseconds.
   */
  duration: number;
  /**
   * The delay in applying an animation step. A number and optional time unit.
   * The default unit is milliseconds.
   */
  delay: number;
  /**
   * An easing style that controls how an animations step accelerates
   * and decelerates during its run time. An easing function such as `cubic-bezier()`,
   * or one of the following constants:
   * - `ease-in`
   * - `ease-out`
   * - `ease-in-and-out`
   */
  easing: string | null;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimateTimings>
