# toObservable

toObservable



# toObservable

Exposes the value of an Angular `Signal` as an RxJS `Observable`. As it reflects a state, the observable will always emit the latest value upon subscription.

[RxJS interop with Angular signals](https://angular.dev/ecosystem/rxjs-interop)[Create an RxJS Observable from a signal with toObservable](https://angular.dev/ecosystem/rxjs-interop#create-an-rxjs-observable-from-a-signal-with-toobservable)

## API

```
function toObservable<T>(
  source: Signal<T>,
  options?: ToObservableOptions | undefined,
): Observable<T>;
```

### toObservable

`Observable<T>`

Exposes the value of an Angular `Signal` as an RxJS `Observable`. As it reflects a state, the observable will always emit the latest value upon subscription.

The signal's value will be propagated into the `Observable`'s subscribers using an `effect`.

[`toObservable`](toobservable) must be called in an injection context unless an injector is provided via options.

@paramsource`Signal<T>`

@paramoptions`ToObservableOptions | undefined`

@returns`Observable<T>`

## Description

Exposes the value of an Angular `Signal` as an RxJS `Observable`. As it reflects a state, the observable will always emit the latest value upon subscription.

The signal's value will be propagated into the `Observable`'s subscribers using an `effect`.

[`toObservable`](toobservable) must be called in an injection context unless an injector is provided via options.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/toObservable>
