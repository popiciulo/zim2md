# CommonEngine

CommonEngine



# CommonEngine

A common engine to use to server render an application.

## API

```
class CommonEngine {
  constructor(options?: CommonEngineOptions | undefined): CommonEngine;
  render(opts: CommonEngineRenderOptions): Promise<string>;
}
```

### constructor

`CommonEngine`

@paramoptions`CommonEngineOptions | undefined`

@returns`CommonEngine`

### render

`Promise<string>`

Render an HTML document for a specific URL with specified render options

@paramopts`CommonEngineRenderOptions`

@returns`Promise<string>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/CommonEngine>
