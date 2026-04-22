# TransferState

TransferState



# TransferState

A key value store that is transferred from the application on the server side to the application on the client side.

## API

```
class TransferState {
  get<T>(key: StateKey<T>, defaultValue: T): T;
  set<T>(key: StateKey<T>, value: T): void;
  remove<T>(key: StateKey<T>): void;
  hasKey<T>(key: StateKey<T>): boolean;
  readonly isEmpty: boolean;
  onSerialize<T>(key: StateKey<T>, callback: () => T): void;
  toJson(): string;
}
```

### get

`T`

Get the value corresponding to a key. Return `defaultValue` if key is not found.

@paramkey`StateKey<T>`

@paramdefaultValue`T`

@returns`T`

### set

`void`

Set the value corresponding to a key.

@paramkey`StateKey<T>`

@paramvalue`T`

@returns`void`

### remove

`void`

Remove a key from the store.

@paramkey`StateKey<T>`

@returns`void`

### hasKey

`boolean`

Test whether a key exists in the store.

@paramkey`StateKey<T>`

@returns`boolean`

### isEmpty

`boolean`

Indicates whether the state is empty.

### onSerialize

`void`

Register a callback to provide the value for a key when `toJson` is called.

@paramkey`StateKey<T>`

@paramcallback`() => T`

@returns`void`

### toJson

`string`

Serialize the current state of the store to JSON.

@returns`string`

## Description

A key value store that is transferred from the application on the server side to the application on the client side.

The [`TransferState`](transferstate) is available as an injectable token. On the client, just inject this token using DI and use it, it will be lazily initialized. On the server it's already included if `renderApplication` function is used. Otherwise, import the `ServerTransferStateModule` module to make the [`TransferState`](transferstate) available.

The values in the store are serialized/deserialized using JSON.stringify/JSON.parse. So only boolean, number, string, null and non-class objects will be serialized and deserialized in a non-lossy manner.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TransferState>
