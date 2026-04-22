# waitForAsync

waitForAsync



# waitForAsync

Wraps a test function in an asynchronous test zone. The test will automatically complete when all asynchronous calls within this zone are done. Can be used to wrap an [`inject`](inject) call.

## API

```
function waitForAsync(fn: Function): (done: any) => any;
```

### waitForAsync

`(done: any) => any`

Wraps a test function in an asynchronous test zone. The test will automatically complete when all asynchronous calls within this zone are done. Can be used to wrap an [`inject`](inject) call.

Example:

```
it('...', waitForAsync(inject([AClass], (object) => {
  object.doSomething.then(() => {
    expect(...);
  })
})));
```

@paramfn`Function`

@returns`(done: any) => any`

## Description

Wraps a test function in an asynchronous test zone. The test will automatically complete when all asynchronous calls within this zone are done. Can be used to wrap an [`inject`](inject) call.

Example:

```
it('...', waitForAsync(inject([AClass], (object) => {
  object.doSomething.then(() => {
    expect(...);
  })
})));
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/waitForAsync>
