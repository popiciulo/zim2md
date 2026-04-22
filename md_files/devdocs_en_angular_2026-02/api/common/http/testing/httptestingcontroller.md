# HttpTestingController

HttpTestingController



# HttpTestingController

Controller to be injected into tests, that allows for mocking and flushing of requests.

## API

```
abstract class HttpTestingController {
  abstract match(match: string | RequestMatch | ((req: HttpRequest<any>) => boolean)): TestRequest[];
  abstract expectOne(url: string, description?: string | undefined): TestRequest;
  abstract expectOne(params: RequestMatch, description?: string | undefined): TestRequest;
  abstract expectOne(matchFn: (req: HttpRequest<any>) => boolean, description?: string | undefined): TestRequest;
  abstract expectOne(match: string | RequestMatch | ((req: HttpRequest<any>) => boolean), description?: string | undefined): TestRequest;
  abstract expectNone(url: string, description?: string | undefined): void;
  abstract expectNone(params: RequestMatch, description?: string | undefined): void;
  abstract expectNone(matchFn: (req: HttpRequest<any>) => boolean, description?: string | undefined): void;
  abstract expectNone(match: string | RequestMatch | ((req: HttpRequest<any>) => boolean), description?: string | undefined): void;
  abstract verify(opts?: { ignoreCancelled?: boolean | undefined; } | undefined): void;
}
```

### match

`TestRequest[]`

Search for requests that match the given parameter, without any expectations.

@parammatch`string | RequestMatch | ((req: HttpRequest<any>) => boolean)`

@returns`TestRequest[]`

### expectOne

4 overloads

Expect that a single request has been made which matches the given URL, and return its mock.

If no such request has been made, or more than one such request has been made, fail with an error message including the given request description, if any.

@paramurl`string`

@paramdescription`string | undefined`

@returns`TestRequest`

Expect that a single request has been made which matches the given parameters, and return its mock.

If no such request has been made, or more than one such request has been made, fail with an error message including the given request description, if any.

@paramparams`RequestMatch`

@paramdescription`string | undefined`

@returns`TestRequest`

Expect that a single request has been made which matches the given predicate function, and return its mock.

If no such request has been made, or more than one such request has been made, fail with an error message including the given request description, if any.

@parammatchFn`(req: HttpRequest<any>) => boolean`

@paramdescription`string | undefined`

@returns`TestRequest`

Expect that a single request has been made which matches the given condition, and return its mock.

If no such request has been made, or more than one such request has been made, fail with an error message including the given request description, if any.

@parammatch`string | RequestMatch | ((req: HttpRequest<any>) => boolean)`

@paramdescription`string | undefined`

@returns`TestRequest`

### expectNone

4 overloads

Expect that no requests have been made which match the given URL.

If a matching request has been made, fail with an error message including the given request description, if any.

@paramurl`string`

@paramdescription`string | undefined`

@returns`void`

Expect that no requests have been made which match the given parameters.

If a matching request has been made, fail with an error message including the given request description, if any.

@paramparams`RequestMatch`

@paramdescription`string | undefined`

@returns`void`

Expect that no requests have been made which match the given predicate function.

If a matching request has been made, fail with an error message including the given request description, if any.

@parammatchFn`(req: HttpRequest<any>) => boolean`

@paramdescription`string | undefined`

@returns`void`

Expect that no requests have been made which match the given condition.

If a matching request has been made, fail with an error message including the given request description, if any.

@parammatch`string | RequestMatch | ((req: HttpRequest<any>) => boolean)`

@paramdescription`string | undefined`

@returns`void`

### verify

`void`

Verify that no unmatched requests are outstanding.

If any requests are outstanding, fail with an error message indicating which requests were not handled.

If `ignoreCancelled` is not set (the default), `verify()` will also fail if cancelled requests were not explicitly matched.

@paramopts`{ ignoreCancelled?: boolean | undefined; } | undefined`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/testing/HttpTestingController>
