# ServiceWorkerModule

ServiceWorkerModule



# ServiceWorkerModule

[Custom service worker script](https://angular.dev/ecosystem/service-workers/custom-service-worker-scripts)[Service worker configuration](https://angular.dev/ecosystem/service-workers/getting-started#service-worker-configuration)

## API

```
class ServiceWorkerModule {
  static register(script: string, options?: SwRegistrationOptions): ModuleWithProviders<ServiceWorkerModule>;
}
```

### register

`ModuleWithProviders<ServiceWorkerModule>`

Register the given Angular Service Worker script.

If `enabled` is set to `false` in the given options, the module will behave as if service workers are not supported by the browser, and the service worker will not be registered.

@paramscript`string`

@paramoptions`SwRegistrationOptions`

@returns`ModuleWithProviders<ServiceWorkerModule>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/ServiceWorkerModule>
