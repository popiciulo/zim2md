# ToSignalOptions

ToSignalOptions



# ToSignalOptions

Options for [`toSignal`](tosignal).

## API

```
interface ToSignalOptions<T> {
  initialValue?: unknown;
  requireSync?: boolean | undefined;
  injector?: Injector | undefined;
  manualCleanup?: boolean | undefined;
  equal?: ValueEqualityFn<T> | undefined;
  debugName?: string | undefined;
}
```

### initialValue

`unknown`

Initial value for the signal produced by [`toSignal`](tosignal).

This will be the value of the signal until the observable emits its first value.

### requireSync

`boolean | undefined`

Whether to require that the observable emits synchronously when [`toSignal`](tosignal) subscribes.

If this is `true`, [`toSignal`](tosignal) will assert that the observable produces a value immediately upon subscription. Setting this option removes the need to either deal with `undefined` in the signal type or provide an `initialValue`, at the cost of a runtime error if this requirement is not met.

### injector

`Injector | undefined`

`Injector` which will provide the `DestroyRef` used to clean up the Observable subscription.

If this is not provided, a `DestroyRef` will be retrieved from the current [injection context](../../../guide/di/dependency-injection-context), unless manual cleanup is requested.

### manualCleanup

`boolean | undefined`

Whether the subscription should be automatically cleaned up (via `DestroyRef`) when [`toSignal`](tosignal)'s creation context is destroyed.

If manual cleanup is enabled, then `DestroyRef` is not used, and the subscription will persist until the `Observable` itself completes.

### equal

`ValueEqualityFn<T> | undefined`

A comparison function which defines equality for values emitted by the observable.

Equality comparisons are executed against the initial value if one is provided.

### debugName

`string | undefined`

A debug name for the signal. Used in Angular DevTools to identify the signal.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/ToSignalOptions>
