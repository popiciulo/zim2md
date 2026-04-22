# CurrencyPipe

CurrencyPipe



# CurrencyPipe

Transforms a number to a currency string, formatted according to locale rules that determine group sizing and separator, decimal-point character, and other locale-specific configurations.

[getCurrencySymbol](getcurrencysymbol)[formatCurrency](formatcurrency)[Built-in Pipes](../../guide/templates/pipes#built-in-pipes)

## Pipe usage

```
{{ value_expression | currency:currencyCode:display:digitsInfo:locale }}
```

## API

```
class CurrencyPipe implements PipeTransform {
  constructor(_locale: string, _defaultCurrencyCode?: string): CurrencyPipe;
  transform(value: string | number, currencyCode?: string | undefined, display?: string | boolean | undefined, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
  transform(value: null | undefined, currencyCode?: string | undefined, display?: string | boolean | undefined, digitsInfo?: string | undefined, locale?: string | undefined): null;
  transform(value: string | number | null | undefined, currencyCode?: string | undefined, display?: string | boolean | undefined, digitsInfo?: string | undefined, locale?: string | undefined): string | null;
}
```

### constructor

`CurrencyPipe`

@param\_locale`string`

@param\_defaultCurrencyCode`string`

@returns`CurrencyPipe`

### transform

3 overloads

@paramvalue`string | number`

The number to be formatted as currency.

@paramcurrencyCode`string | undefined`

The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, such as `USD` for the US dollar and `EUR` for the euro. The default currency code can be configured using the [`DEFAULT_CURRENCY_CODE`](../core/default_currency_code) injection token.

@paramdisplay`string | boolean | undefined`

The format for the currency indicator. One of the following:

- `code`: Show the code (such as `USD`).
- `symbol`(default): Show the symbol (such as `$`).
- `symbol-narrow`: Use the narrow symbol for locales that have two symbols for their currency. For example, the Canadian dollar CAD has the symbol `CA$` and the symbol-narrow `$`. If the locale has no narrow symbol, uses the standard symbol for the locale.
- String: Use the given string value instead of a code or a symbol. For example, an empty string will suppress the currency & symbol.
- Boolean (marked deprecated in v5): `true` for symbol and false for `code`.

@paramdigitsInfo`string | undefined`

Decimal representation options, specified by a string in the following format:  
 `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`.

- `minIntegerDigits`: The minimum number of integer digits before the decimal point. Default is `1`.
- `minFractionDigits`: The minimum number of digits after the decimal point. Default is `2`.
- `maxFractionDigits`: The maximum number of digits after the decimal point. Default is `2`. If not provided, the number will be formatted with the proper amount of digits, depending on what the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) specifies. For example, the Canadian dollar has 2 digits, whereas the Chilean peso has none.

@paramlocale`string | undefined`

A locale code for the locale format rules to use. When not supplied, uses the value of [`LOCALE_ID`](../core/locale_id), which is `en-US` by default. See [Setting your app locale](../../guide/i18n/locale-id).

@returns`string | null`

@paramvalue`null | undefined`

@paramcurrencyCode`string | undefined`

@paramdisplay`string | boolean | undefined`

@paramdigitsInfo`string | undefined`

@paramlocale`string | undefined`

@returns`null`

@paramvalue`string | number | null | undefined`

@paramcurrencyCode`string | undefined`

@paramdisplay`string | boolean | undefined`

@paramdigitsInfo`string | undefined`

@paramlocale`string | undefined`

@returns`string | null`

## Description

Transforms a number to a currency string, formatted according to locale rules that determine group sizing and separator, decimal-point character, and other locale-specific configurations.

---

## Exported by

- `CommonModule`

## Usage Notes

The following code shows how the pipe transforms numbers into text strings, according to various format specifications, where the caller's default locale is `en-US`.

```
@Component({
  selector: 'currency-pipe',
  imports: [CurrencyPipe],
  template: `<div>
    <!--output '$0.26'-->
    <p>A: {{ a | currency }}</p>

    <!--output 'CA$0.26'-->
    <p>A: {{ a | currency: 'CAD' }}</p>

    <!--output 'CAD0.26'-->
    <p>A: {{ a | currency: 'CAD' : 'code' }}</p>

    <!--output 'CA$0,001.35'-->
    <p>B: {{ b | currency: 'CAD' : 'symbol' : '4.2-2' }}</p>

    <!--output '$0,001.35'-->
    <p>B: {{ b | currency: 'CAD' : 'symbol-narrow' : '4.2-2' }}</p>

    <!--output '0 001,35 CA$'-->
    <p>B: {{ b | currency: 'CAD' : 'symbol' : '4.2-2' : 'fr' }}</p>

    <!--output 'CLP1' because CLP has no cents-->
    <p>B: {{ b | currency: 'CLP' }}</p>
  </div>`,
})
export class CurrencyPipeComponent {
  a: number = 0.259;
  b: number = 1.3495;
}
```

Super-powered by Google ©2010–2025.
