# HttpParams

HttpParams



# HttpParams

An HTTP request/response body that represents serialized parameters, per the MIME type `application/x-www-form-urlencoded`.

[Setting URL parameters](../../../guide/http/making-requests#setting-url-parameters)

## API

```
class HttpParams {
  constructor(options?: HttpParamsOptions): HttpParams;
  has(param: string): boolean;
  get(param: string): string | null;
  getAll(param: string): string[] | null;
  keys(): string[];
  append(param: string, value: string | number | boolean): HttpParams;
  appendAll(params: { [param: string]: string | number | boolean | readonly (string | number | boolean)[]; }): HttpParams;
  set(param: string, value: string | number | boolean): HttpParams;
  delete(param: string, value?: string | number | boolean | undefined): HttpParams;
  toString(): string;
}
```

### constructor

`HttpParams`

@paramoptions`HttpParamsOptions`

@returns`HttpParams`

### has

`boolean`

Reports whether the body includes one or more values for a given parameter.

@paramparam`string`

The parameter name.

@returns`boolean`

### get

`string | null`

Retrieves the first value for a parameter.

@paramparam`string`

The parameter name.

@returns`string | null`

### getAll

`string[] | null`

Retrieves all values for a parameter.

@paramparam`string`

The parameter name.

@returns`string[] | null`

### keys

`string[]`

Retrieves all the parameters for this body.

@returns`string[]`

### append

`HttpParams`

Appends a new value to existing values for a parameter.

@paramparam`string`

The parameter name.

@paramvalue`string | number | boolean`

The new value to add.

@returns`HttpParams`

### appendAll

`HttpParams`

Constructs a new body with appended values for the given parameter name.

@paramparams`{ [param: string]: string | number | boolean | readonly (string | number | boolean)[]; }`

parameters and values

@returns`HttpParams`

### set

`HttpParams`

Replaces the value for a parameter.

@paramparam`string`

The parameter name.

@paramvalue`string | number | boolean`

The new value.

@returns`HttpParams`

### delete

`HttpParams`

Removes a given value or all values from a parameter.

@paramparam`string`

The parameter name.

@paramvalue`string | number | boolean | undefined`

The value to remove, if provided.

@returns`HttpParams`

### toString

`string`

Serializes the body to an encoded string, where key-value pairs (separated by `=`) are separated by `&`s.

@returns`string`

## Description

An HTTP request/response body that represents serialized parameters, per the MIME type `application/x-www-form-urlencoded`.

This class is immutable; all mutation operations return a new instance.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpParams>
