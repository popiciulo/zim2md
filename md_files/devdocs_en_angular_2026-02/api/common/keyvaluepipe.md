# KeyValuePipe

KeyValuePipe



# KeyValuePipe

Transforms Object or Map into an array of key value pairs.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | keyvalue:compareFn }}
```

## API

```
class KeyValuePipe implements PipeTransform {
  constructor(differs: KeyValueDiffers): KeyValuePipe;
  transform<K, V>(input: ReadonlyMap<K, V>, compareFn?: ((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined): KeyValue<K, V>[];
  transform<K extends number, V>(input: Record<K, V>, compareFn?: ((a: KeyValue<string, V>, b: KeyValue<string, V>) => number) | null | undefined): KeyValue<string, V>[];
  transform<K extends string, V>(input: Record<K, V> | ReadonlyMap<K, V>, compareFn?: ((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined): KeyValue<K, V>[];
  transform(input: null | undefined, compareFn?: ((a: KeyValue<unknown, unknown>, b: KeyValue<unknown, unknown>) => number) | null | undefined): null;
  transform<K, V>(input: ReadonlyMap<K, V> | null | undefined, compareFn?: ((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined): KeyValue<K, V>[] | null;
  transform<K extends number, V>(input: Record<K, V> | null | undefined, compareFn?: ((a: KeyValue<string, V>, b: KeyValue<string, V>) => number) | null | undefined): KeyValue<string, V>[] | null;
  transform<K extends string, V>(input: Record<K, V> | ReadonlyMap<K, V> | null | undefined, compareFn?: ((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined): KeyValue<K, V>[] | null;
  transform<T>(input: T, compareFn?: (T extends object ? (a: T[keyof T], b: T[keyof T]) => number : never) | undefined): T extends object ? KeyValue<keyof T, T[keyof T]>[] : null;
}
```

### constructor

`KeyValuePipe`

@paramdiffers`KeyValueDiffers`

@returns`KeyValuePipe`

### transform

8 overloads

@paraminput`ReadonlyMap<K, V>`

@paramcompareFn`((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined`

@returns`KeyValue<K, V>[]`

@paraminput`Record<K, V>`

@paramcompareFn`((a: KeyValue<string, V>, b: KeyValue<string, V>) => number) | null | undefined`

@returns`KeyValue<string, V>[]`

@paraminput`Record<K, V> | ReadonlyMap<K, V>`

@paramcompareFn`((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined`

@returns`KeyValue<K, V>[]`

@paraminput`null | undefined`

@paramcompareFn`((a: KeyValue<unknown, unknown>, b: KeyValue<unknown, unknown>) => number) | null | undefined`

@returns`null`

@paraminput`ReadonlyMap<K, V> | null | undefined`

@paramcompareFn`((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined`

@returns`KeyValue<K, V>[] | null`

@paraminput`Record<K, V> | null | undefined`

@paramcompareFn`((a: KeyValue<string, V>, b: KeyValue<string, V>) => number) | null | undefined`

@returns`KeyValue<string, V>[] | null`

@paraminput`Record<K, V> | ReadonlyMap<K, V> | null | undefined`

@paramcompareFn`((a: KeyValue<K, V>, b: KeyValue<K, V>) => number) | null | undefined`

@returns`KeyValue<K, V>[] | null`

@paraminput`T`

@paramcompareFn`(T extends object ? (a: T[keyof T], b: T[keyof T]) => number : never) | undefined`

@returns`T extends object ? KeyValue<keyof T, T[keyof T]>[] : null`

## Description

Transforms Object or Map into an array of key value pairs.

The output array will be ordered by keys. By default the comparator will be by Unicode point value. You can optionally pass a compareFn if your keys are complex types. Passing `null` as the compareFn will use natural ordering of the input.

---

## Exported by

- `CommonModule`

## Usage Notes

### Examples

This examples show how an Object or a Map can be iterated by ngFor with the use of this keyvalue pipe.

```
@Component({
  selector: 'keyvalue-pipe',
  imports: [KeyValuePipe],
  template: `
  <span>
  <p>Object</p>
  @for (item of object | keyvalue; track item.key) {
    <div>{{ item.key }}:{{ item.value }}</div>
  }
  <p>Map</p>
  @for (item of map | keyvalue; track item.key) {
    <div>{{ item.key }}:{{ item.value }}</div>
  }
  <p>Natural order</p>
  @for (item of map | keyvalue : null; track item.key) {
    <div>{{ item.key }}:{{ item.value }}</div>
  }
</span>`,
})
export class KeyValuePipeComponent {
  object: {[key: number]: string} = {2: 'foo', 1: 'bar'};
  map = new Map([
    [2, 'foo'],
    [1, 'bar'],
  ]);
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/KeyValuePipe>
