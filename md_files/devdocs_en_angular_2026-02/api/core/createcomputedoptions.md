# CreateComputedOptions

CreateComputedOptions



# CreateComputedOptions

Options passed to the [`computed`](computed) creation function.

## API

```
interface CreateComputedOptions<T> {
  equal?: ValueEqualityFn<T> | undefined;
  debugName?: string | undefined;
}
```

### equal

`ValueEqualityFn<T> | undefined`

A comparison function which defines equality for computed values.

### debugName

`string | undefined`

A debug name for the computed signal. Used in Angular DevTools to identify the signal.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/CreateComputedOptions>
