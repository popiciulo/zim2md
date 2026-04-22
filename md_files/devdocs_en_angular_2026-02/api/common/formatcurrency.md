# formatCurrency

formatCurrency



# formatCurrency

Formats a number as currency using locale rules.

[formatNumber](formatnumber)[DecimalPipe](decimalpipe)[Internationalization (i18n) Guide](../../guide/i18n)

## API

```
function formatCurrency(
  value: number,
  locale: string,
  currency: string,
  currencyCode?: string | undefined,
  digitsInfo?: string | undefined,
): string;
```

### formatCurrency

`string`

Formats a number as currency using locale rules.

@paramvalue`number`

The number to format.

@paramlocale`string`

A locale code for the locale format rules to use.

@paramcurrency`string`

A string containing the currency symbol or its name, such as "$" or "Canadian Dollar". Used in output string, but does not affect the operation of the function.

@paramcurrencyCode`string | undefined`

The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, such as `USD` for the US dollar and `EUR` for the euro. Used to determine the number of digits in the decimal part.

@paramdigitsInfo`string | undefined`

Decimal representation options, specified by a string in the following format: `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`. See [`DecimalPipe`](decimalpipe) for more details.

@returns`string`

## Description

Formats a number as currency using locale rules.

---

## Exported by

- `CommonModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/formatCurrency>
