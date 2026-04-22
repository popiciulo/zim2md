# StateKey

StateKey



# StateKey

A type-safe key to use with [`TransferState`](transferstate).

## API

```
type StateKey<T> = string & {
  __not_a_string: never;
  __value_type?: T;
}
```

## Description

A type-safe key to use with [`TransferState`](transferstate).

Example:

```
const COUNTER_KEY = makeStateKey<number>('counter');
let value = 10;

transferState.set(COUNTER_KEY, value);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/StateKey>
