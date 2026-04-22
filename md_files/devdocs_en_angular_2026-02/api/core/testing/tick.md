# tick

tick



# tick

**IMPORTANT:** This API requires Zone.j

## API

```
function tick(
  millis?: number,
  tickOptions?: { processNewMacroTasksSynchronously: boolean },
): void;
```

### tick

`void`

**IMPORTANT:** This API requires Zone.j

Simulates the asynchronous passage of time for the timers in the [`fakeAsync`](fakeasync) zone.

The microtasks queue is drained at the very start of this function and after any timer callback has been executed.

@parammillis`number`

The number of milliseconds to advance the virtual timer.

@paramtickOptions`{ processNewMacroTasksSynchronously: boolean; }`

The options to pass to the [`tick()`](tick) function.

@returns`void`

Usage notes

The [`tick()`](tick) option is a flag called `processNewMacroTasksSynchronously`, which determines whether or not to invoke new macroTasks.

If you provide a `tickOptions` object, but do not specify a `processNewMacroTasksSynchronously` property (`tick(100, {})`), then `processNewMacroTasksSynchronously` defaults to true.

If you omit the `tickOptions` parameter (`tick(100))`), then `tickOptions` defaults to `{processNewMacroTasksSynchronously: true}`.

### Example

{@example core/testing/ts/fake\_async.ts region='basic'}

The following example includes a nested timeout (new macroTask), and the `tickOptions` parameter is allowed to default. In this case, `processNewMacroTasksSynchronously` defaults to true, and the nested function is executed on each tick.

```
it ('test with nested setTimeout', fakeAsync(() => {
  let nestedTimeoutInvoked = false;
  function funcWithNestedTimeout() {
    setTimeout(() => {
      nestedTimeoutInvoked = true;
    });
  };
  setTimeout(funcWithNestedTimeout);
  tick();
  expect(nestedTimeoutInvoked).toBe(true);
}));
```

In the following case, `processNewMacroTasksSynchronously` is explicitly set to false, so the nested timeout function is not invoked.

```
it ('test with nested setTimeout', fakeAsync(() => {
  let nestedTimeoutInvoked = false;
  function funcWithNestedTimeout() {
    setTimeout(() => {
      nestedTimeoutInvoked = true;
    });
  };
  setTimeout(funcWithNestedTimeout);
  tick(0, {processNewMacroTasksSynchronously: false});
  expect(nestedTimeoutInvoked).toBe(false);
}));
```

## Description

**IMPORTANT:** This API requires Zone.j

Simulates the asynchronous passage of time for the timers in the [`fakeAsync`](fakeasync) zone.

The microtasks queue is drained at the very start of this function and after any timer callback has been executed.

## Usage Notes

The [`tick()`](tick) option is a flag called `processNewMacroTasksSynchronously`, which determines whether or not to invoke new macroTasks.

If you provide a `tickOptions` object, but do not specify a `processNewMacroTasksSynchronously` property (`tick(100, {})`), then `processNewMacroTasksSynchronously` defaults to true.

If you omit the `tickOptions` parameter (`tick(100))`), then `tickOptions` defaults to `{processNewMacroTasksSynchronously: true}`.

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

The following example includes a nested timeout (new macroTask), and the `tickOptions` parameter is allowed to default. In this case, `processNewMacroTasksSynchronously` defaults to true, and the nested function is executed on each tick.

```
it ('test with nested setTimeout', fakeAsync(() => {
  let nestedTimeoutInvoked = false;
  function funcWithNestedTimeout() {
    setTimeout(() => {
      nestedTimeoutInvoked = true;
    });
  };
  setTimeout(funcWithNestedTimeout);
  tick();
  expect(nestedTimeoutInvoked).toBe(true);
}));
```

In the following case, `processNewMacroTasksSynchronously` is explicitly set to false, so the nested timeout function is not invoked.

```
it ('test with nested setTimeout', fakeAsync(() => {
  let nestedTimeoutInvoked = false;
  function funcWithNestedTimeout() {
    setTimeout(() => {
      nestedTimeoutInvoked = true;
    });
  };
  setTimeout(funcWithNestedTimeout);
  tick(0, {processNewMacroTasksSynchronously: false});
  expect(nestedTimeoutInvoked).toBe(false);
}));
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/tick>
