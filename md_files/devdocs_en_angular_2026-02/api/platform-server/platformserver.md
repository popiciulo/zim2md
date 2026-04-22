# platformServer

platformServer



# platformServer

Creates a server-side instance of an Angular platform.

## API

```
function platformServer(
  extraProviders?: StaticProvider[] | undefined,
): PlatformRef;
```

### platformServer

`PlatformRef`

Creates a server-side instance of an Angular platform.

This platform should be used when performing server-side rendering of an Angular application. Standalone applications can be bootstrapped on the server using the `bootstrapApplication` function from `@angular/platform-browser`. When using `bootstrapApplication`, the [`platformServer`](platformserver) should be created first and passed to the bootstrap function using the [`BootstrapContext`](../platform-browser/bootstrapcontext).

@paramextraProviders`StaticProvider[] | undefined`

@returns`PlatformRef`

## Description

Creates a server-side instance of an Angular platform.

This platform should be used when performing server-side rendering of an Angular application. Standalone applications can be bootstrapped on the server using the `bootstrapApplication` function from `@angular/platform-browser`. When using `bootstrapApplication`, the [`platformServer`](platformserver) should be created first and passed to the bootstrap function using the [`BootstrapContext`](../platform-browser/bootstrapcontext).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-server/platformServer>
