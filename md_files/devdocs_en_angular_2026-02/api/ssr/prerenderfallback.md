# PrerenderFallback

PrerenderFallback



# PrerenderFallback

Defines the fallback strategies for Static Site Generation (SSG) routes when a pre-rendered path is not available. This is particularly relevant for routes with parameterized URLs where some paths might not be pre-rendered at build time.

[ServerRoutePrerenderWithParams](serverrouteprerenderwithparams)

## API

```
enum PrerenderFallback {
  Server: PrerenderFallback.Server;
  Client: PrerenderFallback.Client;
  None: PrerenderFallback.None;
}
```

### Server

Fallback to Server-Side Rendering (SSR) if the pre-rendered path is not available. This strategy dynamically generates the page on the server at request time.

### Client

Fallback to Client-Side Rendering (CSR) if the pre-rendered path is not available. This strategy allows the page to be rendered on the client side.

### None

No fallback; if the path is not pre-rendered, the server will not handle the request. This means the application will not provide any response for paths that are not pre-rendered.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/PrerenderFallback>
