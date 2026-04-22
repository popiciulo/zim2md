# withInterceptors

withInterceptors



# withInterceptors

Adds one or more functional-style HTTP interceptors to the configuration of the [`HttpClient`](httpclient) instance.

[HttpInterceptorFn](httpinterceptorfn)[provideHttpClient](providehttpclient)

## API

```
function withInterceptors(
  interceptorFns: HttpInterceptorFn[],
): HttpFeature<HttpFeatureKind.Interceptors>;
```

### withInterceptors

`HttpFeature<HttpFeatureKind.Interceptors>`

Adds one or more functional-style HTTP interceptors to the configuration of the [`HttpClient`](httpclient) instance.

@paraminterceptorFns`HttpInterceptorFn[]`

@returns`HttpFeature<HttpFeatureKind.Interceptors>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withInterceptors>
