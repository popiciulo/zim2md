# writeResponseToNodeResponse

writeResponseToNodeResponse



# writeResponseToNodeResponse

Streams a web-standard `Response` into a Node.js `ServerResponse` or `Http2ServerResponse`.

## API

```
function writeResponseToNodeResponse(
  source: Response,
  destination: any,
): Promise<void>;
```

### writeResponseToNodeResponse

`Promise<void>`

Streams a web-standard `Response` into a Node.js `ServerResponse` or `Http2ServerResponse`.

This function adapts the web `Response` object to write its content to a Node.js response object, handling both HTTP/1.1 and HTTP/2.

@paramsource`Response`

- The web-standard `Response` object to stream from.

@paramdestination`any`

- The Node.js response object (`ServerResponse` or `Http2ServerResponse`) to stream into.

@returns`Promise<void>`

## Description

Streams a web-standard `Response` into a Node.js `ServerResponse` or `Http2ServerResponse`.

This function adapts the web `Response` object to write its content to a Node.js response object, handling both HTTP/1.1 and HTTP/2.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/writeResponseToNodeResponse>
