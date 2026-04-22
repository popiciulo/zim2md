# CreateSignalOptions

CreateSignalOptions



# CreateSignalOptions

Options passed to the [`signal`](signal) creation function.

## API

```
interface CreateSignalOptions<T> {
  equal?: ValueEqualityFn<T> | undefined;
  debugName?: string | undefined;
}
```

### equal

`ValueEqualityFn<T> | undefined`

A comparison function which defines equality for signal values.

### debugName

`string | undefined`

A debug name for the signal. Used in Angular DevTools to identify the signal.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/CreateSignalOptions>
