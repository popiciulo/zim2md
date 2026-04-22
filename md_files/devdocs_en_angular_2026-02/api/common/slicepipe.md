# SlicePipe

SlicePipe



# SlicePipe

Creates a new `Array` or `String` containing a subset (slice) of the elements.

[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | slice:start:end }}
```

## API

```
class SlicePipe implements PipeTransform {
  transform<T>(value: readonly T[], start: number, end?: number | undefined): T[];
  transform(value: null | undefined, start: number, end?: number | undefined): null;
  transform<T>(value: readonly T[] | null | undefined, start: number, end?: number | undefined): T[] | null;
  transform(value: string, start: number, end?: number | undefined): string;
  transform(value: string | null | undefined, start: number, end?: number | undefined): string | null;
}
```

### transform

5 overloads

@paramvalue`readonly T[]`

a list or a string to be sliced.

@paramstart`number`

the starting index of the subset to return:

- **a positive integer**: return the item at `start` index and all items after in the list or string expression.
- **a negative integer**: return the item at `start` index from the end and all items after in the list or string expression.
- **if positive and greater than the size of the expression**: return an empty list or string.
- **if negative and greater than the size of the expression**: return entire list or string.

@paramend`number | undefined`

the ending index of the subset to return:

- **omitted**: return all items until the end.
- **if positive**: return all items before `end` index of the list or string.
- **if negative**: return all items before `end` index from the end of the list or string.

@returns`T[]`

@paramvalue`null | undefined`

@paramstart`number`

@paramend`number | undefined`

@returns`null`

@paramvalue`readonly T[] | null | undefined`

@paramstart`number`

@paramend`number | undefined`

@returns`T[] | null`

@paramvalue`string`

@paramstart`number`

@paramend`number | undefined`

@returns`string`

@paramvalue`string | null | undefined`

@paramstart`number`

@paramend`number | undefined`

@returns`string | null`

## Description

Creates a new `Array` or `String` containing a subset (slice) of the elements.

---

## Exported by

- `CommonModule`

## Usage Notes

All behavior is based on the expected behavior of the JavaScript API `Array.prototype.slice()` and `String.prototype.slice()`.

When operating on an `Array`, the returned `Array` is always a copy even when all the elements are being returned.

When operating on a blank value, the pipe returns the blank value.

### List Example

This `ngFor` example:

```
@Component({
  selector: 'slice-list-pipe',
  imports: [SlicePipe],
  template: `<ul>
    @for(i of collection | slice: 1 : 3; track $index) {
      <li>{{ i }}</li>
    }
  </ul>`,
})
export class SlicePipeListComponent {
  collection: string[] = ['a', 'b', 'c', 'd'];
}
```

produces the following:

```
<li>b</li>
<li>c</li>
```

### String Examples

```
@Component({
  selector: 'slice-string-pipe',
  imports: [SlicePipe],
  template: `<div>
    <p>{{ str }}[0:4]: '{{ str | slice: 0 : 4 }}' - output is expected to be 'abcd'</p>
    <p>{{ str }}[4:0]: '{{ str | slice: 4 : 0 }}' - output is expected to be ''</p>
    <p>{{ str }}[-4]: '{{ str | slice: -4 }}' - output is expected to be 'ghij'</p>
    <p>{{ str }}[-4:-2]: '{{ str | slice: -4 : -2 }}' - output is expected to be 'gh'</p>
    <p>{{ str }}[-100]: '{{ str | slice: -100 }}' - output is expected to be 'abcdefghij'</p>
    <p>{{ str }}[100]: '{{ str | slice: 100 }}' - output is expected to be ''</p>
  </div>`,
})
export class SlicePipeStringComponent {
  str: string = 'abcdefghij';
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/SlicePipe>
