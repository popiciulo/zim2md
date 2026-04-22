# withNoXsrfProtection

withNoXsrfProtection



# withNoXsrfProtection

Disables XSRF protection in the configuration of the current [`HttpClient`](httpclient) instance.

[provideHttpClient](providehttpclient)

## API

```
function withNoXsrfProtection(): HttpFeature<HttpFeatureKind.NoXsrfProtection>;
```

### withNoXsrfProtection

`HttpFeature<HttpFeatureKind.NoXsrfProtection>`

Disables XSRF protection in the configuration of the current [`HttpClient`](httpclient) instance.

This feature is incompatible with the [`withXsrfConfiguration`](withxsrfconfiguration) feature.

@returns`HttpFeature<HttpFeatureKind.NoXsrfProtection>`

## Description

Disables XSRF protection in the configuration of the current [`HttpClient`](httpclient) instance.

This feature is incompatible with the [`withXsrfConfiguration`](withxsrfconfiguration) feature.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withNoXsrfProtection>
