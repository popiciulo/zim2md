# HttpXhrBackend

HttpXhrBackend



# HttpXhrBackend

Uses `XMLHttpRequest` to send requests to a backend server.

[HttpHandler](httphandler)[JsonpClientBackend](jsonpclientbackend)

## API

```
class HttpXhrBackend implements HttpBackend {
  constructor(xhrFactory: XhrFactory): HttpXhrBackend;
  handle(req: HttpRequest<any>): Observable<HttpEvent<any>>;
}
```

### constructor

`HttpXhrBackend`

@paramxhrFactory`XhrFactory`

@returns`HttpXhrBackend`

### handle

`Observable<HttpEvent<any>>`

Processes a request and returns a stream of response events.

@paramreq`HttpRequest<any>`

The request object.

@returns`Observable<HttpEvent<any>>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpXhrBackend>
