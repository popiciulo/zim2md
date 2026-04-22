# HttpHandler

HttpHandler



# HttpHandler

Transforms an [`HttpRequest`](httprequest) into a stream of [`HttpEvent`](httpevent)s, one of which will likely be a [`HttpResponse`](httpresponse).

## API

```
abstract class HttpHandler {
  abstract handle(req: HttpRequest<any>): Observable<HttpEvent<any>>;
}
```

### handle

`Observable<HttpEvent<any>>`

@paramreq`HttpRequest<any>`

@returns`Observable<HttpEvent<any>>`

## Description

Transforms an [`HttpRequest`](httprequest) into a stream of [`HttpEvent`](httpevent)s, one of which will likely be a [`HttpResponse`](httpresponse).

[`HttpHandler`](httphandler) is injectable. When injected, the handler instance dispatches requests to the first interceptor in the chain, which dispatches to the second, etc, eventually reaching the [`HttpBackend`](httpbackend).

In an [`HttpInterceptor`](httpinterceptor), the [`HttpHandler`](httphandler) parameter is the next interceptor in the chain.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpHandler>
