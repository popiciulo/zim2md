# TRANSLATIONS_FORMAT

TRANSLATIONS\_FORMAT



# TRANSLATIONS\_FORMAT

Provide this token at bootstrap to set the format of your [`TRANSLATIONS`](translations): `xtb`, `xlf` or `xlf2`.

## API

```
const TRANSLATIONS_FORMAT: InjectionToken<string>;
```

## Description

Provide this token at bootstrap to set the format of your [`TRANSLATIONS`](translations): `xtb`, `xlf` or `xlf2`.

See the [i18n guide](../../guide/i18n/merge) for more information.

## Usage Notes

### Example

In standalone apps:

```
import { LOCALE_ID, ApplicationConfig } from '@angular/core';

const appConfig: ApplicationConfig = {
  providers: [{provide: TRANSLATIONS_FORMAT, useValue: 'xlf' }]
};
```

In module based apps: \*

```
import { TRANSLATIONS_FORMAT } from '@angular/core';
import { platformBrowser } from '@angular/platform-browser';
import { AppModule } from './app/app.module';

platformBrowser().bootstrapModule(AppModule, {
  providers: [{provide: TRANSLATIONS_FORMAT, useValue: 'xlf' }]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TRANSLATIONS_FORMAT>
