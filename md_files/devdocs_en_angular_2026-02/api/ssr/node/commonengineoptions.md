# CommonEngineOptions

CommonEngineOptions



# CommonEngineOptions

## API

```
interface CommonEngineOptions {
  bootstrap?: Type<{}> | ((context: BootstrapContext) => Promise<ApplicationRef>) | undefined;
  providers?: StaticProvider[] | undefined;
  enablePerformanceProfiler?: boolean | undefined;
}
```

### bootstrap

`Type<{}> | ((context: BootstrapContext) => Promise<ApplicationRef>) | undefined`

A method that when invoked returns a promise that returns an [`ApplicationRef`](../../core/applicationref) instance once resolved or an NgModule.

### providers

`StaticProvider[] | undefined`

A set of platform level providers for all requests.

### enablePerformanceProfiler

`boolean | undefined`

Enable request performance profiling data collection and printing the results in the server console.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/CommonEngineOptions>
