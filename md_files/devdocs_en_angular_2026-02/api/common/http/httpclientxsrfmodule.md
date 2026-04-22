# HttpClientXsrfModule

HttpClientXsrfModule



# HttpClientXsrfModule

Configures XSRF protection support for outgoing requests.

Deprecation warning

Use withXsrfConfiguration({cookieName: 'XSRF-TOKEN', headerName: 'X-XSRF-TOKEN'}) as providers instead or [`withNoXsrfProtection`](withnoxsrfprotection) if you want to disabled XSRF protection.

## API

```
class HttpClientXsrfModule {
  static disable(): ModuleWithProviders<HttpClientXsrfModule>;
  static withOptions(options?: { cookieName?: string | undefined; headerName?: string | undefined; }): ModuleWithProviders<HttpClientXsrfModule>;
}
```

### disable

`ModuleWithProviders<HttpClientXsrfModule>`

Disable the default XSRF protection.

@returns`ModuleWithProviders<HttpClientXsrfModule>`

### withOptions

`ModuleWithProviders<HttpClientXsrfModule>`

Configure XSRF protection.

@paramoptions`{ cookieName?: string | undefined; headerName?: string | undefined; }`

An object that can specify either or both cookie name or header name.

- Cookie name default is `XSRF-TOKEN`.
- Header name default is `X-XSRF-TOKEN`.

@returns`ModuleWithProviders<HttpClientXsrfModule>`

## Description

Configures XSRF protection support for outgoing requests.

For a server that supports a cookie-based XSRF protection system, use directly to configure XSRF protection with the correct cookie and header names.

If no names are supplied, the default cookie name is `XSRF-TOKEN` and the default header name is `X-XSRF-TOKEN`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/http/HttpClientXsrfModule>
