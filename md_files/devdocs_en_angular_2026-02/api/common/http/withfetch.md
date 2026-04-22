# withFetch

withFetch



# withFetch

Configures the current [`HttpClient`](httpclient) instance to make requests using the fetch API.

[Advanced fetch Options](../../../guide/http/making-requests#advanced-fetch-options)

## API

```
function withFetch(): HttpFeature<HttpFeatureKind.Fetch>;
```

### withFetch

`HttpFeature<HttpFeatureKind.Fetch>`

Configures the current [`HttpClient`](httpclient) instance to make requests using the fetch API.

Note: The Fetch API doesn't support progress report on uploads.

@returns`HttpFeature<HttpFeatureKind.Fetch>`

## Description

Configures the current [`HttpClient`](httpclient) instance to make requests using the fetch API.

Note: The Fetch API doesn't support progress report on uploads.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/withFetch>
