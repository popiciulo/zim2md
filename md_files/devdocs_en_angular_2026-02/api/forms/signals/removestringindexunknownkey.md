# RemoveStringIndexUnknownKey

RemoveStringIndexUnknownKey



# RemoveStringIndexUnknownKey

Utility type that removes a string index key when its value is `unknown`, i.e. `{[key: string]: unknown}`. It allows specific string keys to pass through, even if their value is `unknown`, e.g. `{key: unknown}`.

## API

```
type RemoveStringIndexUnknownKey<K, V> = string extends K
  ? unknown extends V
    ? never
    : K
  : K
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/RemoveStringIndexUnknownKey>
