# TRANSLATIONS

TRANSLATIONS



# TRANSLATIONS

Use this token at bootstrap to provide the content of your translation file (`xtb`, `xlf` or `xlf2`) when you want to translate your application in another language.

## API

```
const TRANSLATIONS: InjectionToken<string>;
```

## Description

Use this token at bootstrap to provide the content of your translation file (`xtb`, `xlf` or `xlf2`) when you want to translate your application in another language.

See the [i18n guide](../../guide/i18n/merge) for more information.

## Usage Notes

### Example

In standalone apps:

```
import { LOCALE_ID, ApplicationConfig } from '@angular/core';

const appConfig: ApplicationConfig = {
  providers: [{provide: TRANSLATIONS, useValue: translations }]
};
```

In module based apps:

```
import { TRANSLATIONS } from '@angular/core';
import { platformBrowser } from '@angular/platform-browser';
import { AppModule } from './app/app.module';

// content of your translation file
const translations = '....';

platformBrowser().bootstrapModule(AppModule, {
  providers: [{provide: TRANSLATIONS, useValue: translations }]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TRANSLATIONS>
