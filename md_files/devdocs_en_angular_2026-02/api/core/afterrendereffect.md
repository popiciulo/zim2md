# afterRenderEffect

afterRenderEffect



# afterRenderEffect

## API

```
function afterRenderEffect(
  callback: (onCleanup: EffectCleanupRegisterFn) => void,
  options?: AfterRenderOptions | undefined,
): AfterRenderRef;
function afterRenderEffect<E = never, W = never, M = never>(
  spec: {
    earlyRead?: ((onCleanup: EffectCleanupRegisterFn) => E) | undefined;
    write?:
      | ((
          ...args: [
            ...([E] extends [never] ? [] : [Signal<E>]),
            EffectCleanupRegisterFn,
          ]
        ) => W)
      | undefined;
    mixedReadWrite?:
      | ((
          ...args: [
            ...([W] extends [never]
              ? [E] extends [never]
                ? []
                : [Signal<E>]
              : [Signal<W>]),
            EffectCleanupRegisterFn,
          ]
        ) => M)
      | undefined;
    read?:
      | ((
          ...args: [
            ...([M] extends [never]
              ? [W] extends [never]
                ? [E] extends [never]
                  ? []
                  : [Signal<E>]
                : [Signal<W>]
              : [Signal<M>]),
            EffectCleanupRegisterFn,
          ]
        ) => void)
      | undefined;
  },
  options?: AfterRenderOptions | undefined,
): AfterRenderRef;
```

```
function afterRenderEffect(callback: (onCleanup: EffectCleanupRegisterFn) => void, options?: AfterRenderOptions | undefined): AfterRenderRef;
```

Register an effect that, when triggered, is invoked when the application finishes rendering, during the `mixedReadWrite` phase.

You should prefer specifying an explicit phase for the effect instead, or you risk significant performance degradation.

Note that callback-based [`afterRenderEffect`](afterrendereffect)s will run

- in the order it they are registered
- only when dirty
- on browser platforms only
- during the `mixedReadWrite` phase

Components are not guaranteed to be [hydrated](../../guide/hydration) before the callback runs. You must use caution when directly reading or writing the DOM and layout.

@paramcallback`(onCleanup: EffectCleanupRegisterFn) => void`

An effect callback function to register

@paramoptions`AfterRenderOptions | undefined`

Options to control the behavior of the callback

@returns`AfterRenderRef`

```
function afterRenderEffect<E = never, W = never, M = never>(spec: { earlyRead?: ((onCleanup: EffectCleanupRegisterFn) => E) | undefined; write?: ((...args: [...[E] extends [never] ? [] : [Signal<E>], EffectCleanupRegisterFn]) => W) | undefined; mixedReadWrite?: ((...args: [...[W] extends [never] ? [E] extends [never] ? [] : [Signal<E>] : [Signal<W>], EffectCleanupRegisterFn]) => M) | undefined; read?: ((...args: [...[M] extends [never] ? [W] extends [never] ? [E] extends [never] ? [] : [Signal<E>] : [Signal<W>] : [Signal<M>], EffectCleanupRegisterFn]) => void) | undefined; }, options?: AfterRenderOptions | undefined): AfterRenderRef;
```

Register effects that, when triggered, are invoked when the application finishes rendering, during the specified phases. The available phases are:

- `earlyRead` Use this phase to **read** from the DOM before a subsequent `write` callback, for example to perform custom layout that the browser doesn't natively support. Prefer the `read` phase if reading can wait until after the write phase. **Never** write to the DOM in this phase.
- `write` Use this phase to **write** to the DOM. **Never** read from the DOM in this phase.
- `mixedReadWrite` Use this phase to read from and write to the DOM simultaneously. **Never** use this phase if it is possible to divide the work among the other phases instead.
- `read` Use this phase to **read** from the DOM. **Never** write to the DOM in this phase.

You should prefer using the `read` and `write` phases over the `earlyRead` and `mixedReadWrite` phases when possible, to avoid performance degradation.

Note that:

- Effects run in the following phase order, only when dirty through signal dependencies:
  1. `earlyRead`
  2. `write`
  3. `mixedReadWrite`
  4. `read`
- [`afterRenderEffect`](afterrendereffect)s in the same phase run in the order they are registered.
- [`afterRenderEffect`](afterrendereffect)s run on browser platforms only, they will not run on the server.
- [`afterRenderEffect`](afterrendereffect)s will run at least once.

The first phase callback to run as part of this spec will receive no parameters. Each subsequent phase callback in this spec will receive the return value of the previously run phase callback as a [`Signal`](signal). This can be used to coordinate work across multiple phases.

Angular is unable to verify or enforce that phases are used correctly, and instead relies on each developer to follow the guidelines documented for each value and carefully choose the appropriate one, refactoring their code if necessary. By doing so, Angular is better able to minimize the performance degradation associated with manual DOM access, ensuring the best experience for the end users of your application or library.

Components are not guaranteed to be [hydrated](../../guide/hydration) before the callback runs. You must use caution when directly reading or writing the DOM and layout.

@paramspec`{ earlyRead?: ((onCleanup: EffectCleanupRegisterFn) => E) | undefined; write?: ((...args: [...[E] extends [never] ? [] : [Signal<E>], EffectCleanupRegisterFn]) => W) | undefined; mixedReadWrite?: ((...args: [...[W] extends [never] ? [E] extends [never] ? [] : [Signal<E>] : [Signal<W>], EffectCleanupRegisterFn]) => M) | undefined; read?: ((...args: [...[M] extends [never] ? [W] extends [never] ? [E] extends [never] ? [] : [Signal<E>] : [Signal<W>] : [Signal<M>], EffectCleanupRegisterFn]) => void) | undefined; }`

The effect functions to register

@paramoptions`AfterRenderOptions | undefined`

Options to control the behavior of the effects

@returns`AfterRenderRef`

Usage notes

Use [`afterRenderEffect`](afterrendereffect) to create effects that will read or write from the DOM and thus should run after rendering.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/afterRenderEffect>
