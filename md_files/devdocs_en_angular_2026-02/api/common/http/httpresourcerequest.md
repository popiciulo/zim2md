# HttpResourceRequest

HttpResourceRequest



# HttpResourceRequest

The structure of an [`httpResource`](httpresource) request which will be sent to the backend.

## API

```
interface HttpResourceRequest {
  url: string;
  method?: string | undefined;
  body?: unknown;
  params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined;
  headers?: HttpHeaders | Record<string, string | readonly string[]> | undefined;
  context?: HttpContext | undefined;
  reportProgress?: boolean | undefined;
  withCredentials?: boolean | undefined;
  keepalive?: boolean | undefined;
  cache?: RequestCache | (string & {}) | undefined;
  credentials?: (string & {}) | RequestCredentials | undefined;
  priority?: (string & {}) | RequestPriority | undefined;
  mode?: (string & {}) | RequestMode | undefined;
  redirect?: (string & {}) | RequestRedirect | undefined;
  referrer?: string | undefined;
  referrerPolicy?: (string & {}) | ReferrerPolicy | undefined;
  integrity?: string | undefined;
  transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined;
  timeout?: number | undefined;
}
```

### url

`string`

URL of the request.

This URL should not include query parameters. Instead, specify query parameters through the `params` field.

### method

`string | undefined`

HTTP method of the request, which defaults to GET if not specified.

### body

`unknown`

Body to send with the request, if there is one.

If no Content-Type header is specified by the user, Angular will attempt to set one based on the type of `body`.

### params

`HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined`

Dictionary of query parameters which will be appeneded to the request URL.

### headers

`HttpHeaders | Record<string, string | readonly string[]> | undefined`

Dictionary of headers to include with the outgoing request.

### context

`HttpContext | undefined`

Context of the request stored in a dictionary of key-value pairs.

### reportProgress

`boolean | undefined`

If `true`, progress events will be enabled for the request and delivered through the `HttpResource.progress` signal.

### withCredentials

`boolean | undefined`

Specifies whether the `withCredentials` flag should be set on the outgoing request.

This flag causes the browser to send cookies and other authentication information along with the request.

### keepalive

`boolean | undefined`

When using the fetch implementation and set to `true`, the browser will not abort the associated request if the page that initiated it is unloaded before the request is complete.

### cache

`RequestCache | (string & {}) | undefined`

Controls how the request will interact with the browser's HTTP cache. This affects whether a response is retrieved from the cache, how it is stored, or if it bypasses the cache altogether.

### credentials

`(string & {}) | RequestCredentials | undefined`

The credentials mode of the request, which determines how cookies and other authentication information are handled. This can affect whether credentials are sent with cross-origin requests or not.

### priority

`(string & {}) | RequestPriority | undefined`

Indicates the relative priority of the request. This may be used by the browser to decide the order in which requests are dispatched and resources fetched.

### mode

`(string & {}) | RequestMode | undefined`

The mode of the request, which determines how the request will interact with the browser's security model. This can affect things like CORS (Cross-Origin Resource Sharing) and same-origin policies.

### redirect

`(string & {}) | RequestRedirect | undefined`

The redirect mode of the request, which determines how redirects are handled. This can affect whether the request follows redirects automatically, or if it fails when a redirect occurs.

### referrer

`string | undefined`

The referrer of the request, which can be used to indicate the origin of the request. This is useful for security and analytics purposes. Value is a same-origin URL, "about:client", or the empty string, to set request's referrer.

### referrerPolicy

`(string & {}) | ReferrerPolicy | undefined`

The referrer policy of the request, which can be used to specify the referrer information to be included with the request. This can affect the amount of referrer information sent with the request, and can be used to enhance privacy and security.

### integrity

`string | undefined`

The integrity metadata of the request, which can be used to ensure the request is made with the expected content. A cryptographic hash of the resource to be fetched by request

### transferCache

`boolean | { includeHeaders?: string[] | undefined; } | undefined`

Configures the server-side rendering transfer cache for this request.

See the documentation on the transfer cache for more information.

### timeout

`number | undefined`

The timeout for the backend HTTP request in ms.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResourceRequest>
