# outputFromObservable

outputFromObservable



# outputFromObservable

Declares an Angular output that is using an RxJS observable as a source for events dispatched to parent subscribers.

[RxJS interop with component and directive outputs](https://angular.dev/ecosystem/rxjs-interop/output-interop)

## API

```
function outputFromObservable<T>(
  observable: Observable<T>,
  opts?: OutputOptions | undefined,
): OutputRef<T>;
```

### outputFromObservable

`OutputRef<T>`

Declares an Angular output that is using an RxJS observable as a source for events dispatched to parent subscribers.

The behavior for an observable as source is defined as followed:

1. New values are forwarded to the Angular output (next notifications).
2. Errors notifications are not handled by Angular. You need to handle these manually. For example by using `catchError`.
3. Completion notifications stop the output from emitting new values.

@paramobservable`Observable<T>`

@paramopts`OutputOptions | undefined`

@returns`OutputRef<T>`

Usage notes

Initialize an output in your directive by declaring a class field and initializing it with the [`outputFromObservable()`](outputfromobservable) function.

```
@Directive({..})
export class MyDir {
  nameChange$ = <some-observable>;
  nameChange = outputFromObservable(this.nameChange$);
}
```

## Description

Declares an Angular output that is using an RxJS observable as a source for events dispatched to parent subscribers.

The behavior for an observable as source is defined as followed:

1. New values are forwarded to the Angular output (next notifications).
2. Errors notifications are not handled by Angular. You need to handle these manually. For example by using `catchError`.
3. Completion notifications stop the output from emitting new values.

## Usage Notes

Initialize an output in your directive by declaring a class field and initializing it with the [`outputFromObservable()`](outputfromobservable) function.

```
@Directive({..})
export class MyDir {
  nameChange$ = <some-observable>;
  nameChange = outputFromObservable(this.nameChange$);
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/outputFromObservable>
