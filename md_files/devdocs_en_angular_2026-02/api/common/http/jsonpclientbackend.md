# JsonpClientBackend

JsonpClientBackend



# JsonpClientBackend

Processes an [`HttpRequest`](httprequest) with the JSONP method, by performing JSONP style requests.

[HttpHandler](httphandler)[HttpXhrBackend](httpxhrbackend)

## API

```
class JsonpClientBackend implements HttpBackend {
  constructor(callbackMap: JsonpCallbackContext, document: any): JsonpClientBackend;
  handle(req: HttpRequest<never>): Observable<HttpEvent<any>>;
}
```

### constructor

`JsonpClientBackend`

@paramcallbackMap`JsonpCallbackContext`

@paramdocument`any`

@returns`JsonpClientBackend`

### handle

`Observable<HttpEvent<any>>`

Processes a JSONP request and returns an event stream of the results.

@paramreq`HttpRequest<never>`

The request object.

@returns`Observable<HttpEvent<any>>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/JsonpClientBackend>
