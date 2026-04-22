# formatPercent

formatPercent



# formatPercent

Formats a number as a percentage according to locale rules.

[formatNumber](formatnumber)[DecimalPipe](decimalpipe)[Internationalization (i18n) Guide](../../guide/i18n)

## API

```
function formatPercent(
  value: number,
  locale: string,
  digitsInfo?: string | undefined,
): string;
```

### formatPercent

`string`

Formats a number as a percentage according to locale rules.

@paramvalue`number`

The number to format.

@paramlocale`string`

A locale code for the locale format rules to use.

@paramdigitsInfo`string | undefined`

Decimal representation options, specified by a string in the following format: `{minIntegerDigits}.{minFractionDigits}-{maxFractionDigits}`. See [`DecimalPipe`](decimalpipe) for more details.

@returns`string`

## Description

Formats a number as a percentage according to locale rules.

---

## Exported by

- `CommonModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/formatPercent>
