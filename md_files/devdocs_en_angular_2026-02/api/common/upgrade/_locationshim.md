# $locationShim

$locationShim



# $locationShim

Location service that provides a drop-in replacement for the $location service provided in AngularJS.

[Using the Angular Unified Location Service](../../../guide/upgrade#using-the-unified-angular-location-service)

## API

```
class $locationShim {
  constructor($injector: any, location: Location, platformLocation: PlatformLocation, urlCodec: UrlCodec, locationStrategy: LocationStrategy): $locationShim;
  onChange(fn: (url: string, state: unknown, oldUrl: string, oldState: unknown) => void, err?: (e: Error) => void): void;
  $$parse(url: string): void;
  $$parseLinkUrl(url: string, relHref?: string | null | undefined): boolean;
  absUrl(): string;
  url(): string;
  url(url: string): this;
  protocol(): string;
  host(): string;
  port(): number | null;
  path(): string;
  path(path: string | number | null): this;
  search(): { [key: string]: unknown; };
  search(search: string | number | { [key: string]: unknown; }): this;
  search(search: string | number | { [key: string]: unknown; }, paramValue: string | number | boolean | string[] | null | undefined): this;
  hash(): string;
  hash(hash: string | number | null): this;
  replace(): this;
  state(): unknown;
  state(state: unknown): this;
}
```

### constructor

`$locationShim`

@param$injector`any`

@paramlocation`Location`

@paramplatformLocation`PlatformLocation`

@paramurlCodec`UrlCodec`

@paramlocationStrategy`LocationStrategy`

@returns`$locationShim`

### onChange

`void`

Registers listeners for URL changes. This API is used to catch updates performed by the AngularJS framework. These changes are a subset of the `$locationChangeStart` and `$locationChangeSuccess` events which fire when AngularJS updates its internally-referenced version of the browser URL.

It's possible for `$locationChange` events to happen, but for the browser URL (window.location) to remain unchanged. This `onChange` callback will fire only when AngularJS actually updates the browser URL (window.location).

@paramfn`(url: string, state: unknown, oldUrl: string, oldState: unknown) => void`

The callback function that is triggered for the listener when the URL changes.

@paramerr`(e: Error) => void`

The callback function that is triggered when an error occurs.

@returns`void`

### $$parse

`void`

Parses the provided URL, and sets the current URL to the parsed result.

@paramurl`string`

The URL string.

@returns`void`

### $$parseLinkUrl

`boolean`

Parses the provided URL and its relative URL.

@paramurl`string`

The full URL string.

@paramrelHref`string | null | undefined`

A URL string relative to the full URL string.

@returns`boolean`

### absUrl

`string`

Retrieves the full URL representation with all segments encoded according to rules specified in [RFC 3986](https://tools.ietf.org/html/rfc3986).

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let absUrl = $location.absUrl();
// => "http://example.com/#/some/path?foo=bar&baz=xoxo"
```

@returns`string`

### url

2 overloads

Retrieves the current URL, or sets a new URL. When setting a URL, changes the path, search, and hash, and returns a reference to its own instance.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let url = $location.url();
// => "/some/path?foo=bar&baz=xoxo"
```

@returns`string`

@paramurl`string`

@returns`this`

### protocol

`string`

Retrieves the protocol of the current URL.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let protocol = $location.protocol();
// => "http"
```

@returns`string`

### host

`string`

Retrieves the protocol of the current URL.

In contrast to the non-AngularJS version `location.host` which returns `hostname:port`, this returns the `hostname` portion only.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let host = $location.host();
// => "example.com"

// given URL http://user:password@example.com:8080/#/some/path?foo=bar&baz=xoxo
host = $location.host();
// => "example.com"
host = location.host;
// => "example.com:8080"
```

@returns`string`

### port

`number | null`

Retrieves the port of the current URL.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let port = $location.port();
// => 80
```

@returns`number | null`

### path

2 overloads

Retrieves the path of the current URL, or changes the path and returns a reference to its own instance.

Paths should always begin with forward slash (/). This method adds the forward slash if it is missing.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let path = $location.path();
// => "/some/path"
```

@returns`string`

@parampath`string | number | null`

@returns`this`

### search

3 overloads

Retrieves a map of the search parameters of the current URL, or changes a search part and returns a reference to its own instance.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo
let searchObject = $location.search();
// => {foo: 'bar', baz: 'xoxo'}

// set foo to 'yipee'
$location.search('foo', 'yipee');
// $location.search() => {foo: 'yipee', baz: 'xoxo'}
```

@returns`{ [key: string]: unknown; }`

@paramsearch`string | number | { [key: string]: unknown; }`

@returns`this`

@paramsearch`string | number | { [key: string]: unknown; }`

@paramparamValue`string | number | boolean | string[] | null | undefined`

@returns`this`

### hash

2 overloads

Retrieves the current hash fragment, or changes the hash fragment and returns a reference to its own instance.

```
// given URL http://example.com/#/some/path?foo=bar&baz=xoxo#hashValue
let hash = $location.hash();
// => "hashValue"
```

@returns`string`

@paramhash`string | number | null`

@returns`this`

### replace

`this`

Changes to `$location` during the current `$digest` will replace the current history record, instead of adding a new one.

@returns`this`

### state

2 overloads

Retrieves the history state object when called without any parameter.

Change the history state object when called with one parameter and return `$location`. The state object is later passed to `pushState` or `replaceState`.

This method is supported only in HTML5 mode and only in browsers supporting the HTML5 History API methods such as `pushState` and `replaceState`. If you need to support older browsers (like Android < 4.0), don't use this method.

@returns`unknown`

@paramstate`unknown`

@returns`this`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/upgrade/$locationShim>
