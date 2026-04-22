# httpResource

httpResource



# httpResource

[`httpResource`](httpresource) makes a reactive HTTP request and exposes the request status and response value as a [`WritableResource`](../../core/writableresource). By default, it assumes that the backend will return JSON data. To make a request that expects a different kind of data, you can use a sub-constructor of [`httpResource`](httpresource), such as [`httpResource.text`](httpresource#text).

## API

```
function httpResource<TResult = unknown>(url, options);function httpResource<TResult = unknown>(url, options?);function httpResource<TResult = unknown>(request, options);function httpResource<TResult = unknown>(request, options?);function httpResource.arrayBuffer<TResult = ArrayBuffer>(url, options);function httpResource.arrayBuffer<TResult = ArrayBuffer>(url, options?);function httpResource.arrayBuffer<TResult = ArrayBuffer>(request, options);function httpResource.arrayBuffer<TResult = ArrayBuffer>(request, options?);function httpResource.blob<TResult = Blob>(url, options);function httpResource.blob<TResult = Blob>(url, options?);function httpResource.blob<TResult = Blob>(request, options);function httpResource.blob<TResult = Blob>(request, options?);function httpResource.text<TResult = string>(url, options);function httpResource.text<TResult = string>(url, options?);function httpResource.text<TResult = string>(request, options);function httpResource.text<TResult = string>(request, options?);
function httpResource<TResult = unknown>(url, options?);
function httpResource<TResult = unknown>(request, options);
function httpResource<TResult = unknown>(request, options?);

function httpResource.arrayBuffer<TResult = ArrayBuffer>(url, options);
function httpResource.arrayBuffer<TResult = ArrayBuffer>(url, options?);
function httpResource.arrayBuffer<TResult = ArrayBuffer>(request, options);
function httpResource.arrayBuffer<TResult = ArrayBuffer>(request, options?);

function httpResource.blob<TResult = Blob>(url, options);
function httpResource.blob<TResult = Blob>(url, options?);
function httpResource.blob<TResult = Blob>(request, options);
function httpResource.blob<TResult = Blob>(request, options?);

function httpResource.text<TResult = string>(url, options);
function httpResource.text<TResult = string>(url, options?);
function httpResource.text<TResult = string>(request, options);
function httpResource.text<TResult = string>(request, options?);
```

```
function httpResource<TResult = unknown>(url: () => string | undefined, options: HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

Create a `Resource` that fetches data with an HTTP GET request to the given URL.

The resource will update when the URL changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource<TResult = unknown>(url: () => string | undefined, options?: HttpResourceOptions<TResult, unknown> | undefined): HttpResourceRef<TResult | undefined>;
```

Create a `Resource` that fetches data with an HTTP GET request to the given URL.

The resource will update when the URL changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource<TResult = unknown>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource<TResult = unknown>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, unknown> | undefined): HttpResourceRef<TResult | undefined>;
```

Create a `Resource` that fetches data with the configured HTTP request.

The resource will update when the request changes via signals.

Uses [`HttpClient`](httpclient) to make requests and supports interceptors, testing, and the other features of the [`HttpClient`](httpclient) API. Data is parsed as JSON by default - use a sub-function of [`httpResource`](httpresource), such as [`httpResource.text()`](httpresource#text), to parse the response differently.

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, unknown> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.arrayBuffer<TResult = ArrayBuffer>(url: () => string | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.arrayBuffer<TResult = ArrayBuffer>(url: () => string | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, ArrayBuffer> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.arrayBuffer<TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, ArrayBuffer> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.arrayBuffer<TResult = ArrayBuffer>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, ArrayBuffer> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, ArrayBuffer> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.blob<TResult = Blob>(url: () => string | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.blob<TResult = Blob>(url: () => string | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, Blob> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.blob<TResult = Blob>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, Blob> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.blob<TResult = Blob>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, Blob> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, Blob> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.text<TResult = string>(url: () => string | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.text<TResult = string>(url: () => string | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramurl`() => string | undefined`

@paramoptions`HttpResourceOptions<TResult, string> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

```
function httpResource.text<TResult = string>(request: () => HttpResourceRequest | undefined, options: HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }): HttpResourceRef<TResult>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, string> & { defaultValue: NoInfer<TResult>; }`

@returns`HttpResourceRef<TResult>`

```
function httpResource.text<TResult = string>(request: () => HttpResourceRequest | undefined, options?: HttpResourceOptions<TResult, string> | undefined): HttpResourceRef<TResult | undefined>;
```

@paramrequest`() => HttpResourceRequest | undefined`

@paramoptions`HttpResourceOptions<TResult, string> | undefined`

@returns`HttpResourceRef<TResult | undefined>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/httpResource>
