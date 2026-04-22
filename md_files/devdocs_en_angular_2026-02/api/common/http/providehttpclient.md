# provideHttpClient

provideHttpClient



# provideHttpClient

Configures Angular's [`HttpClient`](httpclient) service to be available for injection.

[HTTP Client](../../../guide/http/setup)[withInterceptors](withinterceptors)[withInterceptorsFromDi](withinterceptorsfromdi)[withXsrfConfiguration](withxsrfconfiguration)[withNoXsrfProtection](withnoxsrfprotection)[withJsonpSupport](withjsonpsupport)[withRequestsMadeViaParent](withrequestsmadeviaparent)[withFetch](withfetch)

## API

```
function provideHttpClient(
  ...features: HttpFeature<HttpFeatureKind>[]
): EnvironmentProviders;
```

### provideHttpClient

`EnvironmentProviders`

Configures Angular's [`HttpClient`](httpclient) service to be available for injection.

By default, [`HttpClient`](httpclient) will be configured for injection with its default options for XSRF protection of outgoing requests. Additional configuration options can be provided by passing feature functions to [`provideHttpClient`](providehttpclient). For example, HTTP interceptors can be added using the `withInterceptors(...)` feature.

It's strongly recommended to enable [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for applications that use Server-Side Rendering for better performance and compatibility. To enable `fetch`, add [`withFetch()`](withfetch) feature to the [`provideHttpClient()`](providehttpclient) call at the root of the application:

```
provideHttpClient(withFetch());
```

@paramfeatures`HttpFeature<HttpFeatureKind>[]`

@returns`EnvironmentProviders`

## Description

Configures Angular's [`HttpClient`](httpclient) service to be available for injection.

By default, [`HttpClient`](httpclient) will be configured for injection with its default options for XSRF protection of outgoing requests. Additional configuration options can be provided by passing feature functions to [`provideHttpClient`](providehttpclient). For example, HTTP interceptors can be added using the `withInterceptors(...)` feature.

It's strongly recommended to enable [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for applications that use Server-Side Rendering for better performance and compatibility. To enable `fetch`, add [`withFetch()`](withfetch) feature to the [`provideHttpClient()`](providehttpclient) call at the root of the application:

```
provideHttpClient(withFetch());
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/provideHttpClient>
