# AngularAppEngine

AngularAppEngine



# AngularAppEngine

Angular server application engine. Manages Angular server applications (including localized ones), handles rendering requests, and optionally transforms index HTML before rendering.

## API

```
class AngularAppEngine {
  handle(request: Request, requestContext?: unknown): Promise<Response | null>;
}
```

### handle

`Promise<Response | null>`

Handles an incoming HTTP request by serving prerendered content, performing server-side rendering, or delivering a static file for client-side rendered routes based on the [`RenderMode`](rendermode) setting.

@paramrequest`Request`

- The HTTP request to handle.

@paramrequestContext`unknown`

- Optional context for rendering, such as metadata associated with the request.

@returns`Promise<Response | null>`

Usage notes

A request to `https://www.example.com/page/index.html` will serve or render the Angular route corresponding to `https://www.example.com/page`.

## Usage Notes

This class should be instantiated once and used as a singleton across the server-side application to ensure consistent handling of rendering requests and resource management.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/AngularAppEngine>
