# AngularJSUrlCodec

AngularJSUrlCodec



# AngularJSUrlCodec

A [`UrlCodec`](urlcodec) that uses logic from AngularJS to serialize and parse URLs and URL parameters.

## API

```
class AngularJSUrlCodec implements UrlCodec {
  encodePath(path: string): string;
  encodeSearch(search: string | { [k: string]: unknown; }): string;
  encodeHash(hash: string): string;
  decodePath(path: string, html5Mode?: boolean): string;
  decodeSearch(search: string): { [k: string]: unknown; };
  decodeHash(hash: string): string;
  normalize(href: string): string;
  normalize(path: string, search: { [k: string]: unknown; }, hash: string, baseUrl?: string | undefined): string;
  areEqual(valA: string, valB: string): boolean;
  parse(url: string, base?: string | undefined): { href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; };
}
```

### encodePath

`string`

@parampath`string`

@returns`string`

### encodeSearch

`string`

@paramsearch`string | { [k: string]: unknown; }`

@returns`string`

### encodeHash

`string`

@paramhash`string`

@returns`string`

### decodePath

`string`

@parampath`string`

@paramhtml5Mode`boolean`

@returns`string`

### decodeSearch

`{ [k: string]: unknown; }`

@paramsearch`string`

@returns`{ [k: string]: unknown; }`

### decodeHash

`string`

@paramhash`string`

@returns`string`

### normalize

2 overloads

@paramhref`string`

@returns`string`

@parampath`string`

@paramsearch`{ [k: string]: unknown; }`

@paramhash`string`

@parambaseUrl`string | undefined`

@returns`string`

### areEqual

`boolean`

@paramvalA`string`

@paramvalB`string`

@returns`boolean`

### parse

`{ href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; }`

@paramurl`string`

@parambase`string | undefined`

@returns`{ href: string; protocol: string; host: string; search: string; hash: string; hostname: string; port: string; pathname: string; }`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/upgrade/AngularJSUrlCodec>
