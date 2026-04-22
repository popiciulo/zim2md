# UrlCodec

UrlCodec



# UrlCodec

A codec for encoding and decoding URL parts.

## API

```
abstract class UrlCodec {
  abstract encodePath(path: string): string;
  abstract decodePath(path: string): string;
  abstract encodeSearch(search: string | { [k: string]: unknown; }): string;
  abstract decodeSearch(search: string): { [k: string]: unknown; };
  abstract encodeHash(hash: string): string;
  abstract decodeHash(hash: string): string;
  abstract normalize(href: string): string;
  abstract normalize(path: string, search: { [k: string]: unknown; }, hash: string, baseUrl?: string | undefined): string;
  abstract areEqual(valA: string, valB: string): boolean;
  abstract parse(url: string, base?: string | undefined): { href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; };
}
```

### encodePath

`string`

Encodes the path from the provided string

@parampath`string`

The path string

@returns`string`

### decodePath

`string`

Decodes the path from the provided string

@parampath`string`

The path string

@returns`string`

### encodeSearch

`string`

Encodes the search string from the provided string or object

@paramsearch`string | { [k: string]: unknown; }`

@returns`string`

### decodeSearch

`{ [k: string]: unknown; }`

Decodes the search objects from the provided string

@paramsearch`string`

@returns`{ [k: string]: unknown; }`

### encodeHash

`string`

Encodes the hash from the provided string

@paramhash`string`

@returns`string`

### decodeHash

`string`

Decodes the hash from the provided string

@paramhash`string`

@returns`string`

### normalize

2 overloads

Normalizes the URL from the provided string

@paramhref`string`

@returns`string`

Normalizes the URL from the provided string, search, hash, and base URL parameters

@parampath`string`

The URL path

@paramsearch`{ [k: string]: unknown; }`

The search object

@paramhash`string`

The has string

@parambaseUrl`string | undefined`

The base URL for the URL

@returns`string`

### areEqual

`boolean`

Checks whether the two strings are equal

@paramvalA`string`

First string for comparison

@paramvalB`string`

Second string for comparison

@returns`boolean`

### parse

`{ href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; }`

Parses the URL string based on the base URL

@paramurl`string`

The full URL string

@parambase`string | undefined`

The base for the URL

@returns`{ href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/upgrade/UrlCodec>
