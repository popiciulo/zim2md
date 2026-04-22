# rxResource

rxResource



# rxResource

## API

```
function rxResource<T, R>(
  opts: RxResourceOptions<T, R> & { defaultValue: NoInfer<T> },
): ResourceRef<T>;
function rxResource<T, R>(
  opts: RxResourceOptions<T, R>,
): ResourceRef<T | undefined>;
```

```
function rxResource<T, R>(opts: RxResourceOptions<T, R> & { defaultValue: NoInfer<T>; }): ResourceRef<T>;
```

Like `resource` but uses an RxJS based `loader` which maps the request to an `Observable` of the resource's value.

@paramopts`RxResourceOptions<T, R> & { defaultValue: NoInfer<T>; }`

@returns`ResourceRef<T>`

```
function rxResource<T, R>(opts: RxResourceOptions<T, R>): ResourceRef<T | undefined>;
```

Like `resource` but uses an RxJS based `loader` which maps the request to an `Observable` of the resource's value.

@paramopts`RxResourceOptions<T, R>`

@returns`ResourceRef<T | undefined>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/rxjs-interop/rxResource>
