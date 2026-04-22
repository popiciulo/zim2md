# HttpParameterCodec

HttpParameterCodec



# HttpParameterCodec

A codec for encoding and decoding parameters in URLs.

[Custom parameter encoding](../../../guide/http/making-requests#custom-parameter-encoding)

## API

```
interface HttpParameterCodec {
  encodeKey(key: string): string;
  encodeValue(value: string): string;
  decodeKey(key: string): string;
  decodeValue(value: string): string;
}
```

### encodeKey

`string`

@paramkey`string`

@returns`string`

### encodeValue

`string`

@paramvalue`string`

@returns`string`

### decodeKey

`string`

@paramkey`string`

@returns`string`

### decodeValue

`string`

@paramvalue`string`

@returns`string`

## Description

A codec for encoding and decoding parameters in URLs.

Used by [`HttpParams`](httpparams).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpParameterCodec>
