# CommonEngineRenderOptions

CommonEngineRenderOptions



# CommonEngineRenderOptions

## API

```
interface CommonEngineRenderOptions {
  bootstrap?: Type<{}> | ((context: BootstrapContext) => Promise<ApplicationRef>) | undefined;
  providers?: StaticProvider[] | undefined;
  url?: string | undefined;
  document?: string | undefined;
  documentFilePath?: string | undefined;
  inlineCriticalCss?: boolean | undefined;
  publicPath?: string | undefined;
}
```

### bootstrap

`Type<{}> | ((context: BootstrapContext) => Promise<ApplicationRef>) | undefined`

A method that when invoked returns a promise that returns an [`ApplicationRef`](../../core/applicationref) instance once resolved or an NgModule.

### providers

`StaticProvider[] | undefined`

A set of platform level providers for the current request.

### url

`string | undefined`

### document

`string | undefined`

### documentFilePath

`string | undefined`

### inlineCriticalCss

`boolean | undefined`

Reduce render blocking requests by inlining critical CSS. Defaults to true.

### publicPath

`string | undefined`

Base path location of index file. Defaults to the 'documentFilePath' dirname when not provided.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/CommonEngineRenderOptions>
