# UnrecoverableStateEvent

UnrecoverableStateEvent



# UnrecoverableStateEvent

An event emitted when the version of the app used by the service worker to serve this client is in a broken state that cannot be recovered from and a full page reload is required.

[Handling an unrecoverable state](https://angular.dev/ecosystem/service-workers/communications#handling-an-unrecoverable-state)

## API

```
interface UnrecoverableStateEvent {
  type: "UNRECOVERABLE_STATE";
  reason: string;
}
```

### type

`"UNRECOVERABLE_STATE"`

### reason

`string`

## Description

An event emitted when the version of the app used by the service worker to serve this client is in a broken state that cannot be recovered from and a full page reload is required.

For example, the service worker may not be able to retrieve a required resource, neither from the cache nor from the server. This could happen if a new version is deployed to the server and the service worker cache has been partially cleaned by the browser, removing some files of a previous app version but not all.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/UnrecoverableStateEvent>
