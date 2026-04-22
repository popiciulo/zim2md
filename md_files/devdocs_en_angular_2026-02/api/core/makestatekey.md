# makeStateKey

makeStateKey



# makeStateKey

Create a `StateKey<T>` that can be used to store value of type T with [`TransferState`](transferstate).

## API

```
function makeStateKey<T = void>(key: string): StateKey<T>;
```

### makeStateKey

`StateKey<T>`

Create a `StateKey<T>` that can be used to store value of type T with [`TransferState`](transferstate).

Example:

```
const COUNTER_KEY = makeStateKey<number>('counter');
let value = 10;

transferState.set(COUNTER_KEY, value);
```

@paramkey`string`

@returns`StateKey<T>`

## Description

Create a `StateKey<T>` that can be used to store value of type T with [`TransferState`](transferstate).

Example:

```
const COUNTER_KEY = makeStateKey<number>('counter');
let value = 10;

transferState.set(COUNTER_KEY, value);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/makeStateKey>
