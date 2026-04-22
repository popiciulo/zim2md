# toSignal

toSignal



# toSignal

Get the current value of an `Observable` as a reactive `Signal`.

[RxJS interop with Angular signals](https://angular.dev/ecosystem/rxjs-interop)

## API

```
function toSignal<T>(source: any): Signal<T | undefined>;
function toSignal<T>(
  source: any,
  options: NoInfer<ToSignalOptions<T | undefined>> & {
    initialValue?: undefined;
    requireSync?: false | undefined;
  },
): Signal<T | undefined>;
function toSignal<T>(
  source: any,
  options: NoInfer<ToSignalOptions<T | null>> & {
    initialValue?: null | undefined;
    requireSync?: false | undefined;
  },
): Signal<T | null>;
function toSignal<T>(
  source: any,
  options: NoInfer<ToSignalOptions<T>> & {
    initialValue?: undefined;
    requireSync: true;
  },
): Signal<T>;
function toSignal<T, U extends T>(
  source: any,
  options: NoInfer<ToSignalOptions<T | U>> & {
    initialValue: U;
    requireSync?: false | undefined;
  },
): Signal<T | U>;
```

```
function toSignal<T>(source: any): Signal<T | undefined>;
```

@paramsource`any`

@returns`Signal<T | undefined>`

```
function toSignal<T>(source: any, options: NoInfer<ToSignalOptions<T | undefined>> & { initialValue?: undefined; requireSync?: false | undefined; }): Signal<T | undefined>;
```

@paramsource`any`

@paramoptions`NoInfer<ToSignalOptions<T | undefined>> & { initialValue?: undefined; requireSync?: false | undefined; }`

@returns`Signal<T | undefined>`

```
function toSignal<T>(source: any, options: NoInfer<ToSignalOptions<T | null>> & { initialValue?: null | undefined; requireSync?: false | undefined; }): Signal<T | null>;
```

@paramsource`any`

@paramoptions`NoInfer<ToSignalOptions<T | null>> & { initialValue?: null | undefined; requireSync?: false | undefined; }`

@returns`Signal<T | null>`

```
function toSignal<T>(source: any, options: NoInfer<ToSignalOptions<T>> & { initialValue?: undefined; requireSync: true; }): Signal<T>;
```

@paramsource`any`

@paramoptions`NoInfer<ToSignalOptions<T>> & { initialValue?: undefined; requireSync: true; }`

@returns`Signal<T>`

```
function toSignal<T, U>(source: any, options: NoInfer<ToSignalOptions<T | U>> & { initialValue: U; requireSync?: false | undefined; }): Signal<T | U>;
```

@paramsource`any`

@paramoptions`NoInfer<ToSignalOptions<T | U>> & { initialValue: U; requireSync?: false | undefined; }`

@returns`Signal<T | U>`

## Description

Get the current value of an `Observable` as a reactive `Signal`.

[`toSignal`](tosignal) returns a `Signal` which provides synchronous reactive access to values produced by the given `Observable`, by subscribing to that `Observable`. The returned `Signal` will always have the most recent value emitted by the subscription, and will throw an error if the `Observable` errors.

With `requireSync` set to `true`, [`toSignal`](tosignal) will assert that the `Observable` produces a value immediately upon subscription. No `initialValue` is needed in this case, and the returned signal does not include an `undefined` type.

By default, the subscription will be automatically cleaned up when the current [injection context](../../../guide/di/dependency-injection-context) is destroyed. For example, when [`toSignal`](tosignal) is called during the construction of a component, the subscription will be cleaned up when the component is destroyed. If an injection context is not available, an explicit `Injector` can be passed instead.

If the subscription should persist until the `Observable` itself completes, the `manualCleanup` option can be specified instead, which disables the automatic subscription teardown. No injection context is needed in this configuration as well.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/toSignal>
