# resource

resource



# resource

## API

```
function resource<T, R>(
  options: ResourceOptions<T, R> & { defaultValue: NoInfer<T> },
): ResourceRef<T>;
function resource<T, R>(
  options: ResourceOptions<T, R>,
): ResourceRef<T | undefined>;
```

```
function resource<T, R>(options: ResourceOptions<T, R> & { defaultValue: NoInfer<T>; }): ResourceRef<T>;
```

Constructs a [`Resource`](resource) that projects a reactive request to an asynchronous operation defined by a loader function, which exposes the result of the loading operation via signals.

Note that [`resource`](resource) is intended for *read* operations, not operations which perform mutations. [`resource`](resource) will cancel in-progress loads via the `AbortSignal` when destroyed or when a new request object becomes available, which could prematurely abort mutations.

@paramoptions`ResourceOptions<T, R> & { defaultValue: NoInfer<T>; }`

@returns`ResourceRef<T>`

```
function resource<T, R>(options: ResourceOptions<T, R>): ResourceRef<T | undefined>;
```

Constructs a [`Resource`](resource) that projects a reactive request to an asynchronous operation defined by a loader function, which exposes the result of the loading operation via signals.

Note that [`resource`](resource) is intended for *read* operations, not operations which perform mutations. [`resource`](resource) will cancel in-progress loads via the `AbortSignal` when destroyed or when a new request object becomes available, which could prematurely abort mutations.

@paramoptions`ResourceOptions<T, R>`

@returns`ResourceRef<T | undefined>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/resource>
