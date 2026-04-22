# flush

flush



# flush

**IMPORTANT:** This API requires Zone.j

## API

```
function flush(maxTurns?: number | undefined): number;
```

### flush

`number`

**IMPORTANT:** This API requires Zone.j

Flushes any pending microtasks and simulates the asynchronous passage of time for the timers in the [`fakeAsync`](fakeasync) zone by draining the macrotask queue until it is empty.

@parammaxTurns`number | undefined`

The maximum number of times the scheduler attempts to clear its queue before throwing an error.

@returns`number`

## Description

**IMPORTANT:** This API requires Zone.j

Flushes any pending microtasks and simulates the asynchronous passage of time for the timers in the [`fakeAsync`](fakeasync) zone by draining the macrotask queue until it is empty.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/flush>
