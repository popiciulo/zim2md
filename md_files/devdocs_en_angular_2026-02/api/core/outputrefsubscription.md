# OutputRefSubscription

OutputRefSubscription



# OutputRefSubscription

Function that can be used to manually clean up a programmatic [`OutputRef#subscribe`](outputref#subscribe) subscription.

[Subscribing to outputs programmatically](../../guide/components/outputs#subscribing-to-outputs-programmatically)

## API

```
interface OutputRefSubscription {
  unsubscribe(): void;
}
```

### unsubscribe

`void`

@returns`void`

## Description

Function that can be used to manually clean up a programmatic [`OutputRef#subscribe`](outputref#subscribe) subscription.

Note: Angular will automatically clean up subscriptions when the directive/component of the output is destroyed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OutputRefSubscription>
