# HttpInterceptorFn

HttpInterceptorFn



# HttpInterceptorFn

An interceptor for HTTP requests made via [`HttpClient`](httpclient).

[HTTP Guide](../../../guide/http/interceptors)[withInterceptors](withinterceptors)

## API

```
type HttpInterceptorFn = (
  req: HttpRequest<unknown>,
  next: HttpHandlerFn,
) => Observable<HttpEvent<unknown>>
```

## Description

An interceptor for HTTP requests made via [`HttpClient`](httpclient).

[`HttpInterceptorFn`](httpinterceptorfn)s are middleware functions which [`HttpClient`](httpclient) calls when a request is made. These functions have the opportunity to modify the outgoing request or any response that comes back, as well as block, redirect, or otherwise change the request or response semantics.

An [`HttpHandlerFn`](httphandlerfn) representing the next interceptor (or the backend which will make a real HTTP request) is provided. Most interceptors will delegate to this function, but that is not required (see [`HttpHandlerFn`](httphandlerfn) for more details).

[`HttpInterceptorFn`](httpinterceptorfn)s are executed in an [injection context](../../../guide/di/dependency-injection-context). They have access to [`inject()`](../../core/inject) via the [`EnvironmentInjector`](../../core/environmentinjector) from which they were configured.

## Usage Notes

Here is a noop interceptor that passes the request through without modifying it:

```
export const noopInterceptor: HttpInterceptorFn = (req: HttpRequest<unknown>, next:
HttpHandlerFn) => {
  return next(modifiedReq);
};
```

If you want to alter a request, clone it first and modify the clone before passing it to the `next()` handler function.

Here is a basic interceptor that adds a bearer token to the headers

```
export const authenticationInterceptor: HttpInterceptorFn = (req: HttpRequest<unknown>, next:
HttpHandlerFn) => {
   const userToken = 'MY_TOKEN'; const modifiedReq = req.clone({
     headers: req.headers.set('Authorization', `Bearer ${userToken}`),
   });

   return next(modifiedReq);
};
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpInterceptorFn>
