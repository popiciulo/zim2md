# ServerRoutePrerender

ServerRoutePrerender



# ServerRoutePrerender

A server route that uses Static Site Generation (SSG) mode.

[RenderMode](rendermode)

## API

```
interface ServerRoutePrerender extends Omit<ServerRouteCommon, 'status'> {
  renderMode: RenderMode.Prerender;
  fallback?: undefined;
  override path: string;
  override headers?: Record<string, string> | undefined;
}
```

### renderMode

`RenderMode.Prerender`

Specifies that the route uses Static Site Generation (SSG) mode.

### fallback

`undefined`

Fallback cannot be specified unless `getPrerenderParams` is used.

### path

`string`

The path associated with this route.

### headers

`Record<string, string> | undefined`

Optional additional headers to include in the response for this route.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/ServerRoutePrerender>
