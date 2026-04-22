# withAppShell

withAppShell



# withAppShell

Configures the shell of the application.

[provideServerRendering](provideserverrendering)[App shell pattern on Angular.dev](https://angular.dev/ecosystem/service-workers/app-shell)

## API

```
function withAppShell(
  component:
    | Type<unknown>
    | (() => Promise<Type<unknown> | DefaultExport<Type<unknown>>>),
): ServerRenderingFeature<ServerRenderingFeatureKind.AppShell>;
```

### withAppShell

`ServerRenderingFeature<ServerRenderingFeatureKind.AppShell>`

Configures the shell of the application.

The app shell is a minimal, static HTML page that is served immediately, while the full Angular application loads in the background. This improves perceived performance by providing instant feedback to the user.

This function configures the app shell route, which serves the provided component for requests that do not match any defined server routes.

@paramcomponent`Type<unknown> | (() => Promise<Type<unknown> | DefaultExport<Type<unknown>>>)`

- The Angular component to render for the app shell. Can be a direct component type or a dynamic import function.

@returns`ServerRenderingFeature<ServerRenderingFeatureKind.AppShell>`

Usage notes

```
import { provideServerRendering, withAppShell, withRoutes } from '@angular/ssr';
import { AppShellComponent } from './app-shell.component';

provideServerRendering(
  withRoutes(serverRoutes),
  withAppShell(AppShellComponent)
);
```

```
import { provideServerRendering, withAppShell, withRoutes } from '@angular/ssr';

provideServerRendering(
  withRoutes(serverRoutes),
  withAppShell(() =>
    import('./app-shell.component').then((m) => m.AppShellComponent)
  )
);
```

## Description

Configures the shell of the application.

The app shell is a minimal, static HTML page that is served immediately, while the full Angular application loads in the background. This improves perceived performance by providing instant feedback to the user.

This function configures the app shell route, which serves the provided component for requests that do not match any defined server routes.

## Usage Notes

```
import { provideServerRendering, withAppShell, withRoutes } from '@angular/ssr';
import { AppShellComponent } from './app-shell.component';

provideServerRendering(
  withRoutes(serverRoutes),
  withAppShell(AppShellComponent)
);
```

```
import { provideServerRendering, withAppShell, withRoutes } from '@angular/ssr';

provideServerRendering(
  withRoutes(serverRoutes),
  withAppShell(() =>
    import('./app-shell.component').then((m) => m.AppShellComponent)
  )
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/ssr/withAppShell>
