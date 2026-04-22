# withXsrfConfiguration

withXsrfConfiguration



# withXsrfConfiguration

Customizes the XSRF protection for the configuration of the current [`HttpClient`](httpclient) instance.

[provideHttpClient](providehttpclient)

## API

```
function withXsrfConfiguration({
  cookieName,
  headerName,
}: {
  cookieName?: string | undefined;
  headerName?: string | undefined;
}): HttpFeature<HttpFeatureKind.CustomXsrfConfiguration>;
```

### withXsrfConfiguration

`HttpFeature<HttpFeatureKind.CustomXsrfConfiguration>`

Customizes the XSRF protection for the configuration of the current [`HttpClient`](httpclient) instance.

This feature is incompatible with the [`withNoXsrfProtection`](withnoxsrfprotection) feature.

@param{ cookieName, headerName, }`{ cookieName?: string | undefined; headerName?: string | undefined; }`

@returns`HttpFeature<HttpFeatureKind.CustomXsrfConfiguration>`

## Description

Customizes the XSRF protection for the configuration of the current [`HttpClient`](httpclient) instance.

This feature is incompatible with the [`withNoXsrfProtection`](withnoxsrfprotection) feature.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withXsrfConfiguration>
