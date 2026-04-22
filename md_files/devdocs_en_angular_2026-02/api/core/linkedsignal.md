# linkedSignal

linkedSignal



# linkedSignal

## API

```
function linkedSignal<D>(
  computation: () => D,
  options?:
    | {
        equal?: ValueEqualityFn<NoInfer<D>> | undefined;
        debugName?: string | undefined;
      }
    | undefined,
): WritableSignal<D>;
function linkedSignal<S, D>(options: {
  source: () => S;
  computation: (
    source: NoInfer<S>,
    previous?: { source: NoInfer<S>; value: NoInfer<D> } | undefined,
  ) => D;
  equal?: ValueEqualityFn<NoInfer<D>> | undefined;
  debugName?: string | undefined;
}): WritableSignal<D>;
```

```
function linkedSignal<D>(computation: () => D, options?: { equal?: ValueEqualityFn<NoInfer<D>> | undefined; debugName?: string | undefined; } | undefined): WritableSignal<D>;
```

Creates a writable signal whose value is initialized and reset by the linked, reactive computation.

@paramcomputation`() => D`

@paramoptions`{ equal?: ValueEqualityFn<NoInfer<D>> | undefined; debugName?: string | undefined; } | undefined`

@returns`WritableSignal<D>`

```
function linkedSignal<S, D>(options: { source: () => S; computation: (source: NoInfer<S>, previous?: { source: NoInfer<S>; value: NoInfer<D>; } | undefined) => D; equal?: ValueEqualityFn<NoInfer<D>> | undefined; debugName?: string | undefined; }): WritableSignal<D>;
```

Creates a writable signal whose value is initialized and reset by the linked, reactive computation. This is an advanced API form where the computation has access to the previous value of the signal and the computation result.

Note: The computation is reactive, meaning the linked signal will automatically update whenever any of the signals used within the computation change.

@paramoptions`{ source: () => S; computation: (source: NoInfer<S>, previous?: { source: NoInfer<S>; value: NoInfer<D>; } | undefined) => D; equal?: ValueEqualityFn<NoInfer<D>> | undefined; debugName?: string | undefined; }`

@returns`WritableSignal<D>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/linkedSignal>
