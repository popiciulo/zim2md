# HttpUrlEncodingCodec

HttpUrlEncodingCodec



# HttpUrlEncodingCodec

Provides encoding and decoding of URL parameter and query-string values.

## API

```
class HttpUrlEncodingCodec implements HttpParameterCodec {
  encodeKey(key: string): string;
  encodeValue(value: string): string;
  decodeKey(key: string): string;
  decodeValue(value: string): string;
}
```

### encodeKey

`string`

Encodes a key name for a URL parameter or query-string.

@paramkey`string`

The key name.

@returns`string`

### encodeValue

`string`

Encodes the value of a URL parameter or query-string.

@paramvalue`string`

The value.

@returns`string`

### decodeKey

`string`

Decodes an encoded URL parameter or query-string key.

@paramkey`string`

The encoded key name.

@returns`string`

### decodeValue

`string`

Decodes an encoded URL parameter or query-string value.

@paramvalue`string`

The encoded value.

@returns`string`

## Description

Provides encoding and decoding of URL parameter and query-string values.

Serializes and parses URL parameter keys and values to encode and decode them. If you pass URL query parameters without encoding, the query parameters can be misinterpreted at the receiving end.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpUrlEncodingCodec>
