# renderApplication

renderApplication



# renderApplication

Bootstraps an instance of an Angular application and renders it to a string.

## API

```
function renderApplication(
  bootstrap: (context: BootstrapContext) => Promise<ApplicationRef>,
  options: {
    document?: string | Document | undefined;
    url?: string | undefined;
    platformProviders?: Provider[] | undefined;
  },
): Promise<string>;
```

### renderApplication

`Promise<string>`

Bootstraps an instance of an Angular application and renders it to a string.

@parambootstrap`(context: BootstrapContext) => Promise<ApplicationRef>`

A method that when invoked returns a promise that returns an [`ApplicationRef`](../core/applicationref) instance once resolved. The method is invoked with an [`Injector`](../core/injector) instance that provides access to the platform-level dependency injection context.

@paramoptions`{ document?: string | Document | undefined; url?: string | undefined; platformProviders?: Provider[] | undefined; }`

Additional configuration for the render operation:

- `document` - the document of the page to render, either as an HTML string or as a reference to the `document` instance.
- `url` - the URL for the current render request.
- `platformProviders` - the platform level providers for the current render request.

@returns`Promise<string>`

Usage notes

```
import { BootstrapContext, bootstrapApplication } from '@angular/platform-browser';
import { renderApplication } from '@angular/platform-server';
import { ApplicationConfig } from '@angular/core';
import { AppComponent } from './app.component';

const appConfig: ApplicationConfig = { providers: [...] };
const bootstrap = (context: BootstrapContext) =>
  bootstrapApplication(AppComponent, config, context);
const output = await renderApplication(bootstrap);
```

## Usage Notes

```
import { BootstrapContext, bootstrapApplication } from '@angular/platform-browser';
import { renderApplication } from '@angular/platform-server';
import { ApplicationConfig } from '@angular/core';
import { AppComponent } from './app.component';

const appConfig: ApplicationConfig = { providers: [...] };
const bootstrap = (context: BootstrapContext) =>
  bootstrapApplication(AppComponent, config, context);
const output = await renderApplication(bootstrap);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-server/renderApplication>
