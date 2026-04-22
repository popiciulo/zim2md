# ServerRouteClient

ServerRouteClient



# ServerRouteClient

A server route that uses Client-Side Rendering (CSR) mode.

[RenderMode](rendermode)

## API

```
interface ServerRouteClient extends ServerRouteCommon {
  renderMode: RenderMode.Client;
  override path: string;
  override headers?: Record<string, string> | undefined;
  override status?: number | undefined;
}
```

### renderMode

`RenderMode.Client`

Specifies that the route uses Client-Side Rendering (CSR) mode.

### path

`string`

The path associated with this route.

### headers

`Record<string, string> | undefined`

Optional additional headers to include in the response for this route.

### status

`number | undefined`

Optional status code to return for this route.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/ServerRouteClient>
