# FetchBackend

FetchBackend



# FetchBackend

Uses `fetch` to send requests to a backend server.

[HttpHandler](httphandler)

## API

```
class FetchBackend implements HttpBackend {
  handle(request: HttpRequest<any>): Observable<HttpEvent<any>>;
}
```

### handle

`Observable<HttpEvent<any>>`

@paramrequest`HttpRequest<any>`

@returns`Observable<HttpEvent<any>>`

## Description

Uses `fetch` to send requests to a backend server.

This [`FetchBackend`](fetchbackend) requires the support of the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) which is available on all supported browsers and on Node.js v18 or later.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/FetchBackend>
