# TitleCasePipe

TitleCasePipe



# TitleCasePipe

Transforms text to title case. Capitalizes the first letter of each word and transforms the rest of the word to lower case. Words are delimited by any whitespace character, such as a space, tab, or line-feed character.

[LowerCasePipe](lowercasepipe)[UpperCasePipe](uppercasepipe)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | titlecase }}
```

## API

```
class TitleCasePipe implements PipeTransform {
  transform(value: string): string;
  transform(value: null | undefined): null;
  transform(value: string | null | undefined): string | null;
}
```

### transform

3 overloads

@paramvalue`string`

The string to transform to title case.

@returns`string`

@paramvalue`null | undefined`

@returns`null`

@paramvalue`string | null | undefined`

@returns`string | null`

## Description

Transforms text to title case. Capitalizes the first letter of each word and transforms the rest of the word to lower case. Words are delimited by any whitespace character, such as a space, tab, or line-feed character.

---

## Exported by

- `CommonModule`

## Usage Notes

The following example shows the result of transforming various strings into title case.

```
@Component({
  selector: 'titlecase-pipe',
  imports: [TitleCasePipe],
  template: `<div>
    <p>{{ 'some string' | titlecase }}</p>
    <!-- output is expected to be "Some String" -->
    <p>{{ 'tHIs is mIXeD CaSe' | titlecase }}</p>
    <!-- output is expected to be "This Is Mixed Case" -->
    <p>{{ "it's non-trivial question" | titlecase }}</p>
    <!-- output is expected to be "It's Non-trivial Question" -->
    <p>{{ 'one,two,three' | titlecase }}</p>
    <!-- output is expected to be "One,two,three" -->
    <p>{{ 'true|false' | titlecase }}</p>
    <!-- output is expected to be "True|false" -->
    <p>{{ 'foo-vs-bar' | titlecase }}</p>
    <!-- output is expected to be "Foo-vs-bar" -->
  </div>`,
})
export class TitleCasePipeComponent {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/TitleCasePipe>
