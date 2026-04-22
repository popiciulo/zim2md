# NgForOfContext

NgForOfContext



# NgForOfContext

Deprecation warning

The `ngFor` directive is deprecated. Use the `@for` block instead.

## API

```
class NgForOfContext<T, U extends NgIterable<T> = NgIterable<T>> {
  constructor($implicit: T, ngForOf: U, index: number, count: number): NgForOfContext<T, U>;
  override $implicit: T;
  override ngForOf: U;
  override index: number;
  override count: number;
  readonly first: boolean;
  readonly last: boolean;
  readonly even: boolean;
  readonly odd: boolean;
}
```

### constructor

`NgForOfContext<T, U>`

@param$implicit`T`

Reference to the current item from the collection.

@paramngForOf`U`

The value of the iterable expression. Useful when the expression is more complex then a property access, for example when using the async pipe (`userStreams | async`).

@paramindex`number`

Returns an index of the current item in the collection.

@paramcount`number`

Returns total amount of items in the collection.

@returns`NgForOfContext<T, U>`

### $implicit

`T`

Reference to the current item from the collection.

### ngForOf

`U`

The value of the iterable expression. Useful when the expression is more complex then a property access, for example when using the async pipe (`userStreams | async`).

### index

`number`

Returns an index of the current item in the collection.

### count

`number`

Returns total amount of items in the collection.

### first

`boolean`

### last

`boolean`

### even

`boolean`

### odd

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgForOfContext>
