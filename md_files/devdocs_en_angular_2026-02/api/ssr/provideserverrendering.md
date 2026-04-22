# provideServerRendering

provideServerRendering



# provideServerRendering

Configures server-side rendering for an Angular application.

[withRoutes](withroutes)[withAppShell](withappshell)

## API

```
function provideServerRendering(
  ...features: ServerRenderingFeature<ServerRenderingFeatureKind>[]
): EnvironmentProviders;
```

### provideServerRendering

`EnvironmentProviders`

Configures server-side rendering for an Angular application.

This function sets up the necessary providers for server-side rendering, including support for server routes and app shell. It combines features configured using [`withRoutes`](withroutes) and [`withAppShell`](withappshell) to provide a comprehensive server-side rendering setup.

@paramfeatures`ServerRenderingFeature<ServerRenderingFeatureKind>[]`

- Optional features to configure additional server rendering behaviors.

@returns`EnvironmentProviders`

Usage notes

Basic example of how you can enable server-side rendering in your application when using the `bootstrapApplication` function:

```
import { bootstrapApplication, BootstrapContext } from '@angular/platform-browser';
import { provideServerRendering, withRoutes, withAppShell } from '@angular/ssr';
import { AppComponent } from './app/app.component';
import { SERVER_ROUTES } from './app/app.server.routes';
import { AppShellComponent } from './app/app-shell.component';

const bootstrap = (context: BootstrapContext) =>
    bootstrapApplication(AppComponent, {
      providers: [
        provideServerRendering(
          withRoutes(SERVER_ROUTES),
          withAppShell(AppShellComponent),
        ),
      ],
    }, context);

export default bootstrap;
```

## Description

Configures server-side rendering for an Angular application.

This function sets up the necessary providers for server-side rendering, including support for server routes and app shell. It combines features configured using [`withRoutes`](withroutes) and [`withAppShell`](withappshell) to provide a comprehensive server-side rendering setup.

## Usage Notes

Basic example of how you can enable server-side rendering in your application when using the `bootstrapApplication` function:

```
import { bootstrapApplication, BootstrapContext } from '@angular/platform-browser';
import { provideServerRendering, withRoutes, withAppShell } from '@angular/ssr';
import { AppComponent } from './app/app.component';
import { SERVER_ROUTES } from './app/app.server.routes';
import { AppShellComponent } from './app/app-shell.component';

const bootstrap = (context: BootstrapContext) =>
    bootstrapApplication(AppComponent, {
      providers: [
        provideServerRendering(
          withRoutes(SERVER_ROUTES),
          withAppShell(AppShellComponent),
        ),
      ],
    }, context);

export default bootstrap;
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/provideServerRendering>
