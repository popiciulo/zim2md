# ReadonlyArrayLike

ReadonlyArrayLike



# ReadonlyArrayLike

An iterable object with the same shape as a readonly array.

## API

```
type ReadonlyArrayLike<T> = Pick<
  ReadonlyArray<T>,
  number | 'length' | typeof Symbol.iterator
>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/ReadonlyArrayLike>
