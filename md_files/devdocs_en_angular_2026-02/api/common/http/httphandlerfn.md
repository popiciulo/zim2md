# HttpHandlerFn

HttpHandlerFn



# HttpHandlerFn

Represents the next interceptor in an interceptor chain, or the real backend if there are no further interceptors.

[HTTP Guide](../../../guide/http/interceptors)

## API

```
type HttpHandlerFn = (req: HttpRequest<unknown>) => Observable<HttpEvent<unknown>>
```

## Description

Represents the next interceptor in an interceptor chain, or the real backend if there are no further interceptors.

Most interceptors will delegate to this function, and either modify the outgoing request or the response when it arrives. Within the scope of the current request, however, this function may be called any number of times, for any number of downstream requests. Such downstream requests need not be to the same URL or even the same origin as the current request. It is also valid to not call the downstream handler at all, and process the current request entirely within the interceptor.

This function should only be called within the scope of the request that's currently being intercepted. Once that request is complete, this downstream handler function should not be called.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpHandlerFn>
