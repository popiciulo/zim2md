# APP_BASE_HREF

APP\_BASE\_HREF



# APP\_BASE\_HREF

A predefined DI token for the base href to be used with the [`PathLocationStrategy`](pathlocationstrategy). The base href is the URL prefix that should be preserved when generating and recognizing URLs.

## API

```
const APP_BASE_HREF: InjectionToken<string>;
```

## Usage Notes

The following example shows how to use this token to configure the root app injector with a base href value, so that the DI framework can supply the dependency anywhere in the app.

```
import {NgModule} from '@angular/core';
import {APP_BASE_HREF} from '@angular/common';

@NgModule({
  providers: [{provide: APP_BASE_HREF, useValue: '/my/app'}]
})
class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/APP_BASE_HREF>
