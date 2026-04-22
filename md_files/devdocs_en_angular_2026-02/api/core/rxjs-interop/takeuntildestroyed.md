# takeUntilDestroyed

takeUntilDestroyed



# takeUntilDestroyed

Operator which completes the Observable when the calling context (component, directive, service, etc) is destroyed.

[Unsubscribing with takeUntilDestroyed](https://angular.dev/ecosystem/rxjs-interop/take-until-destroyed)

## API

```
function takeUntilDestroyed<T>(
  destroyRef?: DestroyRef | undefined,
): MonoTypeOperatorFunction<T>;
```

### takeUntilDestroyed

`MonoTypeOperatorFunction<T>`

Operator which completes the Observable when the calling context (component, directive, service, etc) is destroyed.

@paramdestroyRef`DestroyRef | undefined`

optionally, the `DestroyRef` representing the current context. This can be passed explicitly to use [`takeUntilDestroyed`](takeuntildestroyed) outside of an [injection context](../../../guide/di/dependency-injection-context). Otherwise, the current `DestroyRef` is injected.

@returns`MonoTypeOperatorFunction<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/takeUntilDestroyed>
