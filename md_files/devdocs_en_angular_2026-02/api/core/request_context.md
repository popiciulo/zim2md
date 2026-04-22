# REQUEST_CONTEXT

REQUEST\_CONTEXT



# REQUEST\_CONTEXT

Injection token for additional request context.

[Accessing Request and Response via DI](../../guide/ssr#accessing-request-and-response-via-di)

## API

```
const REQUEST_CONTEXT: InjectionToken<unknown>;
```

## Description

Injection token for additional request context.

Use this token to pass custom metadata or context related to the current request in server-side rendering.

## Usage Notes

This token is only available during server-side rendering and will be `null` in other contexts.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/REQUEST_CONTEXT>
