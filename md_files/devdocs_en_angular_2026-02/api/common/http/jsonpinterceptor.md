# JsonpInterceptor

JsonpInterceptor



# JsonpInterceptor

Identifies requests with the method JSONP and shifts them to the [`JsonpClientBackend`](jsonpclientbackend).

[HttpInterceptor](httpinterceptor)

## API

```
class JsonpInterceptor {
  constructor(injector: EnvironmentInjector): JsonpInterceptor;
  intercept(initialRequest: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>;
}
```

### constructor

`JsonpInterceptor`

@paraminjector`EnvironmentInjector`

@returns`JsonpInterceptor`

### intercept

`Observable<HttpEvent<any>>`

Identifies and handles a given JSONP request.

@paraminitialRequest`HttpRequest<any>`

The outgoing request object to handle.

@paramnext`HttpHandler`

The next interceptor in the chain, or the backend if no interceptors remain in the chain.

@returns`Observable<HttpEvent<any>>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/JsonpInterceptor>
