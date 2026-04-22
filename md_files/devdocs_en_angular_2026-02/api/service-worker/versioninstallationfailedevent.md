# VersionInstallationFailedEvent

VersionInstallationFailedEvent



# VersionInstallationFailedEvent

An event emitted when the installation of a new version failed. It may be used for logging/monitoring purposes.

[Service Worker Communication Guide](https://angular.dev/ecosystem/service-workers/communications)

## API

```
interface VersionInstallationFailedEvent {
  type: "VERSION_INSTALLATION_FAILED";
  version: { hash: string; appData?: object | undefined; };
  error: string;
}
```

### type

`"VERSION_INSTALLATION_FAILED"`

### version

`{ hash: string; appData?: object | undefined; }`

### error

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/VersionInstallationFailedEvent>
