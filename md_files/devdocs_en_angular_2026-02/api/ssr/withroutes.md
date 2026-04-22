# withRoutes

withRoutes



# withRoutes

Configures server-side routing for the application.

[provideServerRendering](provideserverrendering)[ServerRoute](serverroute)

## API

```
function withRoutes(
  routes: ServerRoute[],
): ServerRenderingFeature<ServerRenderingFeatureKind.ServerRoutes>;
```

### withRoutes

`ServerRenderingFeature<ServerRenderingFeatureKind.ServerRoutes>`

Configures server-side routing for the application.

This function registers an array of [`ServerRoute`](serverroute) definitions, enabling server-side rendering for specific URL paths. These routes are used to pre-render content on the server, improving initial load performance and SEO.

@paramroutes`ServerRoute[]`

- An array of [`ServerRoute`](serverroute) objects, each defining a server-rendered route.

@returns`ServerRenderingFeature<ServerRenderingFeatureKind.ServerRoutes>`

Usage notes

```
import { provideServerRendering, withRoutes, ServerRoute, RenderMode } from '@angular/ssr';

const serverRoutes: ServerRoute[] = [
  {
    path: '', // This renders the "/" route on the client (CSR)
    renderMode: RenderMode.Client,
  },
  {
    path: 'about', // This page is static, so we prerender it (SSG)
    renderMode: RenderMode.Prerender,
  },
  {
    path: 'profile', // This page requires user-specific data, so we use SSR
    renderMode: RenderMode.Server,
  },
  {
    path: '**', // All other routes will be rendered on the server (SSR)
    renderMode: RenderMode.Server,
  },
];

provideServerRendering(withRoutes(serverRoutes));
```

## Description

Configures server-side routing for the application.

This function registers an array of [`ServerRoute`](serverroute) definitions, enabling server-side rendering for specific URL paths. These routes are used to pre-render content on the server, improving initial load performance and SEO.

## Usage Notes

```
import { provideServerRendering, withRoutes, ServerRoute, RenderMode } from '@angular/ssr';

const serverRoutes: ServerRoute[] = [
  {
    path: '', // This renders the "/" route on the client (CSR)
    renderMode: RenderMode.Client,
  },
  {
    path: 'about', // This page is static, so we prerender it (SSG)
    renderMode: RenderMode.Prerender,
  },
  {
    path: 'profile', // This page requires user-specific data, so we use SSR
    renderMode: RenderMode.Server,
  },
  {
    path: '**', // All other routes will be rendered on the server (SSR)
    renderMode: RenderMode.Server,
  },
];

provideServerRendering(withRoutes(serverRoutes));
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/withRoutes>
