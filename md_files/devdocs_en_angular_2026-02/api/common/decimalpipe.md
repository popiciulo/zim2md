# DecimalPipe

DecimalPipe



# DecimalPipe

Formats a value according to digit options and locale rules. Locale determines group sizing and separator, decimal point character, and other locale-specific configurations.

[formatNumber](formatnumber)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | number:digitsInfo:locale }}
```

## API

```
class DecimalPipe implements PipeTransform {
  constructor(_locale: string): DecimalPipe;
  transform(value: string | number, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
  transform(value: null | undefined, digitsInfo?: string | undefined, locale?: string | undefined): null;
  transform(value: string | number | null | undefined, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
}
```

### constructor

`DecimalPipe`

@param\_locale`string`

@returns`DecimalPipe`

### transform

3 overloads

@paramvalue`string | number`

The value to be formatted.

@paramdigitsInfo`string | undefined`

Sets digit and decimal representation. [See more](#digitsinfo).

@paramlocale`string | undefined`

Specifies what locale format rules to use. [See more](#locale).

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

Formats a value according to digit options and locale rules. Locale determines group sizing and separator, decimal point character, and other locale-specific configurations.

---

## Exported by

- `CommonModule`

## Usage Notes

### digitsInfo

The value's decimal representation is specified by the `digitsInfo` parameter, written in the following format:

```
{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}
```

- `minIntegerDigits`: The minimum number of integer digits before the decimal point. Default is 1.
- `minFractionDigits`: The minimum number of digits after the decimal point. Default is 0.
- `maxFractionDigits`: The maximum number of digits after the decimal point. Default is 3.

If the formatted value is truncated it will be rounded using the "to-nearest" method:

```
{{3.6 | number: '1.0-0'}}
<!--will output '4'-->

{{-3.6 | number:'1.0-0'}}
<!--will output '-4'-->
```

### locale

`locale` will format a value according to locale rules. Locale determines group sizing and separator, decimal point character, and other locale-specific configurations.

When not supplied, uses the value of [`LOCALE_ID`](../core/locale_id), which is `en-US` by default.

See [Setting your app locale](../../guide/i18n/locale-id).

### Example

The following code shows how the pipe transforms values according to various format specifications, where the caller's default locale is `en-US`.

```
@Component({
  selector: 'number-pipe',
  imports: [DecimalPipe],
  template: `<div>
    <p>
      No specified formatting:
      {{ pi | number }}
      <!--output: '3.142'-->
    </p>

    <p>
      With digitsInfo parameter specified:
      {{ pi | number: '4.1-5' }}
      <!--output: '0,003.14159'-->
    </p>

    <p>
      With digitsInfo and locale parameters specified:
      {{ pi | number: '4.1-5' : 'fr' }}
      <!--output: '0 003,14159'-->
    </p>
  </div>`,
})
export class NumberPipeComponent {
  pi: number = 3.14159265359;
}
```

Super-powered by Google ©2010–2025.
