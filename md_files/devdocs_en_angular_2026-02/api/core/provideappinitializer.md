# provideAppInitializer

provideAppInitializer



# provideAppInitializer

The provided function is injected at application startup and executed during app initialization. If the function returns a Promise or an Observable, initialization does not complete until the Promise is resolved or the Observable is completed.

[APP\_INITIALIZER](app_initializer)

## API

```
function provideAppInitializer(initializerFn: () => any): EnvironmentProviders;
```

### provideAppInitializer

`EnvironmentProviders`

The provided function is injected at application startup and executed during app initialization. If the function returns a Promise or an Observable, initialization does not complete until the Promise is resolved or the Observable is completed.

You can, for example, create a function that loads language data or an external configuration, and provide that function using [`provideAppInitializer()`](provideappinitializer). The function is executed during the application bootstrap process, and the needed data is available on startup.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`APP_INITIALIZER`](app_initializer) token which is now deprecated.

@paraminitializerFn`() => any`

@returns`EnvironmentProviders`

Usage notes

The following example illustrates how to configure an initialization function using [`provideAppInitializer()`](provideappinitializer)

```
bootstrapApplication(App, {
  providers: [
    provideAppInitializer(() => {
      const http = inject(HttpClient);
      return firstValueFrom(
        http
          .get("https://someUrl.com/api/user")
          .pipe(tap(user => { ... }))
      );
    }),
    provideHttpClient(),
  ],
});
```

## Description

The provided function is injected at application startup and executed during app initialization. If the function returns a Promise or an Observable, initialization does not complete until the Promise is resolved or the Observable is completed.

You can, for example, create a function that loads language data or an external configuration, and provide that function using [`provideAppInitializer()`](provideappinitializer). The function is executed during the application bootstrap process, and the needed data is available on startup.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`APP_INITIALIZER`](app_initializer) token which is now deprecated.

## Usage Notes

The following example illustrates how to configure an initialization function using [`provideAppInitializer()`](provideappinitializer)

```
bootstrapApplication(App, {
  providers: [
    provideAppInitializer(() => {
      const http = inject(HttpClient);
      return firstValueFrom(
        http
          .get("https://someUrl.com/api/user")
          .pipe(tap(user => { ... }))
      );
    }),
    provideHttpClient(),
  ],
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/provideAppInitializer>
