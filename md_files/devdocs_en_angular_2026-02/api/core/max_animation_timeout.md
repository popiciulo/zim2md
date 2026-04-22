# MAX_ANIMATION_TIMEOUT

MAX\_ANIMATION\_TIMEOUT



# MAX\_ANIMATION\_TIMEOUT

A [DI token](injectiontoken) that configures the maximum animation timeout before element removal. The default value mirrors from Chrome's cross document navigation view transition timeout. It's intended to prevent people from accidentally forgetting to call the removal function in their callback. Also serves as a delay for when stylesheets are pruned.

[Animating your applications with animate.enter and animate.leave](../../guide/animations)

## API

```
const MAX_ANIMATION_TIMEOUT: InjectionToken<number>;
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/MAX_ANIMATION_TIMEOUT>
