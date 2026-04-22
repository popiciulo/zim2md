# LOCALE_ID

LOCALE\_ID



# LOCALE\_ID

Provide this token to set the locale of your application. It is used for i18n extraction, by i18n pipes (DatePipe, I18nPluralPipe, CurrencyPipe, DecimalPipe and PercentPipe) and by ICU expressions.

## API

```
const LOCALE_ID: InjectionToken<string>;
```

## Description

Provide this token to set the locale of your application. It is used for i18n extraction, by i18n pipes (DatePipe, I18nPluralPipe, CurrencyPipe, DecimalPipe and PercentPipe) and by ICU expressions.

See the [i18n guide](../../guide/i18n/locale-id) for more information.

## Usage Notes

### Example

In standalone apps:

```
import { LOCALE_ID, ApplicationConfig } from '@angular/core';
import { AppModule } from './app/app.module';

const appConfig: ApplicationConfig = {
  providers: [{provide: LOCALE_ID, useValue: 'en-US' }]
};
```

In module based apps:

```
import { LOCALE_ID } from '@angular/core';
import { platformBrowser } from '@angular/platform-browser';
import { AppModule } from './app/app.module';

platformBrowser().bootstrapModule(AppModule, {
  providers: [{provide: LOCALE_ID, useValue: 'en-US' }]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/LOCALE_ID>
