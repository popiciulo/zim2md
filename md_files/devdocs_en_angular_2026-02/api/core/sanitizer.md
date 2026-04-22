# Sanitizer

Sanitizer



# Sanitizer

Sanitizer is used by the views to sanitize potentially dangerous values.

[Sanitization and security contexts](https://angular.dev/best-practices/security#sanitization-and-security-contexts)

## API

```
abstract class Sanitizer {
  abstract sanitize(context: SecurityContext, value: string | {} | null): string | null;
}
```

### sanitize

`string | null`

@paramcontext`SecurityContext`

@paramvalue`string | {} | null`

@returns`string | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Sanitizer>
