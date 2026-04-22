# ServerRouteServer

ServerRouteServer



# ServerRouteServer

A server route that uses Server-Side Rendering (SSR) mode.

[RenderMode](rendermode)

## API

```
interface ServerRouteServer extends ServerRouteCommon {
  renderMode: RenderMode.Server;
  override path: string;
  override headers?: Record<string, string> | undefined;
  override status?: number | undefined;
}
```

### renderMode

`RenderMode.Server`

Specifies that the route uses Server-Side Rendering (SSR) mode.

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
<https://angular.dev/api/ssr/ServerRouteServer>
