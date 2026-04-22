# HttpBackend

HttpBackend



# HttpBackend

A final [`HttpHandler`](httphandler) which will dispatch the request via browser HTTP APIs to a backend.

## API

```
abstract class HttpBackend implements HttpHandler {
  abstract handle(req: HttpRequest<any>): Observable<HttpEvent<any>>;
}
```

### handle

`Observable<HttpEvent<any>>`

@paramreq`HttpRequest<any>`

@returns`Observable<HttpEvent<any>>`

## Description

A final [`HttpHandler`](httphandler) which will dispatch the request via browser HTTP APIs to a backend.

Interceptors sit between the [`HttpClient`](httpclient) interface and the [`HttpBackend`](httpbackend).

When injected, [`HttpBackend`](httpbackend) dispatches requests directly to the backend, without going through the interceptor chain.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpBackend>
