# HttpErrorResponse

HttpErrorResponse



# HttpErrorResponse

A response that represents an error or failure, either from a non-successful HTTP status, an error while executing the request, or some other failure which occurred during the parsing of the response.

[Handling request failure](../../../guide/http/making-requests#handling-request-failure)

## API

```
class HttpErrorResponse extends HttpResponseBase implements Error {
  constructor(init: { error?: any; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }): HttpErrorResponse;
  readonly name: "HttpErrorResponse";
  readonly message: string;
  readonly error: any;
  readonly ok: false;
  readonly override headers: HttpHeaders;
  readonly override status: number;
  readonly override statusText: string;
  readonly override url: string | null;
  readonly override type: HttpEventType.ResponseHeader | HttpEventType.Response;
  readonly override redirected?: boolean | undefined;
  readonly override responseType?: ResponseType | undefined;
}
```

### constructor

`HttpErrorResponse`

@paraminit`{ error?: any; headers?: HttpHeaders | undefined; status?: number | undefined; statusText?: string | undefined; url?: string | undefined; redirected?: boolean | undefined; responseType?: ResponseType | undefined; }`

@returns`HttpErrorResponse`

### name

`"HttpErrorResponse"`

### message

`string`

### error

`any`

### ok

`false`

Errors are never okay, even when the status code is in the 2xx success range.

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

## Description

A response that represents an error or failure, either from a non-successful HTTP status, an error while executing the request, or some other failure which occurred during the parsing of the response.

Any error returned on the `Observable` response stream will be wrapped in an [`HttpErrorResponse`](httperrorresponse) to provide additional context about the state of the HTTP layer when the error occurred. The error property will contain either a wrapped Error object or the error response returned from the server.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpErrorResponse>
