# SwUpdate

SwUpdate



# SwUpdate

Subscribe to update notifications from the Service Worker, trigger update checks, and forcibly activate updates.

[Service Worker Communication Guide](https://angular.dev/ecosystem/service-workers/communications)

## API

```
class SwUpdate {
  constructor(sw: NgswCommChannel): SwUpdate;
  readonly versionUpdates: Observable<VersionEvent>;
  readonly unrecoverable: Observable<UnrecoverableStateEvent>;
  readonly isEnabled: boolean;
  checkForUpdate(): Promise<boolean>;
  activateUpdate(): Promise<boolean>;
}
```

### constructor

`SwUpdate`

@paramsw`NgswCommChannel`

@returns`SwUpdate`

### versionUpdates

`Observable<VersionEvent>`

Emits a [`VersionDetectedEvent`](versiondetectedevent) event whenever a new version is detected on the server.

Emits a [`VersionInstallationFailedEvent`](versioninstallationfailedevent) event whenever checking for or downloading a new version fails.

Emits a [`VersionReadyEvent`](versionreadyevent) event whenever a new version has been downloaded and is ready for activation.

### unrecoverable

`Observable<UnrecoverableStateEvent>`

Emits an [`UnrecoverableStateEvent`](unrecoverablestateevent) event whenever the version of the app used by the service worker to serve this client is in a broken state that cannot be recovered from without a full page reload.

### isEnabled

`boolean`

True if the Service Worker is enabled (supported by the browser and enabled via [`ServiceWorkerModule`](serviceworkermodule)).

### checkForUpdate

`Promise<boolean>`

Checks for an update and waits until the new version is downloaded from the server and ready for activation.

@returns`Promise<boolean>`

### activateUpdate

`Promise<boolean>`

Updates the current client (i.e. browser tab) to the latest version that is ready for activation.

In most cases, you should not use this method and instead should update a client by reloading the page.

Updating a client without reloading can easily result in a broken application due to a version mismatch between the application shell and other page resources, such as lazy-loaded chunks, whose filenames may change between versions.

Only use this method, if you are certain it is safe for your specific use case.

@returns`Promise<boolean>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/SwUpdate>
