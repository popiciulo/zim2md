# assertNotInReactiveContext

assertNotInReactiveContext



# assertNotInReactiveContext

Asserts that the current stack frame is not within a reactive context. Useful to disallow certain code from running inside a reactive context (see [`toSignal`](rxjs-interop/tosignal))

## API

```
function assertNotInReactiveContext(
  debugFn: Function,
  extraContext?: string | undefined,
): void;
```

### assertNotInReactiveContext

`void`

Asserts that the current stack frame is not within a reactive context. Useful to disallow certain code from running inside a reactive context (see [`toSignal`](rxjs-interop/tosignal))

@paramdebugFn`Function`

a reference to the function making the assertion (used for the error message).

@paramextraContext`string | undefined`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/assertNotInReactiveContext>
