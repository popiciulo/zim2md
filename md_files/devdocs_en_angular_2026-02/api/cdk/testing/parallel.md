# parallel

parallel



# parallel

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

## API

```
function parallel<T1, T2, T3, T4, T5>(
  values: () => [
    T1 | PromiseLike<T1>,
    T2 | PromiseLike<T2>,
    T3 | PromiseLike<T3>,
    T4 | PromiseLike<T4>,
    T5 | PromiseLike<T5>,
  ],
): Promise<[T1, T2, T3, T4, T5]>;
function parallel<T1, T2, T3, T4>(
  values: () => [
    T1 | PromiseLike<T1>,
    T2 | PromiseLike<T2>,
    T3 | PromiseLike<T3>,
    T4 | PromiseLike<T4>,
  ],
): Promise<[T1, T2, T3, T4]>;
function parallel<T1, T2, T3>(
  values: () => [
    T1 | PromiseLike<T1>,
    T2 | PromiseLike<T2>,
    T3 | PromiseLike<T3>,
  ],
): Promise<[T1, T2, T3]>;
function parallel<T1, T2>(
  values: () => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>],
): Promise<[T1, T2]>;
function parallel<T>(values: () => (T | PromiseLike<T>)[]): Promise<T[]>;
```

```
function parallel<T1, T2, T3, T4, T5>(values: () => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>, T4 | PromiseLike<T4>, T5 | PromiseLike<T5>]): Promise<[T1, T2, T3, T4, T5]>;
```

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

@paramvalues`() => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>, T4 | PromiseLike<T4>, T5 | PromiseLike<T5>]`

A getter for the async values to resolve in parallel with batched change detection.

@returns`Promise<[T1, T2, T3, T4, T5]>`

```
function parallel<T1, T2, T3, T4>(values: () => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>, T4 | PromiseLike<T4>]): Promise<[T1, T2, T3, T4]>;
```

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

@paramvalues`() => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>, T4 | PromiseLike<T4>]`

A getter for the async values to resolve in parallel with batched change detection.

@returns`Promise<[T1, T2, T3, T4]>`

```
function parallel<T1, T2, T3>(values: () => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>]): Promise<[T1, T2, T3]>;
```

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

@paramvalues`() => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>, T3 | PromiseLike<T3>]`

A getter for the async values to resolve in parallel with batched change detection.

@returns`Promise<[T1, T2, T3]>`

```
function parallel<T1, T2>(values: () => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>]): Promise<[T1, T2]>;
```

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

@paramvalues`() => [T1 | PromiseLike<T1>, T2 | PromiseLike<T2>]`

A getter for the async values to resolve in parallel with batched change detection.

@returns`Promise<[T1, T2]>`

```
function parallel<T>(values: () => (T | PromiseLike<T>)[]): Promise<T[]>;
```

Resolves the given list of async values in parallel (i.e. via Promise.all) while batching change detection over the entire operation such that change detection occurs exactly once before resolving the values and once after.

@paramvalues`() => (T | PromiseLike<T>)[]`

A getter for the async values to resolve in parallel with batched change detection.

@returns`Promise<T[]>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/parallel>
