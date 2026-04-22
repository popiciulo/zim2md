# LowerCasePipe

LowerCasePipe



# LowerCasePipe

Transforms text to all lower case.

[UpperCasePipe](uppercasepipe)[TitleCasePipe](titlecasepipe)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | lowercase }}
```

## API

```
class LowerCasePipe implements PipeTransform {
  transform(value: string): string;
  transform(value: null | undefined): null;
  transform(value: string | null | undefined): string | null;
}
```

### transform

3 overloads

@paramvalue`string`

The string to transform to lower case.

@returns`string`

@paramvalue`null | undefined`

@returns`null`

@paramvalue`string | null | undefined`

@returns`string | null`

## Description

Transforms text to all lower case.

---

## Exported by

- `CommonModule`

## Usage Notes

The following example defines a view that allows the user to enter text, and then uses the pipe to convert the input text to all lower case.

```
@Component({
  selector: 'lowerupper-pipe',
  imports: [LowerCasePipe, UpperCasePipe],
  template: `<div>
    <label>Name: </label><input #name (keyup)="change(name.value)" type="text" />
    <p>In lowercase:</p>
    <pre>'{{ value | lowercase }}'</pre>
    <p>In uppercase:</p>
    <pre>'{{ value | uppercase }}'</pre>
  </div>`,
})
export class LowerUpperPipeComponent {
  value: string = '';
  change(value: string) {
    this.value = value;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/LowerCasePipe>
