# HttpResponseBase

HttpResponseBase



# HttpResponseBase

Base class for both [`HttpResponse`](httpresponse) and [`HttpHeaderResponse`](httpheaderresponse).

## API

```
abstract class HttpResponseBase {
  constructor(init: { headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }, defaultStatus?: number, defaultStatusText?: string): HttpResponseBase;
  readonly headers: HttpHeaders;
  readonly status: number;
  readonly statusText: string;
  readonly url: string | null;
  readonly ok: boolean;
  readonly type: HttpEventType.ResponseHeader | HttpEventType.Response;
  readonly redirected?: boolean | undefined;
  readonly responseType?: ResponseType | undefined;
}
```

### constructor

`HttpResponseBase`

Super-constructor for all responses.

The single parameter accepted is an initialization hash. Any properties of the response passed there will override the default values.

@paraminit`{ headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }`

@paramdefaultStatus`number`

@paramdefaultStatusText`string`

@returns`HttpResponseBase`

### headers

`HttpHeaders`

All response headers.

### status

`number`

Response status code.

### statusText

`string`

@deprecated

With HTTP/2 and later versions, this will incorrectly remain set to 'OK' even when the status code of a response is not 200.

Textual description of response status code, defaults to OK.

Do not depend on this.

### url

`string | null`

URL of the resource retrieved, or null if not available.

### ok

`boolean`

Whether the status code falls in the 2xx range.

### type

`HttpEventType.ResponseHeader | HttpEventType.Response`

Type of the response, narrowed to either the full response or the header.

### redirected

`boolean | undefined`

Indicates whether the HTTP response was redirected during the request. This property is only available when using the Fetch API using [`withFetch()`](withfetch) When using the default XHR Request this property will be `undefined`

### responseType

`ResponseType | undefined`

Indicates the type of the HTTP response, based on how the request was made and how the browser handles the response.

This corresponds to the `type` property of the Fetch API's `Response` object, which can indicate values such as:

- `'basic'`: A same-origin response, allowing full access to the body and headers.
- `'cors'`: A cross-origin response with CORS enabled, exposing only safe response headers.
- `'opaque'`: A cross-origin response made with `no-cors`, where the response body and headers are inaccessible.
- `'opaqueredirect'`: A response resulting from a redirect followed in `no-cors` mode.
- `'error'`: A response representing a network error or similar failure.

This property is only available when using the Fetch-based backend (via [`withFetch()`](withfetch)). When using Angular's (XHR) backend, this value will be `undefined`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResponseBase>
