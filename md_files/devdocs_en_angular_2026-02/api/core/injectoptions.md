# InjectOptions

InjectOptions



# InjectOptions

Type of the options argument to [`inject`](inject).

## API

```
interface InjectOptions {
  optional?: boolean | undefined;
  skipSelf?: boolean | undefined;
  self?: boolean | undefined;
  host?: boolean | undefined;
}
```

### optional

`boolean | undefined`

Use optional injection, and return `null` if the requested token is not found.

### skipSelf

`boolean | undefined`

Start injection at the parent of the current injector.

### self

`boolean | undefined`

Only query the current injector for the token, and don't fall back to the parent injector if it's not found.

### host

`boolean | undefined`

Stop injection at the host component's injector. Only relevant when injecting from an element injector, and a no-op for environment injectors.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/InjectOptions>
