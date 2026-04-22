# HttpClient

HttpClient



# HttpClient

Performs HTTP requests. This service is available as an injectable class, with methods to perform HTTP requests. Each request method has multiple signatures, and the return type varies based on the signature that is called (mainly the values of `observe` and `responseType`).

[HTTP Guide](../../../guide/http)[HTTP Request](httprequest)

## API

```
class HttpClient {
  constructor(handler: HttpHandler): HttpClient;
  request<R>(req: HttpRequest<any>): Observable<HttpEvent<R>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<Blob>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<string>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; observe: "events"; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "events"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<any>>;
  request<R>(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "events"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<R>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  request(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "response"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  request<R>(method: string, url: string, options: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "response"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; }): Observable<HttpResponse<R>>;
  request(method: string, url: string, options?: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; reportProgress?: boolean | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  request<R>(method: string, url: string, options?: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; reportProgress?: boolean | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<R>;
  request(method: string, url: string, options?: { body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; observe?: "body" | "events" | "response" | undefined; reportProgress?: boolean | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<any>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; body?: any; }): Observable<ArrayBuffer>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<Blob>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<string>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpEvent<ArrayBuffer>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpEvent<Blob>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpEvent<string>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpEvent<Object>>;
  delete<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpEvent<T>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpResponse<ArrayBuffer>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpResponse<Blob>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpResponse<string>>;
  delete(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpResponse<Object>>;
  delete<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }): Observable<HttpResponse<T>>;
  delete(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; } | undefined): Observable<Object>;
  delete<T>(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; } | undefined): Observable<T>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<Blob>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<string>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  get<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  get(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  get<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  get(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  get<T>(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<Blob>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<string>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  head<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  head(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  head<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  head(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  head<T>(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
  jsonp(url: string, callbackParam: string): Observable<Object>;
  jsonp<T>(url: string, callbackParam: string): Observable<T>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<Blob>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<string>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  options<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  options(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  options<T>(url: string, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  options(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  options<T>(url: string, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<Blob>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<string>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  patch<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  patch(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  patch<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  patch(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  patch<T>(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<Blob>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<string>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  post<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  post(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  post<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  post(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  post<T>(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<ArrayBuffer>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<Blob>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<string>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<ArrayBuffer>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Blob>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<string>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<Object>>;
  put<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpEvent<T>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<ArrayBuffer>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Blob>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<string>>;
  put(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<Object>>;
  put<T>(url: string, body: any, options: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }): Observable<HttpResponse<T>>;
  put(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<Object>;
  put<T>(url: string, body: any, options?: { headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined): Observable<T>;
}
```

### constructor

`HttpClient`

@paramhandler`HttpHandler`

@returns`HttpClient`

### request

17 overloads

Sends an [`HttpRequest`](httprequest) and returns a stream of [`HttpEvent`](httpevent)s.

@paramreq`HttpRequest<any>`

@returns`Observable<HttpEvent<R>>`

Constructs a request that interprets the body as an `ArrayBuffer` and returns the response in an `ArrayBuffer`.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<ArrayBuffer>`

Constructs a request that interprets the body as a blob and returns the response as a blob.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<Blob>`

Constructs a request that interprets the body as a text string and returns a string value.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<string>`

Constructs a request that interprets the body as an `ArrayBuffer` and returns the the full event stream.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; observe: "events"; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a request that interprets the body as a `Blob` and returns the full event stream.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Blob>>`

Constructs a request which interprets the body as a text string and returns the full event stream.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<string>>`

Constructs a request which interprets the body as a JavaScript object and returns the full event stream.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "events"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<any>>`

Constructs a request which interprets the body as a JavaScript object and returns the full event stream.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "events"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<R>>`

Constructs a request which interprets the body as an `ArrayBuffer` and returns the full [`HttpResponse`](httpresponse).

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a request which interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Blob>>`

