# renderModule

renderModule



# renderModule

Bootstraps an application using provided NgModule and serializes the page content to string.

## API

```
function renderModule<T>(
  moduleType: Type<T>,
  options: {
    document?: string | Document | undefined;
    url?: string | undefined;
    extraProviders?: StaticProvider[] | undefined;
  },
): Promise<string>;
```

### renderModule

`Promise<string>`

Bootstraps an application using provided NgModule and serializes the page content to string.

@parammoduleType`Type<T>`

A reference to an NgModule that should be used for bootstrap.

@paramoptions`{ document?: string | Document | undefined; url?: string | undefined; extraProviders?: StaticProvider[] | undefined; }`

Additional configuration for the render operation:

- `document` - the document of the page to render, either as an HTML string or as a reference to the `document` instance.
- `url` - the URL for the current render request.
- `extraProviders` - set of platform level providers for the current render request.

@returns`Promise<string>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-server/renderModule>
