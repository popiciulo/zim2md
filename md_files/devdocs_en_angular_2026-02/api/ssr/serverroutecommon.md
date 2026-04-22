# ServerRouteCommon

ServerRouteCommon



# ServerRouteCommon

Common interface for server routes, providing shared properties.

## API

```
interface ServerRouteCommon {
  path: string;
  headers?: Record<string, string> | undefined;
  status?: number | undefined;
}
```

### path

`string`

The path associated with this route.

### headers

`Record<string, string> | undefined`

Optional additional headers to include in the response for this route.

### status

`number | undefined`

Optional status code to return for this route.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/ServerRouteCommon>
