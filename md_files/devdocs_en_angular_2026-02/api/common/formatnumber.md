# formatNumber

formatNumber



# formatNumber

Formats a number as text, with group sizing, separator, and other parameters based on the locale.

[Internationalization (i18n) Guide](../../guide/i18n)

## API

```
function formatNumber(
  value: number,
  locale: string,
  digitsInfo?: string | undefined,
): string;
```

### formatNumber

`string`

Formats a number as text, with group sizing, separator, and other parameters based on the locale.

@paramvalue`number`

The number to format.

@paramlocale`string`

A locale code for the locale format rules to use.

@paramdigitsInfo`string | undefined`

Decimal representation options, specified by a string in the following format: `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`. See [`DecimalPipe`](decimalpipe) for more details.

@returns`string`

## Description

Formats a number as text, with group sizing, separator, and other parameters based on the locale.

---

## Exported by

- `CommonModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/formatNumber>
