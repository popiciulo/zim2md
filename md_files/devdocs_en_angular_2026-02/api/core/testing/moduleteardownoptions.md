# ModuleTeardownOptions

ModuleTeardownOptions



# ModuleTeardownOptions

Configures the test module teardown behavior in [`TestBed`](testbed).

## API

```
interface ModuleTeardownOptions {
  destroyAfterEach: boolean;
  rethrowErrors?: boolean | undefined;
}
```

### destroyAfterEach

`boolean`

Whether the test module should be destroyed after every test. Defaults to `true`.

### rethrowErrors

`boolean | undefined`

Whether errors during test module destruction should be re-thrown. Defaults to `true`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/ModuleTeardownOptions>
