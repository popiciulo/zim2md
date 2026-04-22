# TestRequest

TestRequest



# TestRequest

A mock requests that was received and is ready to be answered.

## API

```
class TestRequest {
  constructor(request: HttpRequest<any>, observer: Observer<HttpEvent<any>>): TestRequest;
  readonly cancelled: boolean;
  override request: HttpRequest<any>;
  flush(body: string | number | boolean | Object | ArrayBuffer | Blob | (string | number | boolean | Object | null)[] | null, opts?: { headers?: HttpHeaders | { [name: string]: string | string[]; } | undefined; status?: number | undefined; statusText?: string | undefined; }): void;
  error(error: ErrorEvent, opts?: TestRequestErrorOptions | undefined): void;
  error(error: ProgressEvent<EventTarget>, opts?: TestRequestErrorOptions | undefined): void;
  event(event: HttpEvent<any>): void;
}
```

### constructor

`TestRequest`

@paramrequest`HttpRequest<any>`

@paramobserver`Observer<HttpEvent<any>>`

@returns`TestRequest`

### cancelled

`boolean`

Whether the request was cancelled after it was sent.

### request

`HttpRequest<any>`

### flush

`void`

Resolve the request by returning a body plus additional HTTP information (such as response headers) if provided. If the request specifies an expected body type, the body is converted into the requested type. Otherwise, the body is converted to `JSON` by default.

Both successful and unsuccessful responses can be delivered via `flush()`.

@parambody`string | number | boolean | Object | ArrayBuffer | Blob | (string | number | boolean | Object | null)[] | null`

@paramopts`{ headers?: HttpHeaders | { [name: string]: string | string[]; } | undefined; status?: number | undefined; statusText?: string | undefined; }`

@returns`void`

### error

2 overloads

Resolve the request by returning an `ErrorEvent` (e.g. simulating a network failure).

@deprecated

Http requests never emit an `ErrorEvent`. Please specify a `ProgressEvent`.

@paramerror`ErrorEvent`

@paramopts`TestRequestErrorOptions | undefined`

@returns`void`

Resolve the request by returning an `ProgressEvent` (e.g. simulating a network failure).

@paramerror`ProgressEvent<EventTarget>`

@paramopts`TestRequestErrorOptions | undefined`

@returns`void`

### event

`void`

Deliver an arbitrary `HttpEvent` (such as a progress event) on the response stream for this request.

@paramevent`HttpEvent<any>`

@returns`void`

## Description

A mock requests that was received and is ready to be answered.

This interface allows access to the underlying `HttpRequest`, and allows responding with `HttpEvent`s or `HttpErrorResponse`s.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/testing/TestRequest>
