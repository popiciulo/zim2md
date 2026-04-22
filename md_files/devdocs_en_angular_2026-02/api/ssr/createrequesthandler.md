# createRequestHandler

createRequestHandler



# createRequestHandler

Annotates a request handler function with metadata, marking it as a special handler.

## API

```
function createRequestHandler(
  handler: RequestHandlerFunction,
): RequestHandlerFunction;
```

### createRequestHandler

`RequestHandlerFunction`

Annotates a request handler function with metadata, marking it as a special handler.

@paramhandler`RequestHandlerFunction`

- The request handler function to be annotated.

@returns`RequestHandlerFunction`

Usage notes

Example usage in a Hono application:

```
const app = new Hono();
export default createRequestHandler(app.fetch);
```

Example usage in a H3 application:

```
const app = createApp();
const handler = toWebHandler(app);
export default createRequestHandler(handler);
```

## Usage Notes

Example usage in a Hono application:

```
const app = new Hono();
export default createRequestHandler(app.fetch);
```

Example usage in a H3 application:

```
const app = createApp();
const handler = toWebHandler(app);
export default createRequestHandler(handler);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/createRequestHandler>
