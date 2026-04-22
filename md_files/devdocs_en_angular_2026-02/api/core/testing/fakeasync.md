# fakeAsync

fakeAsync



# fakeAsync

**IMPORTANT:** This API requires Zone.j

## API

```
function fakeAsync(
  fn: Function,
  options?: { flush?: boolean | undefined } | undefined,
): (...args: any[]) => any;
```

### fakeAsync

`(...args: any[]) => any`

**IMPORTANT:** This API requires Zone.j

Wraps a function to be executed in the [`fakeAsync`](fakeasync) zone:

- Microtasks are manually executed by calling [`flushMicrotasks()`](flushmicrotasks).
- Timers are synchronous; [`tick()`](tick) simulates the asynchronous passage of time.

Can be used to wrap [`inject()`](inject) calls.

@paramfn`Function`

The function that you want to wrap in the [`fakeAsync`](fakeasync) zone.

@paramoptions`{ flush?: boolean | undefined; } | undefined`

- flush: When true, will drain the macrotask queue after the test function completes. When false, will throw an exception at the end of the function if there are pending timers.

@returns`(...args: any[]) => any`

Usage notes

### Example

{@example core/testing/ts/fake\_async.ts region='basic'}

## Description

**IMPORTANT:** This API requires Zone.j

Wraps a function to be executed in the [`fakeAsync`](fakeasync) zone:

- Microtasks are manually executed by calling [`flushMicrotasks()`](flushmicrotasks).
- Timers are synchronous; [`tick()`](tick) simulates the asynchronous passage of time.

Can be used to wrap [`inject()`](inject) calls.

## Usage Notes

### Example

```
describe('this test', () => {
  it(
    'looks async but is synchronous',
    <any>fakeAsync((): void => {
      let flag = false;
      setTimeout(() => {
        flag = true;
      }, 100);
      expect(flag).toBe(false);
      tick(50);
      expect(flag).toBe(false);
      tick(50);
      expect(flag).toBe(true);
    }),
  );
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/fakeAsync>
