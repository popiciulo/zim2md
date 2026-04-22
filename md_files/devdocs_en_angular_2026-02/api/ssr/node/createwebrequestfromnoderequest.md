# createWebRequestFromNodeRequest

createWebRequestFromNodeRequest



# createWebRequestFromNodeRequest

Converts a Node.js `IncomingMessage` or `Http2ServerRequest` into a Web Standard `Request` object.

## API

```
function createWebRequestFromNodeRequest(nodeRequest: any): Request;
```

### createWebRequestFromNodeRequest

`Request`

Converts a Node.js `IncomingMessage` or `Http2ServerRequest` into a Web Standard `Request` object.

This function adapts the Node.js request objects to a format that can be used by web platform APIs.

@paramnodeRequest`any`

- The Node.js request object (`IncomingMessage` or `Http2ServerRequest`) to convert.

@returns`Request`

## Description

Converts a Node.js `IncomingMessage` or `Http2ServerRequest` into a Web Standard `Request` object.

This function adapts the Node.js request objects to a format that can be used by web platform APIs.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/node/createWebRequestFromNodeRequest>
