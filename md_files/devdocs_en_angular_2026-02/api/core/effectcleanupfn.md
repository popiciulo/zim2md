# EffectCleanupFn

EffectCleanupFn



# EffectCleanupFn

An effect can, optionally, register a cleanup function. If registered, the cleanup is executed before the next effect run. The cleanup function makes it possible to "cancel" any work that the previous effect run might have started.

[Effect cleanup functions](../../guide/signals#effect-cleanup-functions)

## API

```
type EffectCleanupFn = () => void
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/EffectCleanupFn>
