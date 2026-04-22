# formatDate

formatDate



# formatDate

Formats a date according to locale rules.

[DatePipe](datepipe)[Internationalization (i18n) Guide](../../guide/i18n)

## API

```
function formatDate(
  value: string | number | Date,
  format: string,
  locale: string,
  timezone?: string | undefined,
): string;
```

### formatDate

`string`

Formats a date according to locale rules.

@paramvalue`string | number | Date`

The date to format, as a Date, or a number (milliseconds since UTC epoch) or an [ISO date-time string](https://www.w3.org/TR/NOTE-datetime).

@paramformat`string`

The date-time components to include. See [`DatePipe`](datepipe) for details.

@paramlocale`string`

A locale code for the locale format rules to use.

@paramtimezone`string | undefined`

The time zone. A time zone offset from GMT (such as `'+0430'`). If not specified, uses host system settings.

@returns`string`

## Description

Formats a date according to locale rules.

---

## Exported by

- `CommonModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/formatDate>
