# runInInjectionContext

runInInjectionContext



# runInInjectionContext

Runs the given function in the [context](../../guide/di/dependency-injection-context) of the given [`Injector`](injector).

[Run within an injection context](../../guide/di/dependency-injection-context#run-within-an-injection-context)

## API

```
function runInInjectionContext<ReturnT>(
  injector: Injector,
  fn: () => ReturnT,
): ReturnT;
```

### runInInjectionContext

`ReturnT`

Runs the given function in the [context](../../guide/di/dependency-injection-context) of the given [`Injector`](injector).

Within the function's stack frame, [`inject`](inject) can be used to inject dependencies from the given [`Injector`](injector). Note that [`inject`](inject) is only usable synchronously, and cannot be used in any asynchronous callbacks or after any `await` points.

@paraminjector`Injector`

the injector which will satisfy calls to [`inject`](inject) while `fn` is executing

@paramfn`() => ReturnT`

the closure to be run in the context of `injector`

@returns`ReturnT`

## Description

Runs the given function in the [context](../../guide/di/dependency-injection-context) of the given [`Injector`](injector).

Within the function's stack frame, [`inject`](inject) can be used to inject dependencies from the given [`Injector`](injector). Note that [`inject`](inject) is only usable synchronously, and cannot be used in any asynchronous callbacks or after any `await` points.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/runInInjectionContext>
