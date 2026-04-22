# HttpInterceptor

HttpInterceptor



# HttpInterceptor

Intercepts and handles an [`HttpRequest`](httprequest) or [`HttpResponse`](httpresponse).

[HTTP Guide](../../../guide/http/interceptors)[HttpInterceptorFn](httpinterceptorfn)

## API

```
interface HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>;
}
```

### intercept

`Observable<HttpEvent<any>>`

Identifies and handles a given HTTP request.

@paramreq`HttpRequest<any>`

The outgoing request object to handle.

@paramnext`HttpHandler`

The next interceptor in the chain, or the backend if no interceptors remain in the chain.

@returns`Observable<HttpEvent<any>>`

## Description

Intercepts and handles an [`HttpRequest`](httprequest) or [`HttpResponse`](httpresponse).

Most interceptors transform the outgoing request before passing it to the next interceptor in the chain, by calling `next.handle(transformedReq)`. An interceptor may transform the response event stream as well, by applying additional RxJS operators on the stream returned by `next.handle()`.

More rarely, an interceptor may handle the request entirely, and compose a new event stream instead of invoking `next.handle()`. This is an acceptable behavior, but keep in mind that further interceptors will be skipped entirely.

It is also rare but valid for an interceptor to return multiple responses on the event stream for a single request.

## Usage Notes

To use the same instance of `HttpInterceptors` for the entire app, import the [`HttpClientModule`](httpclientmodule) only in your `AppModule`, and add the interceptors to the root application injector. If you import [`HttpClientModule`](httpclientmodule) multiple times across different modules (for example, in lazy loading modules), each import creates a new copy of the [`HttpClientModule`](httpclientmodule), which overwrites the interceptors provided in the root module.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpInterceptor>
