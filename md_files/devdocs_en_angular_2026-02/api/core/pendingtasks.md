# PendingTasks

PendingTasks



# PendingTasks

Service that keeps track of pending tasks contributing to the stableness of Angular application. While several existing Angular services (ex.: `HttpClient`) will internally manage tasks influencing stability, this API gives control over stability to library and application developers for specific cases not covered by Angular internals.

[PendingTasks for Server Side Rendering (SSR)](../../guide/zoneless#pendingtasks-for-server-side-rendering-ssr)

## API

```
class PendingTasks {
  add(): () => void;
  run(fn: () => Promise<unknown>): void;
}
```

### add

`() => void`

Adds a new task that should block application's stability.

@returns`() => void`

### run

`void`

Runs an asynchronous function and blocks the application's stability until the function completes.

```
pendingTasks.run(async () => {
  const userData = await fetch('/api/user');
  this.userData.set(userData);
});
```

@paramfn`() => Promise<unknown>`

The asynchronous function to execute

@returns`void`

## Description

Service that keeps track of pending tasks contributing to the stableness of Angular application. While several existing Angular services (ex.: `HttpClient`) will internally manage tasks influencing stability, this API gives control over stability to library and application developers for specific cases not covered by Angular internals.

The concept of stability comes into play in several important scenarios:

- SSR process needs to wait for the application stability before serializing and sending rendered HTML;
- tests might want to delay assertions until the application becomes stable;

## Usage Notes

```
const pendingTasks = inject(PendingTasks);
const taskCleanup = pendingTasks.add();
// do work that should block application's stability and then:
taskCleanup();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/PendingTasks>
