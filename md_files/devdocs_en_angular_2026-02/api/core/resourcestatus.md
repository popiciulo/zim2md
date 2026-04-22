# ResourceStatus

ResourceStatus



# ResourceStatus

String value capturing the status of a [`Resource`](resource).

## API

```
type ResourceStatus = 'idle' | 'error' | 'loading' | 'reloading' | 'resolved' | 'local'
```

## Description

String value capturing the status of a [`Resource`](resource).

Possible statuses are:

`idle` - The resource has no valid request and will not perform any loading. `value()` will be `undefined`.

`loading` - The resource is currently loading a new value as a result of a change in its reactive dependencies. `value()` will be `undefined`.

`reloading` - The resource is currently reloading a fresh value for the same reactive dependencies. `value()` will continue to return the previously fetched value during the reloading operation.

`error` - Loading failed with an error. `value()` will be `undefined`.

`resolved` - Loading has completed and the resource has the value returned from the loader.

`local` - The resource's value was set locally via `.set()` or `.update()`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ResourceStatus>
