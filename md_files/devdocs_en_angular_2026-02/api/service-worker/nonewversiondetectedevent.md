# NoNewVersionDetectedEvent

NoNewVersionDetectedEvent



# NoNewVersionDetectedEvent

An event emitted when the service worker has checked the version of the app on the server and it didn't find a new version that it doesn't have already downloaded.

[Service Worker Communication Guide](https://angular.dev/ecosystem/service-workers/communications)

## API

```
interface NoNewVersionDetectedEvent {
  type: "NO_NEW_VERSION_DETECTED";
  version: { hash: string; appData?: Object | undefined; };
}
```

### type

`"NO_NEW_VERSION_DETECTED"`

### version

`{ hash: string; appData?: Object | undefined; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/NoNewVersionDetectedEvent>
