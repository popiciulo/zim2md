# TestEnvironmentOptions

TestEnvironmentOptions



# TestEnvironmentOptions

## API

```
interface TestEnvironmentOptions {
  teardown?: ModuleTeardownOptions | undefined;
  errorOnUnknownElements?: boolean | undefined;
  errorOnUnknownProperties?: boolean | undefined;
}
```

### teardown

`ModuleTeardownOptions | undefined`

Configures the test module teardown behavior in [`TestBed`](testbed).

### errorOnUnknownElements

`boolean | undefined`

Whether errors should be thrown when unknown elements are present in component's template. Defaults to `false`, where the error is simply logged. If set to `true`, the error is thrown.

### errorOnUnknownProperties

`boolean | undefined`

Whether errors should be thrown when unknown properties are present in component's template. Defaults to `false`, where the error is simply logged. If set to `true`, the error is thrown.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/TestEnvironmentOptions>