Constructs a request which interprets the body as a text stream and returns the full [`HttpResponse`](httpresponse).

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<string>>`

Constructs a request which interprets the body as a JavaScript object and returns the full [`HttpResponse`](httpresponse).

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "response"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Object>>`

Constructs a request which interprets the body as a JavaScript object and returns the full [`HttpResponse`](httpresponse) with the response body in the requested type.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; reportProgress?: boolean | undefined; observe: "response"; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<R>>`

Constructs a request which interprets the body as a JavaScript object and returns the full [`HttpResponse`](httpresponse) as a JavaScript object.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; reportProgress?: boolean | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<Object>`

Constructs a request which interprets the body as a JavaScript object with the response body of the requested type.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; responseType?: "json" | undefined; reportProgress?: boolean | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<R>`

Constructs a request where response type and requested observable are not known statically.

@parammethod`string`

The HTTP method.

@paramurl`string`

The endpoint URL.

@paramoptions`{ body?: any; headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; observe?: "body" | "events" | "response" | undefined; reportProgress?: boolean | undefined; responseType?: "arraybuffer" | "blob" | "text" | "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<any>`

### delete

15 overloads

Constructs a `DELETE` request that interprets the body as an `ArrayBuffer` and returns the response as an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<ArrayBuffer>`

Constructs a `DELETE` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<Blob>`

Constructs a `DELETE` request that interprets the body as a text string and returns a string.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<string>`

Constructs a `DELETE` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `DELETE` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Blob>>`

Constructs a `DELETE` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<string>>`

Constructs a `DELETE` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Object>>`

Constructs a `DELETE`request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<T>>`

Constructs a `DELETE` request that interprets the body as an `ArrayBuffer` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `DELETE` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Blob>>`

Constructs a `DELETE` request that interprets the body as a text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<string>>`

Constructs a `DELETE` request the interprets the body as a JavaScript object and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Object>>`

Constructs a `DELETE` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<T>>`

Constructs a `DELETE` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; } | undefined`

The HTTP options to send with the request.

@returns`Observable<Object>`

Constructs a DELETE request that interprets the body as JSON and returns the response in a given type.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; body?: any; } | undefined`

The HTTP options to send with the request.

@returns`Observable<T>`

### get

15 overloads

Constructs a `GET` request that interprets the body as an `ArrayBuffer` and returns the response in an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<ArrayBuffer>`

Constructs a `GET` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<Blob>`

Constructs a `GET` request that interprets the body as a text string and returns the response as a string value.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<string>`

Constructs a `GET` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `GET` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Blob>>`

Constructs a `GET` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<string>>`

Constructs a `GET` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Object>>`

Constructs a `GET` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<T>>`

Constructs a `GET` request that interprets the body as an `ArrayBuffer` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `GET` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Blob>>`

Constructs a `GET` request that interprets the body as a text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<string>>`

Constructs a `GET` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Object>>`

Constructs a `GET` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<T>>`

Constructs a `GET` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<Object>`

Constructs a `GET` request that interprets the body as JSON and returns the response body in a given type.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<T>`

### head

15 overloads

Constructs a `HEAD` request that interprets the body as an `ArrayBuffer` and returns the response as an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<ArrayBuffer>`

Constructs a `HEAD` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<Blob>`

Constructs a `HEAD` request that interprets the body as a text string and returns the response as a string value.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<string>`

Constructs a `HEAD` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `HEAD` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Blob>>`

Constructs a `HEAD` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<string>>`

Constructs a `HEAD` request that interprets the body as JSON and returns the full HTTP event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<Object>>`

Constructs a `HEAD` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpEvent<T>>`

Constructs a `HEAD` request that interprets the body as an `ArrayBuffer` and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `HEAD` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Blob>>`

Constructs a `HEAD` request that interprets the body as text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<string>>`

Constructs a `HEAD` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<Object>>`

Constructs a `HEAD` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

The HTTP options to send with the request.

@returns`Observable<HttpResponse<T>>`

