# HttpContext

HttpContext



# HttpContext

Http context stores arbitrary user defined values and ensures type safety without actually knowing the types. It is backed by a `Map` and guarantees that keys do not clash.

[Request and response metadata](../../../guide/http/interceptors#request-and-response-metadata)

## API

```
class HttpContext {
  set<T>(token: HttpContextToken<T>, value: T): HttpContext;
  get<T>(token: HttpContextToken<T>): T;
  delete(token: HttpContextToken<unknown>): HttpContext;
  has(token: HttpContextToken<unknown>): boolean;
  keys(): IterableIterator<HttpContextToken<unknown>>;
}
```

### set

`HttpContext`

Store a value in the context. If a value is already present it will be overwritten.

@paramtoken`HttpContextToken<T>`

The reference to an instance of [`HttpContextToken`](httpcontexttoken).

@paramvalue`T`

The value to store.

@returns`HttpContext`

### get

`T`

Retrieve the value associated with the given token.

@paramtoken`HttpContextToken<T>`

The reference to an instance of [`HttpContextToken`](httpcontexttoken).

@returns`T`

### delete

`HttpContext`

Delete the value associated with the given token.

@paramtoken`HttpContextToken<unknown>`

The reference to an instance of [`HttpContextToken`](httpcontexttoken).

@returns`HttpContext`

### has

`boolean`

Checks for existence of a given token.

@paramtoken`HttpContextToken<unknown>`

The reference to an instance of [`HttpContextToken`](httpcontexttoken).

@returns`boolean`

### keys

`IterableIterator<HttpContextToken<unknown>>`

@returns`IterableIterator<HttpContextToken<unknown>>`

## Description

Http context stores arbitrary user defined values and ensures type safety without actually knowing the types. It is backed by a `Map` and guarantees that keys do not clash.

This context is mutable and is shared between cloned requests unless explicitly specified.

## Usage Notes

### Usage Example

```
// inside cache.interceptors.ts
export const IS_CACHE_ENABLED = new HttpContextToken<boolean>(() => false);

export class CacheInterceptor implements HttpInterceptor {

  intercept(req: HttpRequest<any>, delegate: HttpHandler): Observable<HttpEvent<any>> {
    if (req.context.get(IS_CACHE_ENABLED) === true) {
      return ...;
    }
    return delegate.handle(req);
  }
}

// inside a service

this.httpClient.get('/api/weather', {
  context: new HttpContext().set(IS_CACHE_ENABLED, true)
}).subscribe(...);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpContext>
