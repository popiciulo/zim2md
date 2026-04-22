# inject

inject



# inject

Allows injecting dependencies in `beforeEach()` and `it()`. Note: this function (imported from the `@angular/core/testing` package) can **only** be used to inject dependencies in tests. To inject dependencies in your application code, use the [`inject`](inject) function from the `@angular/core` package instead.

## API

```
function inject(tokens: any[], fn: Function): () => any;
```

### inject

`() => any`

Allows injecting dependencies in `beforeEach()` and `it()`. Note: this function (imported from the `@angular/core/testing` package) can **only** be used to inject dependencies in tests. To inject dependencies in your application code, use the [`inject`](inject) function from the `@angular/core` package instead.

Example:

```
beforeEach(inject([Dependency, AClass], (dep, object) => {
  // some code that uses `dep` and `object`
  // ...
}));

it('...', inject([AClass], (object) => {
  object.doSomething();
  expect(...);
})
```

@paramtokens`any[]`

@paramfn`Function`

@returns`() => any`

## Description

Allows injecting dependencies in `beforeEach()` and `it()`. Note: this function (imported from the `@angular/core/testing` package) can **only** be used to inject dependencies in tests. To inject dependencies in your application code, use the [`inject`](inject) function from the `@angular/core` package instead.

Example:

```
beforeEach(inject([Dependency, AClass], (dep, object) => {
  // some code that uses `dep` and `object`
  // ...
}));

it('...', inject([AClass], (object) => {
  object.doSomething();
  expect(...);
})
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/inject>