Constructs a `HEAD` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<Object>`

Constructs a `HEAD` request that interprets the body as JSON and returns the response in a given type.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

The HTTP options to send with the request.

@returns`Observable<T>`

### jsonp

2 overloads

Constructs a `JSONP` request for the given URL and name of the callback parameter.

@paramurl`string`

The resource URL.

@paramcallbackParam`string`

The callback function name.

@returns`Observable<Object>`

Constructs a `JSONP` request for the given URL and name of the callback parameter.

@paramurl`string`

The resource URL.

@paramcallbackParam`string`

The callback function name.

You must install a suitable interceptor, such as one provided by [`HttpClientJsonpModule`](httpclientjsonpmodule). If no such interceptor is reached, then the `JSONP` request can be rejected by the configured backend.

@returns`Observable<T>`

### options

15 overloads

Constructs an `OPTIONS` request that interprets the body as an `ArrayBuffer` and returns the response as an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<ArrayBuffer>`

Constructs an `OPTIONS` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<Blob>`

Constructs an `OPTIONS` request that interprets the body as a text string and returns a string value.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<string>`

Constructs an `OPTIONS` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs an `OPTIONS` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<Blob>>`

Constructs an `OPTIONS` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<string>>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<Object>>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<T>>`

Constructs an `OPTIONS` request that interprets the body as an `ArrayBuffer` and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs an `OPTIONS` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<Blob>>`

Constructs an `OPTIONS` request that interprets the body as text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<string>>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<Object>>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<T>>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options.

@returns`Observable<Object>`

Constructs an `OPTIONS` request that interprets the body as JSON and returns the response in a given type.

@paramurl`string`

The endpoint URL.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options.

@returns`Observable<T>`

### patch

15 overloads

Constructs a `PATCH` request that interprets the body as an `ArrayBuffer` and returns the response as an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<ArrayBuffer>`

Constructs a `PATCH` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<Blob>`

Constructs a `PATCH` request that interprets the body as a text string and returns the response as a string value.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<string>`

Constructs a `PATCH` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `PATCH` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<Blob>>`

Constructs a `PATCH` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<string>>`

Constructs a `PATCH` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<Object>>`

Constructs a `PATCH` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpEvent<T>>`

Constructs a `PATCH` request that interprets the body as an `ArrayBuffer` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `PATCH` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<Blob>>`

Constructs a `PATCH` request that interprets the body as a text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<string>>`

Constructs a `PATCH` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<Object>>`

Constructs a `PATCH` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<HttpResponse<T>>`

Constructs a `PATCH` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options.

@returns`Observable<Object>`

Constructs a `PATCH` request that interprets the body as JSON and returns the response in a given type.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to edit.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options.

@returns`Observable<T>`

### post

15 overloads

Constructs a `POST` request that interprets the body as an `ArrayBuffer` and returns an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options.

@returns`Observable<ArrayBuffer>`

Constructs a `POST` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<Blob>`

Constructs a `POST` request that interprets the body as a text string and returns the response as a string value.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<string>`

Constructs a `POST` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `POST` request that interprets the body as a `Blob` and returns the response in an observable of the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<Blob>>`

Constructs a `POST` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<string>>`

Constructs a POST request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<Object>>`

Constructs a POST request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<T>>`

Constructs a POST request that interprets the body as an `ArrayBuffer` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `POST` request that interprets the body as a `Blob` and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<Blob>>`

Constructs a `POST` request that interprets the body as a text stream and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<string>>`

Constructs a `POST` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<Object>>`

Constructs a `POST` request that interprets the body as JSON and returns the full [`HttpResponse`](httpresponse).

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<T>>`

Constructs a `POST` request that interprets the body as JSON and returns the response body as an object parsed from JSON.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

HTTP options

@returns`Observable<Object>`

Constructs a `POST` request that interprets the body as JSON and returns an observable of the response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The content to replace with.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; transferCache?: boolean | { includeHeaders?: string[] | undefined; } | undefined; timeout?: number | undefined; } | undefined`

HTTP options

@returns`Observable<T>`

### put

15 overloads

Constructs a `PUT` request that interprets the body as an `ArrayBuffer` and returns the response as an `ArrayBuffer`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<ArrayBuffer>`

