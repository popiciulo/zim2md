# HttpRequest

HttpRequest



# HttpRequest

An outgoing HTTP request with an optional typed body.

## API

```
class HttpRequest<T> {
  constructor(method: "GET" | "HEAD", url: string, init?: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): HttpRequest;
  constructor(method: "DELETE" | "JSONP" | "OPTIONS", url: string, init?: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; timeout?: number | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; } | undefined): HttpRequest;
  constructor(method: "POST", url: string, body: T | null, init?: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): HttpRequest;
  constructor(method: "PUT" | "PATCH", url: string, body: T | null, init?: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; timeout?: number | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; } | undefined): HttpRequest;
  constructor(method: string, url: string, body: T | null, init?: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): HttpRequest;
  readonly body: T | null;
  readonly headers: HttpHeaders;
  readonly context: HttpContext;
  readonly reportProgress: boolean;
  readonly withCredentials: boolean;
  readonly credentials: RequestCredentials;
  readonly keepalive: boolean;
  readonly cache: RequestCache;
  readonly priority: RequestPriority;
  readonly mode: RequestMode;
  readonly redirect: RequestRedirect;
  readonly referrer: string;
  readonly integrity: string;
  readonly referrerPolicy: ReferrerPolicy;
  readonly responseType: "arraybuffer" | "blob" | "text" | "json";
  readonly method: string;
  readonly params: HttpParams;
  readonly urlWithParams: string;
  readonly transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined;
  readonly timeout?: number | undefined;
  serializeBody(): string | ArrayBuffer | Blob | FormData | URLSearchParams | null;
  detectContentTypeHeader(): string | null;
  clone(): HttpRequest<T>;
  clone(update: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; body?: T | null | undefined; method?: string | undefined; url?: string | undefined; setHeaders?: { [name: string]: string | string[]; } | undefined; setParams?: { [param: string]: string; } | undefined; }): HttpRequest<T>;
  clone<V>(update: { headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; body?: V | null | undefined; method?: string | undefined; url?: string | undefined; setHeaders?: { [name: string]: string | string[]; } | undefined; setParams?: { [param: string]: string; } | undefined; }): HttpRequest<V>;
}
```

### constructor

5 overloads

@parammethod`"GET" | "HEAD"`

@paramurl`string`

@paraminit`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

@returns`HttpRequest`

@parammethod`"DELETE" | "JSONP" | "OPTIONS"`

@paramurl`string`

@paraminit`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; timeout?: number | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; } | undefined`

@returns`HttpRequest`

@parammethod`"POST"`

@paramurl`string`

@parambody`T | null`

@paraminit`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

@returns`HttpRequest`

@parammethod`"PUT" | "PATCH"`

@paramurl`string`

@parambody`T | null`

@paraminit`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; timeout?: number | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; } | undefined`

@returns`HttpRequest`

@parammethod`string`

@paramurl`string`

@parambody`T | null`

@paraminit`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

@returns`HttpRequest`

### body

`T | null`

The request body, or `null` if one isn't set.

Bodies are not enforced to be immutable, as they can include a reference to any user-defined data type. However, interceptors should take care to preserve idempotence by treating them as such.

### headers

`HttpHeaders`

Outgoing headers for this request.

### context

`HttpContext`

Shared and mutable context that can be used by interceptors

### reportProgress

`boolean`

Whether this request should be made in a way that exposes progress events.

Progress events are expensive (change detection runs on each event) and so they should only be requested if the consumer intends to monitor them.

Note: The [`FetchBackend`](fetchbackend) doesn't support progress report on uploads.

### withCredentials

`boolean`

Whether this request should be sent with outgoing credentials (cookies).

### credentials

`RequestCredentials`

The credentials mode of the request, which determines how cookies and HTTP authentication are handled. This can affect whether cookies are sent with the request, and how authentication is handled.

### keepalive

`boolean`

When using the fetch implementation and set to `true`, the browser will not abort the associated request if the page that initiated it is unloaded before the request is complete.

### cache

`RequestCache`

Controls how the request will interact with the browser's HTTP cache. This affects whether a response is retrieved from the cache, how it is stored, or if it bypasses the cache altogether.

### priority

`RequestPriority`

Indicates the relative priority of the request. This may be used by the browser to decide the order in which requests are dispatched and resources fetched.

### mode

`RequestMode`

The mode of the request, which determines how the request will interact with the browser's security model. This can affect things like CORS (Cross-Origin Resource Sharing) and same-origin policies.

### redirect

`RequestRedirect`

The redirect mode of the request, which determines how redirects are handled. This can affect whether the request follows redirects automatically, or if it fails when a redirect occurs.

### referrer

`string`

The referrer of the request, which can be used to indicate the origin of the request. This is useful for security and analytics purposes. Value is a same-origin URL, "about:client", or the empty string, to set request's referrer.

### integrity

`string`

The integrity metadata of the request, which can be used to ensure the request is made with the expected content. A cryptographic hash of the resource to be fetched by request

### referrerPolicy

`ReferrerPolicy`

The referrer policy of the request, which can be used to specify the referrer information to be included with the request. This can affect the amount of referrer information sent with the request, and can be used to enhance privacy and security.

### responseType

`"arraybuffer" | "blob" | "text" | "json"`

The expected response type of the server.

This is used to parse the response appropriately before returning it to the requestee.

### method

`string`

The outgoing HTTP request method.

### params

`HttpParams`

Outgoing URL parameters.

To pass a string representation of HTTP parameters in the URL-query-string format, the [`HttpParamsOptions`](httpparamsoptions)' `fromString` may be used. For example:

```
new HttpParams({fromString: 'angular=awesome'})
```

### urlWithParams

`string`

The outgoing URL with all URL parameters set.

### transferCache

`boolean | { includeHeaders?: string[] | undefined; } | undefined`

The HttpTransferCache option for the request

### timeout

`number | undefined`

The timeout for the backend HTTP request in ms.

### serializeBody

`string | ArrayBuffer | Blob | FormData | URLSearchParams | null`

Transform the free-form body into a serialized format suitable for transmission to the server.

@returns`string | ArrayBuffer | Blob | FormData | URLSearchParams | null`

### detectContentTypeHeader

`string | null`

Examine the body and attempt to infer an appropriate MIME type for it.

If no such type can be inferred, this method will return `null`.

@returns`string | null`

### clone

3 overloads

@returns`HttpRequest<T>`

@paramupdate`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; body?: T | null | undefined; method?: string | undefined; url?: string | undefined; setHeaders?: { [name: string]: string | string[]; } | undefined; setParams?: { [param: string]: string; } | undefined; }`

@returns`HttpRequest<T>`

@paramupdate`{ headers?: HttpHeaders | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; params?: HttpParams | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; body?: V | null | undefined; method?: string | undefined; url?: string | undefined; setHeaders?: { [name: string]: string | string[]; } | undefined; setParams?: { [param: string]: string; } | undefined; }`

@returns`HttpRequest<V>`

## Description

An outgoing HTTP request with an optional typed body.

[`HttpRequest`](httprequest) represents an outgoing request, including URL, method, headers, body, and other request configuration options. Instances should be assumed to be immutable. To modify a [`HttpRequest`](httprequest), the `clone` method should be used.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpRequest>
