# withRequestsMadeViaParent

withRequestsMadeViaParent



# withRequestsMadeViaParent

Configures the current [`HttpClient`](httpclient) instance to make requests via the parent injector's [`HttpClient`](httpclient) instead of directly.

[HTTP client setup](../../../guide/http/setup#withrequestsmadeviaparent)[provideHttpClient](providehttpclient)

## API

```
function withRequestsMadeViaParent(): HttpFeature<HttpFeatureKind.RequestsMadeViaParent>;
```

### withRequestsMadeViaParent

`HttpFeature<HttpFeatureKind.RequestsMadeViaParent>`

Configures the current [`HttpClient`](httpclient) instance to make requests via the parent injector's [`HttpClient`](httpclient) instead of directly.

By default, [`provideHttpClient`](providehttpclient) configures [`HttpClient`](httpclient) in its injector to be an independent instance. For example, even if [`HttpClient`](httpclient) is configured in the parent injector with one or more interceptors, they will not intercept requests made via this instance.

With this option enabled, once the request has passed through the current injector's interceptors, it will be delegated to the parent injector's [`HttpClient`](httpclient) chain instead of dispatched directly, and interceptors in the parent configuration will be applied to the request.

If there are several [`HttpClient`](httpclient) instances in the injector hierarchy, it's possible for [`withRequestsMadeViaParent`](withrequestsmadeviaparent) to be used at multiple levels, which will cause the request to "bubble up" until either reaching the root level or an [`HttpClient`](httpclient) which was not configured with this option.

@returns`HttpFeature<HttpFeatureKind.RequestsMadeViaParent>`

## Description

Configures the current [`HttpClient`](httpclient) instance to make requests via the parent injector's [`HttpClient`](httpclient) instead of directly.

By default, [`provideHttpClient`](providehttpclient) configures [`HttpClient`](httpclient) in its injector to be an independent instance. For example, even if [`HttpClient`](httpclient) is configured in the parent injector with one or more interceptors, they will not intercept requests made via this instance.

With this option enabled, once the request has passed through the current injector's interceptors, it will be delegated to the parent injector's [`HttpClient`](httpclient) chain instead of dispatched directly, and interceptors in the parent configuration will be applied to the request.

If there are several [`HttpClient`](httpclient) instances in the injector hierarchy, it's possible for [`withRequestsMadeViaParent`](withrequestsmadeviaparent) to be used at multiple levels, which will cause the request to "bubble up" until either reaching the root level or an [`HttpClient`](httpclient) which was not configured with this option.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withRequestsMadeViaParent>