Constructs a `PUT` request that interprets the body as a `Blob` and returns the response as a `Blob`.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<Blob>`

Constructs a `PUT` request that interprets the body as a text string and returns the response as a string value.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<string>`

Constructs a `PUT` request that interprets the body as an `ArrayBuffer` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<ArrayBuffer>>`

Constructs a `PUT` request that interprets the body as a `Blob` and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<Blob>>`

Constructs a `PUT` request that interprets the body as a text string and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<string>>`

Constructs a `PUT` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<Object>>`

Constructs a `PUT` request that interprets the body as JSON and returns the full event stream.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "events"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpEvent<T>>`

Constructs a `PUT` request that interprets the body as an `ArrayBuffer` and returns an observable of the full HTTP response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "arraybuffer"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<ArrayBuffer>>`

Constructs a `PUT` request that interprets the body as a `Blob` and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "blob"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<Blob>>`

Constructs a `PUT` request that interprets the body as a text stream and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType: "text"; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<string>>`

Constructs a `PUT` request that interprets the body as JSON and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<Object>>`

Constructs a `PUT` request that interprets the body as an instance of the requested type and returns the full HTTP response.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; observe: "response"; context?: HttpContext | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; }`

HTTP options

@returns`Observable<HttpResponse<T>>`

Constructs a `PUT` request that interprets the body as JSON and returns an observable of JavaScript object.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options

@returns`Observable<Object>`

Constructs a `PUT` request that interprets the body as an instance of the requested type and returns an observable of the requested type.

@paramurl`string`

The endpoint URL.

@parambody`any`

The resources to add/update.

@paramoptions`{ headers?: HttpHeaders | Record<string, string | string[]> | undefined; context?: HttpContext | undefined; observe?: "body" | undefined; params?: HttpParams | Record<string, string | number | boolean | readonly (string | number | boolean)[]> | undefined; reportProgress?: boolean | undefined; responseType?: "json" | undefined; withCredentials?: boolean | undefined; credentials?: RequestCredentials | undefined; keepalive?: boolean | undefined; priority?: RequestPriority | undefined; cache?: RequestCache | undefined; mode?: RequestMode | undefined; redirect?: RequestRedirect | undefined; referrer?: string | undefined; integrity?: string | undefined; referrerPolicy?: ReferrerPolicy | undefined; timeout?: number | undefined; } | undefined`

HTTP options

@returns`Observable<T>`

## Description

Performs HTTP requests. This service is available as an injectable class, with methods to perform HTTP requests. Each request method has multiple signatures, and the return type varies based on the signature that is called (mainly the values of `observe` and `responseType`).

Note that the `responseType` *options* value is a String that identifies the single data type of the response. A single overload version of the method handles each response type. The value of `responseType` cannot be a union, as the combined signature could imply.

## Usage Notes

### HTTP Request Example

```
 // GET heroes whose name contains search term
searchHeroes(term: string): observable<Hero[]>{

 const params = new HttpParams({fromString: 'name=term'});
   return this.httpClient.request('GET', this.heroesUrl, {responseType:'json', params});
}
```

Alternatively, the parameter string can be used without invoking HttpParams by directly joining to the URL.

```
this.httpClient.request('GET', this.heroesUrl + '?' + 'name=term', {responseType:'json'});
```

### JSONP Example

```
requestJsonp(url, callback = 'callback') {
 return this.httpClient.jsonp(this.heroesURL, callback);
}
```

### PATCH Example

```
// PATCH one of the heroes' name
patchHero (id: number, heroName: string): Observable<{}> {
const url = `${this.heroesUrl}/${id}`;   // PATCH api/heroes/42
 return this.httpClient.patch(url, {name: heroName}, httpOptions)
   .pipe(catchError(this.handleError('patchHero')));
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpClient>
