# Format data based on locale

Format data based on locale



# Format data based on locale

  

Angular provides the following built-in data transformation [pipes](../templates/pipes). The data transformation pipes use the [`LOCALE_ID`](../../api/core/locale_id) token to format data based on rules of each locale.

| Data transformation pipe | Details |
| --- | --- |
| [`DatePipe`](../../api/common/datepipe) | Formats a date value. |
| [`CurrencyPipe`](../../api/common/currencypipe) | Transforms a number into a currency string. |
| [`DecimalPipe`](../../api/common/decimalpipe) | Transforms a number into a decimal number string. |
| [`PercentPipe`](../../api/common/percentpipe) | Transforms a number into a percentage string. |

## Use DatePipe to display the current date

To display the current date in the format for the current locale, use the following format for the [`DatePipe`](../../api/common/datepipe).

```
{{ today | date }}
```

## Override current locale for CurrencyPipe

Add the `locale` parameter to the pipe to override the current value of [`LOCALE_ID`](../../api/core/locale_id) token.

To force the currency to use American English (`en-US`), use the following format for the [`CurrencyPipe`](../../api/common/currencypipe)

```
{{ amount | currency : 'en-US' }}
```

**HELPFUL:** The locale specified for the [`CurrencyPipe`](../../api/common/currencypipe) overrides the global [`LOCALE_ID`](../../api/core/locale_id) token of your application.

## What's next

  [Prepare component for translation](prepare)  

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/i18n/format-data-locale>
