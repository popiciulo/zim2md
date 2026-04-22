# DestroyRef

DestroyRef



# DestroyRef

[`DestroyRef`](destroyref) lets you set callbacks to run for any cleanup or destruction behavior. The scope of this destruction depends on where [`DestroyRef`](destroyref) is injected. If [`DestroyRef`](destroyref) is injected in a component or directive, the callbacks run when that component or directive is destroyed. Otherwise the callbacks run when a corresponding injector is destroyed.

[Lifecycle DestroyRef](../../guide/components/lifecycle#destroyref)

## API

```
abstract class DestroyRef {
  abstract onDestroy(callback: () => void): () => void;
  abstract readonly destroyed: boolean;
}
```

### onDestroy

`() => void`

Registers a destroy callback in a given lifecycle scope. Returns a cleanup function that can be invoked to unregister the callback.

@paramcallback`() => void`

@returns`() => void`

Usage notes

### Example

```
const destroyRef = inject(DestroyRef);

// register a destroy callback
const unregisterFn = destroyRef.onDestroy(() => doSomethingOnDestroy());

// stop the destroy callback from executing if needed
unregisterFn();
```

### destroyed

`boolean`

Indicates whether the instance has already been destroyed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DestroyRef>
