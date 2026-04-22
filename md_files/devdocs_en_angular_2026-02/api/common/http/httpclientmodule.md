# HttpClientModule

HttpClientModule



# HttpClientModule

Configures the dependency injector for [`HttpClient`](httpclient) with supporting services for XSRF. Automatically imported by [`HttpClientModule`](httpclientmodule).

Deprecation warning

use `provideHttpClient(withInterceptorsFromDi())` as providers instead

## API

```
class HttpClientModule {
}
```

## Description

Configures the dependency injector for [`HttpClient`](httpclient) with supporting services for XSRF. Automatically imported by [`HttpClientModule`](httpclientmodule).

You can add interceptors to the chain behind [`HttpClient`](httpclient) by binding them to the multiprovider for built-in DI token [`HTTP_INTERCEPTORS`](http_interceptors).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpClientModule>
