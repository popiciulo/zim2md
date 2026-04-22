# REQUEST

REQUEST



# REQUEST

Injection token representing the current HTTP request object.

[`Request` on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Request)[Accessing Request and Response via DI](../../guide/ssr#accessing-request-and-response-via-di)

## API

```
const REQUEST: InjectionToken<Request | null>;
```

## Description

Injection token representing the current HTTP request object.

Use this token to access the current request when handling server-side rendering (SSR).

## Usage Notes

This token may be `null` in the following scenarios:

- During the build processes.
- When the application is rendered in the browser (client-side rendering).
- When performing static site generation (SSG).
- During route extraction in development (at the time of the request).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/REQUEST>
