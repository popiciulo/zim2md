# UpperCasePipe

UpperCasePipe



# UpperCasePipe

Transforms text to all upper case.

[LowerCasePipe](lowercasepipe)[TitleCasePipe](titlecasepipe)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | uppercase }}
```

## API

```
class UpperCasePipe implements PipeTransform {
  transform(value: string): string;
  transform(value: null | undefined): null;
  transform(value: string | null | undefined): string | null;
}
```

### transform

3 overloads

@paramvalue`string`

The string to transform to upper case.

@returns`string`

@paramvalue`null | undefined`

@returns`null`

@paramvalue`string | null | undefined`

@returns`string | null`

## Description

Transforms text to all upper case.

---

## Exported by

- `CommonModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/UpperCasePipe>
