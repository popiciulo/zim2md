# VersionDetectedEvent

VersionDetectedEvent



# VersionDetectedEvent

An event emitted when the service worker has detected a new version of the app on the server and is about to start downloading it.

[Service Worker Communication Guide](https://angular.dev/ecosystem/service-workers/communications)

## API

```
interface VersionDetectedEvent {
  type: "VERSION_DETECTED";
  version: { hash: string; appData?: object | undefined; };
}
```

### type

`"VERSION_DETECTED"`

### version

`{ hash: string; appData?: object | undefined; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/VersionDetectedEvent>
