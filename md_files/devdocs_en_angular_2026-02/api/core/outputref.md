# OutputRef

OutputRef



# OutputRef

A reference to an Angular output.

[Subscribing to outputs programmatically](../../guide/components/outputs#subscribing-to-outputs-programmatically)

## API

```
interface OutputRef<T> {
  subscribe(callback: (value: T) => void): OutputRefSubscription;
}
```

### subscribe

`OutputRefSubscription`

Registers a callback that is invoked whenever the output emits a new value of type `T`.

Angular will automatically clean up the subscription when the directive/component of the output is destroyed.

@paramcallback`(value: T) => void`

@returns`OutputRefSubscription`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OutputRef>
