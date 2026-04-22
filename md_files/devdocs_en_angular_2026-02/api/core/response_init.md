# RESPONSE_INIT

RESPONSE\_INIT



# RESPONSE\_INIT

Injection token for response initialization options.

[`ResponseInit` on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Response/Response)[Accessing Request and Response via DI](../../guide/ssr#accessing-request-and-response-via-di)

## API

```
const RESPONSE_INIT: InjectionToken<ResponseInit | null>;
```

## Description

Injection token for response initialization options.

Use this token to provide response options for configuring or initializing HTTP responses in server-side rendering or API endpoints.

## Usage Notes

This token may be `null` in the following scenarios:

- During the build processes.
- When the application is rendered in the browser (client-side rendering).
- When performing static site generation (SSG).
- During route extraction in development (at the time of the request).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/RESPONSE_INIT>
