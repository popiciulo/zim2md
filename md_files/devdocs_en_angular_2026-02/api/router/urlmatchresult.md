# UrlMatchResult

UrlMatchResult



# UrlMatchResult

Represents the result of matching URLs with a custom matching function.

[UrlMatcher](urlmatcher)

## API

```
type UrlMatchResult = {
  consumed: UrlSegment[];
  posParams?: {[name: string]: UrlSegment};
}
```

## Description

Represents the result of matching URLs with a custom matching function.

- `consumed` is an array of the consumed URL segments.
- `posParams` is a map of positional parameters.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlMatchResult>
