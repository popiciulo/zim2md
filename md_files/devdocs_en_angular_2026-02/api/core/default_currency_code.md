# DEFAULT_CURRENCY_CODE

DEFAULT\_CURRENCY\_CODE



# DEFAULT\_CURRENCY\_CODE

Provide this token to set the default currency code your application uses for CurrencyPipe when there is no currency code passed into it. This is only used by CurrencyPipe and has no relation to locale currency. Defaults to USD if not configured.

## API

```
const DEFAULT_CURRENCY_CODE: InjectionToken<string>;
```

## Description

Provide this token to set the default currency code your application uses for CurrencyPipe when there is no currency code passed into it. This is only used by CurrencyPipe and has no relation to locale currency. Defaults to USD if not configured.

See the [i18n guide](../../guide/i18n/locale-id) for more information.

The default currency code is currently always `USD`.

If you need the previous behavior then set it by creating a [`DEFAULT_CURRENCY_CODE`](default_currency_code) provider in your application [`NgModule`](ngmodule):

```
{provide: DEFAULT_CURRENCY_CODE, useValue: 'USD'}
```

## Usage Notes

### Example

In standalone apps:

```
import { LOCALE_ID, ApplicationConfig } from '@angular/core';

const appConfig: ApplicationConfig = {
  providers: [{provide: DEFAULT_CURRENCY_CODE, useValue: 'EUR' }]
};
```

In module based apps:

```
import { platformBrowser } from '@angular/platform-browser';
import { AppModule } from './app/app.module';

platformBrowser().bootstrapModule(AppModule, {
  providers: [{provide: DEFAULT_CURRENCY_CODE, useValue: 'EUR' }]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DEFAULT_CURRENCY_CODE>
