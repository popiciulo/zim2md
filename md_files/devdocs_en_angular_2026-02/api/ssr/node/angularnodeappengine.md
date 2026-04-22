# AngularNodeAppEngine

AngularNodeAppEngine



# AngularNodeAppEngine

Angular server application engine. Manages Angular server applications (including localized ones), handles rendering requests, and optionally transforms index HTML before rendering.

## API

```
class AngularNodeAppEngine {
  handle(request: any, requestContext?: unknown): Promise<Response | null>;
}
```

### handle

`Promise<Response | null>`

Handles an incoming HTTP request by serving prerendered content, performing server-side rendering, or delivering a static file for client-side rendered routes based on the `RenderMode` setting.

This method adapts Node.js's `IncomingMessage` or `Http2ServerRequest` to a format compatible with the `AngularAppEngine` and delegates the handling logic to it.

@paramrequest`any`

- The incoming HTTP request (`IncomingMessage` or `Http2ServerRequest`).

@paramrequestContext`unknown`

- Optional context for rendering, such as metadata associated with the request.

@returns`Promise<Response | null>`

Usage notes

A request to `https://www.example.com/page/index.html` will serve or render the Angular route corresponding to `https://www.example.com/page`.

## Usage Notes

This class should be instantiated once and used as a singleton across the server-side application to ensure consistent handling of rendering requests and resource management.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/AngularNodeAppEngine>
