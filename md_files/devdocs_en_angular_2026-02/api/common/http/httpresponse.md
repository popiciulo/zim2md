# HttpResponse

HttpResponse



# HttpResponse

A full HTTP response, including a typed response body (which may be `null` if one was not returned).

[Interacting with the server response events](../../../guide/http/making-requests#interacting-with-the-server-response-events)

## API

```
class HttpResponse<T> extends HttpResponseBase {
  constructor(init?: { body?: T | null | undefined; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }): HttpResponse<T>;
  readonly body: T | null;
  readonly type: HttpEventType.Response;
  clone(): HttpResponse<T>;
  clone(update: { headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }): HttpResponse<T>;
  clone<V>(update: { body?: V | null | undefined; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }): HttpResponse<V>;
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

`HttpResponse<T>`

Construct a new [`HttpResponse`](httpresponse).

@paraminit`{ body?: T | null | undefined; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }`

@returns`HttpResponse<T>`

### body

`T | null`

The response body, or `null` if one was not returned.

### type

`HttpEventType.Response`

### clone

3 overloads

@returns`HttpResponse<T>`

@paramupdate`{ headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }`

@returns`HttpResponse<T>`

@paramupdate`{ body?: V | null | undefined; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }`

@returns`HttpResponse<V>`

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

A full HTTP response, including a typed response body (which may be `null` if one was not returned).

[`HttpResponse`](httpresponse) is a [`HttpEvent`](httpevent) available on the response event stream.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResponse>
