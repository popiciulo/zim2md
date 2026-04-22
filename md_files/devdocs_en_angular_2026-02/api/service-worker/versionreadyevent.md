# VersionReadyEvent

VersionReadyEvent



# VersionReadyEvent

An event emitted when a new version of the app is available.

[Service Worker Communication Guide](https://angular.dev/ecosystem/service-workers/communications)

## API

```
interface VersionReadyEvent {
  type: "VERSION_READY";
  currentVersion: { hash: string; appData?: object | undefined; };
  latestVersion: { hash: string; appData?: object | undefined; };
}
```

### type

`"VERSION_READY"`

### currentVersion

`{ hash: string; appData?: object | undefined; }`

### latestVersion

`{ hash: string; appData?: object | undefined; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/VersionReadyEvent>
