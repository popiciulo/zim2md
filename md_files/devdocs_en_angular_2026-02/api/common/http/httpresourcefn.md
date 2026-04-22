# HttpResourceFn

HttpResourceFn



# HttpResourceFn

Type for the `httpRequest` top-level function, which includes the call signatures for the JSON- based `httpRequest` as well as sub-functions for `ArrayBuffer`, `Blob`, and `string` type requests.

## API

```
interface HttpResourceFn {
  <TResult = unknown>(url: () => string | undefined, options: HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
  <TResult = unknown>(url: () => string | undefined, options?: HttpResourceOptions<TResult, unknown> | undefined): HttpResourceRef<TResult | undefined>;
  <TResult = unknown>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
  <TResult = unknown>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, unknown> | undefined): HttpResourceRef<TResult | undefined>;
  arrayBuffer: { <TResult = ArrayBuffer>(url: () => string | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = ArrayBuffer>(url: () => string | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>; <TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>; };
  blob: { <TResult = Blob>(url: () => string | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = Blob>(url: () => string | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>; <TResult = Blob>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = Blob>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>; };
  text: { <TResult = string>(url: () => string | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = string>(url: () => string | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>; <TResult = string>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = string>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>; };
}
```

`HttpResourceRef<TResult>`

Create a `Resource` that fetches data with an HTTP GET request to the given URL.

The resource will update when the URL changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

`HttpResourceRef<TResult | undefined>`

Create a `Resource` that fetches data with an HTTP GET request to the given URL.

The resource will update when the URL changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

`HttpResourceRef<TResult>`

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

`HttpResourceRef<TResult | undefined>`

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

### arrayBuffer

`{ <TResult = ArrayBuffer>(url: () => string | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = ArrayBuffer>(url: () => string | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>; <TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>; }`

@experimental

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the URL or request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed into an `ArrayBuffer`.

### blob

`{ <TResult = Blob>(url: () => string | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = Blob>(url: () => string | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>; <TResult = Blob>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = Blob>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>; }`

@experimental

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the URL or request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed into a `Blob`.

### text

`{ <TResult = string>(url: () => string | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = string>(url: () => string | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>; <TResult = string>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>; <TResult = string>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>; }`

@experimental

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the URL or request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as a `string`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpResourceFn>
