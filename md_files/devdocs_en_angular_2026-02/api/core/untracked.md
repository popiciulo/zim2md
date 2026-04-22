# untracked

untracked



# untracked

Execute an arbitrary function in a non-reactive (non-tracking) context. The executed function can, optionally, return a value.

[Reading without tracking dependencies](../../guide/signals#reading-without-tracking-dependencies)

## API

```
function untracked<T>(nonReactiveReadsFn: () => T): T;
```

### untracked

`T`

Execute an arbitrary function in a non-reactive (non-tracking) context. The executed function can, optionally, return a value.

@paramnonReactiveReadsFn`() => T`

@returns`T`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/untracked>
