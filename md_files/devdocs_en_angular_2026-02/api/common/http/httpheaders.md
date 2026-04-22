# HttpHeaders

HttpHeaders



# HttpHeaders

Represents the header configuration options for an HTTP request. Instances are immutable. Modifying methods return a cloned instance with the change. The original object is never changed.

[Setting request headers](../../../guide/http/making-requests#setting-request-headers)

## API

```
class HttpHeaders {
  constructor(headers?: string | { [name: string]: string | number | (string | number)[]; } | Headers | undefined): HttpHeaders;
  has(name: string): boolean;
  get(name: string): string | null;
  keys(): string[];
  getAll(name: string): string[] | null;
  append(name: string, value: string | string[]): HttpHeaders;
  set(name: string, value: string | string[]): HttpHeaders;
  delete(name: string, value?: string | string[] | undefined): HttpHeaders;
}
```

### constructor

`HttpHeaders`

Constructs a new HTTP header object with the given values.

@paramheaders`string | { [name: string]: string | number | (string | number)[]; } | Headers | undefined`

@returns`HttpHeaders`

### has

`boolean`

Checks for existence of a given header.

@paramname`string`

The header name to check for existence.

@returns`boolean`

### get

`string | null`

Retrieves the first value of a given header.

@paramname`string`

The header name.

@returns`string | null`

### keys

`string[]`

Retrieves the names of the headers.

@returns`string[]`

### getAll

`string[] | null`

Retrieves a list of values for a given header.

@paramname`string`

The header name from which to retrieve values.

@returns`string[] | null`

### append

`HttpHeaders`

Appends a new value to the existing set of values for a header and returns them in a clone of the original instance.

@paramname`string`

The header name for which to append the values.

@paramvalue`string | string[]`

The value to append.

@returns`HttpHeaders`

### set

`HttpHeaders`

Sets or modifies a value for a given header in a clone of the original instance. If the header already exists, its value is replaced with the given value in the returned object.

@paramname`string`

The header name.

@paramvalue`string | string[]`

The value or values to set or override for the given header.

@returns`HttpHeaders`

### delete

`HttpHeaders`

Deletes values for a given header in a clone of the original instance.

@paramname`string`

The header name.

@paramvalue`string | string[] | undefined`

The value or values to delete for the given header.

@returns`HttpHeaders`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpHeaders>
