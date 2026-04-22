# HTTP_TRANSFER_CACHE_ORIGIN_MAP

HTTP\_TRANSFER\_CACHE\_ORIGIN\_MAP



# HTTP\_TRANSFER\_CACHE\_ORIGIN\_MAP

If your application uses different HTTP origins to make API calls (via [`HttpClient`](httpclient)) on the server and on the client, the [`HTTP_TRANSFER_CACHE_ORIGIN_MAP`](http_transfer_cache_origin_map) token allows you to establish a mapping between those origins, so that `HttpTransferCache` feature can recognize those requests as the same ones and reuse the data cached on the server during hydration on the client.

## API

```
const HTTP_TRANSFER_CACHE_ORIGIN_MAP: InjectionToken<Record<string, string>>;
```

## Description

If your application uses different HTTP origins to make API calls (via [`HttpClient`](httpclient)) on the server and on the client, the [`HTTP_TRANSFER_CACHE_ORIGIN_MAP`](http_transfer_cache_origin_map) token allows you to establish a mapping between those origins, so that `HttpTransferCache` feature can recognize those requests as the same ones and reuse the data cached on the server during hydration on the client.

**Important note**: the [`HTTP_TRANSFER_CACHE_ORIGIN_MAP`](http_transfer_cache_origin_map) token should *only* be provided in the *server* code of your application (typically in the `app.server.config.ts` script). Angular throws an error if it detects that the token is defined while running on the client.

## Usage Notes

When the same API endpoint is accessed via `http://internal-domain.com:8080` on the server and via `https://external-domain.com` on the client, you can use the following configuration:

```
// in app.server.config.ts
{
    provide: HTTP_TRANSFER_CACHE_ORIGIN_MAP,
    useValue: {
        'http://internal-domain.com:8080': 'https://external-domain.com'
    }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HTTP_TRANSFER_CACHE_ORIGIN_MAP>
