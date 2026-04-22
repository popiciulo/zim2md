# ServerRoutePrerenderWithParams

ServerRoutePrerenderWithParams



# ServerRoutePrerenderWithParams

A server route configuration that uses Static Site Generation (SSG) mode, including support for routes with parameters.

[RenderMode](rendermode)[ServerRoutePrerender](serverrouteprerender)[PrerenderFallback](prerenderfallback)

## API

```
interface ServerRoutePrerenderWithParams extends Omit<ServerRoutePrerender, 'fallback'> {
  fallback?: PrerenderFallback | undefined;
  getPrerenderParams: () => Promise<Record<string, string>[]>;
  override path: string;
  override headers?: Record<string, string> | undefined;
  override renderMode: RenderMode.Prerender;
}
```

### fallback

`PrerenderFallback | undefined`

Optional strategy to use if the SSG path is not pre-rendered. This is especially relevant for routes with parameterized URLs, where some paths may not be pre-rendered at build time.

This property determines how to handle requests for paths that are not pre-rendered:

- [`PrerenderFallback.Server`](prerenderfallback#Server): Use Server-Side Rendering (SSR) to dynamically generate the page at request time.
- [`PrerenderFallback.Client`](prerenderfallback#Client): Use Client-Side Rendering (CSR) to fetch and render the page on the client side.
- [`PrerenderFallback.None`](prerenderfallback#None): No fallback; if the path is not pre-rendered, the server will not handle the request.

@default [`PrerenderFallback.Server`](prerenderfallback#Server) if not provided.

### getPrerenderParams

`() => Promise<Record<string, string>[]>`

A function that returns a Promise resolving to an array of objects, each representing a route path with URL parameters. This function runs in the injector context, allowing access to Angular services and dependencies.

It also works for catch-all routes (e.g., `/**`), where the parameter name will be `**` and the return value will be the segments of the path, such as `/foo/bar`. These routes can also be combined, e.g., `/product/:id/**`, where both a parameterized segment (`:id`) and a catch-all segment (`**`) can be used together to handle more complex paths.

### path

`string`

The path associated with this route.

### headers

`Record<string, string> | undefined`

Optional additional headers to include in the response for this route.

### renderMode

`RenderMode.Prerender`

Specifies that the route uses Static Site Generation (SSG) mode.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/ServerRoutePrerenderWithParams>
