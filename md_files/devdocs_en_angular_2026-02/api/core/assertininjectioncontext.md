# assertInInjectionContext

assertInInjectionContext



# assertInInjectionContext

Asserts that the current stack frame is within an [injection context](../../guide/di/dependency-injection-context) and has access to [`inject`](inject).

[Asserts the context](../../guide/di/dependency-injection-context#asserts-the-context)

## API

```
function assertInInjectionContext(debugFn: Function): void;
```

### assertInInjectionContext

`void`

Asserts that the current stack frame is within an [injection context](../../guide/di/dependency-injection-context) and has access to [`inject`](inject).

@paramdebugFn`Function`

a reference to the function making the assertion (used for the error message).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/assertInInjectionContext>
