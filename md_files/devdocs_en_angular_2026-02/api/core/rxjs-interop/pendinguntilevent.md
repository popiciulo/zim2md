# pendingUntilEvent

pendingUntilEvent



# pendingUntilEvent

Operator which makes the application unstable until the observable emits, completes, errors, or is unsubscribed.

## API

```
function pendingUntilEvent<T>(
  injector?: Injector | undefined,
): MonoTypeOperatorFunction<T>;
```

### pendingUntilEvent

`MonoTypeOperatorFunction<T>`

Operator which makes the application unstable until the observable emits, completes, errors, or is unsubscribed.

Use this operator in observables whose subscriptions are important for rendering and should be included in SSR serialization.

@paraminjector`Injector | undefined`

The `Injector` to use during creation. If this is not provided, the current injection context will be used instead (via `inject`).

@returns`MonoTypeOperatorFunction<T>`

## Description

Operator which makes the application unstable until the observable emits, completes, errors, or is unsubscribed.

Use this operator in observables whose subscriptions are important for rendering and should be included in SSR serialization.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/pendingUntilEvent>
