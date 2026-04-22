# createNodeRequestHandler

createNodeRequestHandler



# createNodeRequestHandler

Attaches metadata to the handler function to mark it as a special handler for Node.js environments.

## API

```
function createNodeRequestHandler<T extends NodeRequestHandlerFunction>(
  handler: T,
): T;
```

### createNodeRequestHandler

`T`

Attaches metadata to the handler function to mark it as a special handler for Node.js environments.

@paramhandler`T`

- The handler function to be defined and annotated.

@returns`T`

Usage notes

Usage in an Express application:

```
const app = express();
export default createNodeRequestHandler(app);
```

Usage in a Hono application:

```
const app = new Hono();
export default createNodeRequestHandler(async (req, res, next) => {
  try {
    const webRes = await app.fetch(createWebRequestFromNodeRequest(req));
    if (webRes) {
      await writeResponseToNodeResponse(webRes, res);
    } else {
      next();
    }
  } catch (error) {
    next(error);
  }
});
```

Usage in a Fastify application:

```
const app = Fastify();
export default createNodeRequestHandler(async (req, res) => {
  await app.ready();
  app.server.emit('request', req, res);
});
```

## Usage Notes

Usage in an Express application:

```
const app = express();
export default createNodeRequestHandler(app);
```

Usage in a Hono application:

```
const app = new Hono();
export default createNodeRequestHandler(async (req, res, next) => {
  try {
    const webRes = await app.fetch(createWebRequestFromNodeRequest(req));
    if (webRes) {
      await writeResponseToNodeResponse(webRes, res);
    } else {
      next();
    }
  } catch (error) {
    next(error);
  }
});
```

Usage in a Fastify application:

```
const app = Fastify();
export default createNodeRequestHandler(async (req, res) => {
  await app.ready();
  app.server.emit('request', req, res);
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/createNodeRequestHandler>
