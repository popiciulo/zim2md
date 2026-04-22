# withInterceptorsFromDi

withInterceptorsFromDi



# withInterceptorsFromDi

Includes class-based interceptors configured using a multi-provider in the current injector into the configured [`HttpClient`](httpclient) instance.

[HttpInterceptor](httpinterceptor)[HTTP\_INTERCEPTORS](http_interceptors)[provideHttpClient](providehttpclient)

## API

```
function withInterceptorsFromDi(): HttpFeature<HttpFeatureKind.LegacyInterceptors>;
```

### withInterceptorsFromDi

`HttpFeature<HttpFeatureKind.LegacyInterceptors>`

Includes class-based interceptors configured using a multi-provider in the current injector into the configured [`HttpClient`](httpclient) instance.

Prefer [`withInterceptors`](withinterceptors) and functional interceptors instead, as support for DI-provided interceptors may be phased out in a later release.

@returns`HttpFeature<HttpFeatureKind.LegacyInterceptors>`

## Description

Includes class-based interceptors configured using a multi-provider in the current injector into the configured [`HttpClient`](httpclient) instance.

Prefer [`withInterceptors`](withinterceptors) and functional interceptors instead, as support for DI-provided interceptors may be phased out in a later release.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withInterceptorsFromDi>
