# getCurrencySymbol

getCurrencySymbol



# getCurrencySymbol

Retrieves the currency symbol for a given currency code.

[Internationalization (i18n) Guide](../../guide/i18n)

Deprecation warning

Angular recommends relying on the `Intl` API for i18n. You can use `Intl.NumberFormat().formatToParts()` to extract the currency symbol. For example: `Intl.NumberFormat('en', {style:'currency', currency: 'USD'}).formatToParts().find(part => part.type === 'currency').value` returns `$` for USD currency code in the `en` locale. Note: `US$` is a currency symbol for the `en-ca` locale but not the `en-us` locale.

## API

```
function getCurrencySymbol(
  code: string,
  format: 'wide' | 'narrow',
  locale?: string,
): string;
```

### getCurrencySymbol

`string`

Retrieves the currency symbol for a given currency code.

For example, for the default `en-US` locale, the code `USD` can be represented by the narrow symbol `$` or the wide symbol `US$`.

@deprecated

Angular recommends relying on the `Intl` API for i18n. You can use `Intl.NumberFormat().formatToParts()` to extract the currency symbol. For example: `Intl.NumberFormat('en', {style:'currency', currency: 'USD'}).formatToParts().find(part => part.type === 'currency').value` returns `$` for USD currency code in the `en` locale. Note: `US$` is a currency symbol for the `en-ca` locale but not the `en-us` locale.

@paramcode`string`

The currency code.

@paramformat`"wide" | "narrow"`

The format, `wide` or `narrow`.

@paramlocale`string`

A locale code for the locale format rules to use.

@returns`string`

## Description

Retrieves the currency symbol for a given currency code.

For example, for the default `en-US` locale, the code `USD` can be represented by the narrow symbol `$` or the wide symbol `US$`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/getCurrencySymbol>
