# HttpXsrfTokenExtractor

HttpXsrfTokenExtractor



# HttpXsrfTokenExtractor

Retrieves the current XSRF token to use with the next outgoing request.

## API

```
abstract class HttpXsrfTokenExtractor {
  abstract getToken(): string | null;
}
```

### getToken

`string | null`

Get the XSRF token to use with an outgoing request.

Will be called for every request, so the token may change between requests.

@returns`string | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpXsrfTokenExtractor>
