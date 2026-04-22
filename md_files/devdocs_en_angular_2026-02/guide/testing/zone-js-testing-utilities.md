# Zone.js Testing Utilities

Zone.js Testing Utilities



# Zone.js Testing Utilities

  

This guide describes testing utilities primarily used for managing and controlling async tasks in unit tests. These utilities are essentially the Zone.js-specific mock clock utilities, particularly relevant for controlling the flow of asynchronous operations within tests.

For general Angular testing utilities, including [`TestBed`](../../api/core/testing/testbed) and [`ComponentFixture`](../../api/core/testing/componentfixture), see the [Testing Utility APIs](utility-apis) guide.

Here's a summary of Zone.js-specific functions:

| Function | Details |
| --- | --- |
| [`waitForAsync`](../../api/core/testing/waitforasync) | Tracks async tasks and completes the tests only once there are no longer any micro or macrotasks remaining in the test zone. See [waitForAsync](components-scenarios#waitForAsync). |
| [`fakeAsync`](../../api/core/testing/fakeasync) | Runs the body of a test (`it`) within a special *fakeAsync test zone*, enabling a linear control flow coding style. See [fakeAsync](components-scenarios#fake-async). |
| [`tick`](../../api/core/testing/tick) | Simulates the passage of time and the completion of pending asynchronous activities by flushing both *timer* and *micro-task* queues within the *fakeAsync test zone*. The curious, dedicated reader might enjoy this lengthy blog post, ["*Tasks, microtasks, queues and schedules*"](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules). Accepts an optional argument that moves the virtual clock forward by the specified number of milliseconds, clearing asynchronous activities scheduled within that timeframe. See [tick](components-scenarios#tick). |
| [`discardPeriodicTasks`](../../api/core/testing/discardperiodictasks) | Discards any periodic tasks (e.g. `setInterval`) that were created inside the [`fakeAsync`](../../api/core/testing/fakeasync) Zone. |
| [`flushMicrotasks`](../../api/core/testing/flushmicrotasks) | When a [`fakeAsync()`](../../api/core/testing/fakeasync) test ends with pending *micro-tasks* such as unresolved promises, the test fails with a clear error message.   In general, a test should wait for micro-tasks to finish. When pending microtasks are expected, call [`flushMicrotasks`](../../api/core/testing/flushmicrotasks) to flush the *micro-task* queue and avoid the error. |

Super-powered by Google ©2010–2025.
