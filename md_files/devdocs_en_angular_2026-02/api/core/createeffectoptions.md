# CreateEffectOptions

CreateEffectOptions



# CreateEffectOptions

Options passed to the [`effect`](effect) function.

## API

```
interface CreateEffectOptions {
  injector?: Injector | undefined;
  manualCleanup?: boolean | undefined;
  allowSignalWrites?: boolean | undefined;
  debugName?: string | undefined;
}
```

### injector

`Injector | undefined`

The [`Injector`](injector) in which to create the effect.

If this is not provided, the current [injection context](../../guide/di/dependency-injection-context) will be used instead (via [`inject`](inject)).

### manualCleanup

`boolean | undefined`

Whether the [`effect`](effect) should require manual cleanup.

If this is `false` (the default) the effect will automatically register itself to be cleaned up with the current [`DestroyRef`](destroyref).

If this is `true` and you want to use the effect outside an injection context, you still need to provide an [`Injector`](injector) to the effect.

### allowSignalWrites

`boolean | undefined`

@deprecated

no longer required, signal writes are allowed by default.

### debugName

`string | undefined`

A debug name for the effect. Used in Angular DevTools to identify the effect.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/CreateEffectOptions>
