# PercentPipe

PercentPipe



# PercentPipe

Transforms a number to a percentage string, formatted according to locale rules that determine group sizing and separator, decimal-point character, and other locale-specific configurations.

[formatPercent](formatpercent)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | percent:digitsInfo:locale }}
```

## API

```
class PercentPipe implements PipeTransform {
  constructor(_locale: string): PercentPipe;
  transform(value: string | number, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
  transform(value: null | undefined, digitsInfo?: string | undefined, locale?: string | undefined): null;
  transform(value: string | number | null | undefined, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
}
```

### constructor

`PercentPipe`

@param\_locale`string`

@returns`PercentPipe`

### transform

3 overloads

@paramvalue`string | number`

@paramdigitsInfo`string | undefined`

@paramlocale`string | undefined`

@returns`string | null`

@paramvalue`null | undefined`

@paramdigitsInfo`string | undefined`

@paramlocale`string | undefined`

@returns`null`

@paramvalue`string | number | null | undefined`

@paramdigitsInfo`string | undefined`

@paramlocale`string | undefined`

@returns`string | null`

## Description

Transforms a number to a percentage string, formatted according to locale rules that determine group sizing and separator, decimal-point character, and other locale-specific configurations.

---

## Exported by

- `CommonModule`

## Usage Notes

The following code shows how the pipe transforms numbers into text strings, according to various format specifications, where the caller's default locale is `en-US`.

```
@Component({
  selector: 'percent-pipe',
  imports: [PercentPipe],
  template: `<div>
    <!--output '26%'-->
    <p>A: {{ a | percent }}</p>

    <!--output '0,134.950%'-->
    <p>B: {{ b | percent: '4.3-5' }}</p>

    <!--output '0 134,950 %'-->
    <p>B: {{ b | percent: '4.3-5' : 'fr' }}</p>
  </div>`,
})
export class PercentPipeComponent {
  a: number = 0.259;
  b: number = 1.3495;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/PercentPipe>
