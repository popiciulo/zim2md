# QueryList

QueryList



# QueryList

An unmodifiable list of items that Angular keeps up to date when the state of the application changes.

## API

```
class QueryList<T> implements Iterable<T> {
  constructor(_emitDistinctChangesOnly?: boolean): QueryList<T>;
  readonly dirty: true;
  readonly length: number;
  readonly first: T;
  readonly last: T;
  readonly changes: Observable<any>;
  get(index: number): T | undefined;
  map<U>(fn: (item: T, index: number, array: T[]) => U): U[];
  filter<S extends T>(predicate: (value: T, index: number, array: readonly T[]) => value is S): S[];
  filter(predicate: (value: T, index: number, array: readonly T[]) => unknown): T[];
  find(fn: (item: T, index: number, array: T[]) => boolean): T | undefined;
  reduce<U>(fn: (prevValue: U, curValue: T, curIndex: number, array: T[]) => U, init: U): U;
  forEach(fn: (item: T, index: number, array: T[]) => void): void;
  some(fn: (value: T, index: number, array: T[]) => boolean): boolean;
  toArray(): T[];
  toString(): string;
  reset(resultsTree: (any[] | T)[], identityAccessor?: ((value: T) => unknown) | undefined): void;
  notifyOnChanges(): void;
  setDirty(): void;
  destroy(): void;
  [Symbol.iterator]: () => Iterator<T, any, any>;
}
```

### constructor

`QueryList<T>`

@param\_emitDistinctChangesOnly`boolean`

@returns`QueryList<T>`

### dirty

`true`

### length

`number`

### first

`T`

### last

`T`

### changes

`Observable<any>`

Returns `Observable` of [`QueryList`](querylist) notifying the subscriber of changes.

### get

`T | undefined`

Returns the QueryList entry at `index`.

@paramindex`number`

@returns`T | undefined`

### map

`U[]`

See [Array.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

@paramfn`(item: T, index: number, array: T[]) => U`

@returns`U[]`

### filter

2 overloads

See [Array.filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

@parampredicate`(value: T, index: number, array: readonly T[]) => value is S`

@returns`S[]`

@parampredicate`(value: T, index: number, array: readonly T[]) => unknown`

@returns`T[]`

### find

`T | undefined`

See [Array.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)

@paramfn`(item: T, index: number, array: T[]) => boolean`

@returns`T | undefined`

### reduce

`U`

See [Array.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

@paramfn`(prevValue: U, curValue: T, curIndex: number, array: T[]) => U`

@paraminit`U`

@returns`U`

### forEach

`void`

See [Array.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

@paramfn`(item: T, index: number, array: T[]) => void`

@returns`void`

### some

`boolean`

See [Array.some](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)

@paramfn`(value: T, index: number, array: T[]) => boolean`

@returns`boolean`

### toArray

`T[]`

Returns a copy of the internal results list as an Array.

@returns`T[]`

### toString

`string`

@returns`string`

### reset

`void`

Updates the stored data of the query list, and resets the `dirty` flag to `false`, so that on change detection, it will not notify of changes to the queries, unless a new change occurs.

@paramresultsTree`(any[] | T)[]`

The query results to store

@paramidentityAccessor`((value: T) => unknown) | undefined`

Optional function for extracting stable object identity from a value in the array. This function is executed for each element of the query result list while comparing current query list with the new one (provided as a first argument of the `reset` function) to detect if the lists are different. If the function is not provided, elements are compared as is (without any pre-processing).

@returns`void`

### notifyOnChanges

`void`

Triggers a change event by emitting on the `changes` [`EventEmitter`](eventemitter).

@returns`void`

### setDirty

`void`

internal

@returns`void`

### destroy

`void`

internal

@returns`void`

### [Symbol.iterator]

`() => Iterator<T, any, any>`

## Description

An unmodifiable list of items that Angular keeps up to date when the state of the application changes.

The type of object that [`ViewChildren`](viewchildren), [`ContentChildren`](contentchildren), and [`QueryList`](querylist) provide.

Implements an iterable interface, therefore it can be used in both ES6 javascript `for (var i of items)` loops as well as in Angular templates with `@for(i of myList; track $index)`.

Changes can be observed by subscribing to the `changes` `Observable`. \*

## Usage Notes

### Example

```
@Component({...})
class Container {
  @ViewChildren(Item) items:QueryList<Item>;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/QueryList>
