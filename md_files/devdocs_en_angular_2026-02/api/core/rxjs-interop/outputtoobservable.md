# outputToObservable

outputToObservable



# outputToObservable

Converts an Angular output declared via `output()` or [`outputFromObservable()`](outputfromobservable) to an observable. It creates an observable that represents the stream of "events firing" in an output.

[RxJS interop with component and directive outputs](https://angular.dev/ecosystem/rxjs-interop/output-interop)

## API

```
function outputToObservable<T>(ref: OutputRef<T>): Observable<T>;
```

### outputToObservable

`Observable<T>`

Converts an Angular output declared via `output()` or [`outputFromObservable()`](outputfromobservable) to an observable. It creates an observable that represents the stream of "events firing" in an output.

You can subscribe to the output via `Observable.subscribe` then.

@paramref`OutputRef<T>`

@returns`Observable<T>`

## Description

Converts an Angular output declared via `output()` or [`outputFromObservable()`](outputfromobservable) to an observable. It creates an observable that represents the stream of "events firing" in an output.

You can subscribe to the output via `Observable.subscribe` then.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/outputToObservable>
