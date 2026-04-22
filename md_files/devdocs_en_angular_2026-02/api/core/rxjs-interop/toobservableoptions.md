# ToObservableOptions

ToObservableOptions



# ToObservableOptions

Options for [`toObservable`](toobservable).

## API

```
interface ToObservableOptions {
  injector?: Injector | undefined;
}
```

### injector

`Injector | undefined`

The `Injector` to use when creating the underlying `effect` which watches the signal.

If this isn't specified, the current [injection context](../../../guide/di/dependency-injection-context) will be used.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/ToObservableOptions>
