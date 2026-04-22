# HttpHeaderResponse

HttpHeaderResponse



# HttpHeaderResponse

A partial HTTP response which only includes the status and header data, but no response body.

[Receiving raw progress events](../../../guide/http/making-requests#receiving-raw-progress-events)

## API

```
class HttpHeaderResponse extends HttpResponseBase {
  constructor(init?: { headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; }): HttpHeaderResponse;
  readonly type: HttpEventType.ResponseHeader;
  clone(update?: { headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; }): HttpHeaderResponse;
  readonly override headers: HttpHeaders;
  readonly override status: number;
  readonly override statusText: string;
  readonly override url: string | null;
  readonly override ok: boolean;
  readonly override redirected?: boolean | undefined;
  readonly override responseType?: ResponseType | undefined;
}
```

### constructor

`HttpHeaderResponse`

Create a new [`HttpHeaderResponse`](httpheaderresponse) with the given parameters.

@paraminit`{ headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; }`

@returns`HttpHeaderResponse`

### type

`HttpEventType.ResponseHeader`

### clone

`HttpHeaderResponse`

Copy this [`HttpHeaderResponse`](httpheaderresponse), overriding its contents with the given parameter hash.

@paramupdate`{ headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; }`

@returns`HttpHeaderResponse`

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

## Description

A partial HTTP response which only includes the status and header data, but no response body.

[`HttpHeaderResponse`](httpheaderresponse) is a [`HttpEvent`](httpevent) available on the response event stream, only when progress events are requested.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpHeaderResponse>
