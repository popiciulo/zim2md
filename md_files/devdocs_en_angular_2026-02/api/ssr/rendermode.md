# RenderMode

RenderMode



# RenderMode

Different rendering modes for server routes.

[withRoutes](withroutes)[ServerRoute](serverroute)

## API

```
enum RenderMode {
  Server: RenderMode.Server;
  Client: RenderMode.Client;
  Prerender: RenderMode.Prerender;
}
```

### Server

Server-Side Rendering (SSR) mode, where content is rendered on the server for each request.

### Client

Client-Side Rendering (CSR) mode, where content is rendered on the client side in the browser.

### Prerender

Static Site Generation (SSG) mode, where content is pre-rendered at build time and served as static files.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/RenderMode>
