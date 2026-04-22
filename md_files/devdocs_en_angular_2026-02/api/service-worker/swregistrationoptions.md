# SwRegistrationOptions

SwRegistrationOptions



# SwRegistrationOptions

Token that can be used to provide options for [`ServiceWorkerModule`](serviceworkermodule) outside of [`ServiceWorkerModule.register()`](serviceworkermodule#register).

[Service worker configuration](https://angular.dev/ecosystem/service-workers/getting-started#service-worker-configuration)

## API

```
abstract class SwRegistrationOptions {
  enabled?: boolean | undefined;
  updateViaCache?: ServiceWorkerUpdateViaCache | undefined;
  type?: WorkerType | undefined;
  scope?: string | undefined;
  registrationStrategy?: string | (() => Observable<unknown>) | undefined;
}
```

### enabled

`boolean | undefined`

Whether the ServiceWorker will be registered and the related services (such as [`SwPush`](swpush) and [`SwUpdate`](swupdate)) will attempt to communicate and interact with it.

Default: true

### updateViaCache

`ServiceWorkerUpdateViaCache | undefined`

The value of the setting used to determine the circumstances in which the browser will consult the HTTP cache when it tries to update the service worker or any scripts that are imported via importScripts(). [ServiceWorkerRegistration.updateViaCache](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/updateViaCache)

### type

`WorkerType | undefined`

The type of the ServiceWorker script to register. [ServiceWorkerRegistration#type](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register#type)

- `classic`: Registers the script as a classic worker. ES module features such as `import` and `export` are NOT allowed in the script.
- `module`: Registers the script as an ES module. Allows use of `import`/`export` syntax and module features.

@default 'classic'

### scope

`string | undefined`

A URL that defines the ServiceWorker's registration scope; that is, what range of URLs it can control. It will be used when calling [ServiceWorkerContainer#register()](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register).

### registrationStrategy

`string | (() => Observable<unknown>) | undefined`

Defines the ServiceWorker registration strategy, which determines when it will be registered with the browser.

The default behavior of registering once the application stabilizes (i.e. as soon as there are no pending micro- and macro-tasks) is designed to register the ServiceWorker as soon as possible but without affecting the application's first time load.

Still, there might be cases where you want more control over when the ServiceWorker is registered (for example, there might be a long-running timeout or polling interval, preventing the app from stabilizing). The available option are:

- `registerWhenStable:<timeout>`: Register as soon as the application stabilizes (no pending micro-/macro-tasks) but no later than `<timeout>` milliseconds. If the app hasn't stabilized after `<timeout>` milliseconds (for example, due to a recurrent asynchronous task), the ServiceWorker will be registered anyway. If `<timeout>` is omitted, the ServiceWorker will only be registered once the app stabilizes.
- `registerImmediately`: Register immediately.
- `registerWithDelay:<timeout>`: Register with a delay of `<timeout>` milliseconds. For example, use `registerWithDelay:5000` to register the ServiceWorker after 5 seconds. If `<timeout>` is omitted, is defaults to `0`, which will register the ServiceWorker as soon as possible but still asynchronously, once all pending micro-tasks are completed.
- An Observable factory function: A function that returns an `Observable`. The function will be used at runtime to obtain and subscribe to the `Observable` and the ServiceWorker will be registered as soon as the first value is emitted.

Default: 'registerWhenStable:30000'

## Description

Token that can be used to provide options for [`ServiceWorkerModule`](serviceworkermodule) outside of [`ServiceWorkerModule.register()`](serviceworkermodule#register).

You can use this token to define a provider that generates the registration options at runtime, for example via a function call:

{@example service-worker/registration-options/module.ts region="registration-options" header="app.module.ts"}

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/service-worker/SwRegistrationOptions>
