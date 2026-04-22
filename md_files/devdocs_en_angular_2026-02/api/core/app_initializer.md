# APP_INITIALIZER

APP\_INITIALIZER



# APP\_INITIALIZER

A DI token that you can use to provide one or more initialization functions.

[ApplicationInitStatus](applicationinitstatus)[provideAppInitializer](provideappinitializer)

Deprecation warning

from v19.0.0, use provideAppInitializer instead

## API

```
const APP_INITIALIZER: InjectionToken<readonly (() => any)[]>;
```

## Description

A DI token that you can use to provide one or more initialization functions.

The provided functions are injected at application startup and executed during app initialization. If any of these functions returns a Promise or an Observable, initialization does not complete until the Promise is resolved or the Observable is completed.

You can, for example, create a factory function that loads language data or an external configuration, and provide that function to the [`APP_INITIALIZER`](app_initializer) token. The function is executed during the application bootstrap process, and the needed data is available on startup.

Note that the provided initializer is run in the injection context.

## Usage Notes

The following example illustrates how to configure a multi-provider using [`APP_INITIALIZER`](app_initializer) token and a function returning a promise.

### Example with NgModule-based application

```
 function initializeApp(): Promise<any> {
   const http = inject(HttpClient);
   return firstValueFrom(
     http
       .get("https://someUrl.com/api/user")
       .pipe(tap(user => { ... }))
   );
 }

 @NgModule({
  imports: [BrowserModule],
  declarations: [AppComponent],
  bootstrap: [AppComponent],
  providers: [{
    provide: APP_INITIALIZER,
    useValue: initializeApp,
    multi: true,
   }]
  })
 export class AppModule {}
```

### Example with standalone application

```
function initializeApp() {
  const http = inject(HttpClient);
  return firstValueFrom(
    http
      .get("https://someUrl.com/api/user")
      .pipe(tap(user => { ... }))
  );
}

bootstrapApplication(App, {
  providers: [
    provideHttpClient(),
    {
      provide: APP_INITIALIZER,
      useValue: initializeApp,
      multi: true,
    },
  ],
});
```

It's also possible to configure a multi-provider using [`APP_INITIALIZER`](app_initializer) token and a function returning an observable, see an example below. Note: the `HttpClient` in this example is used for demo purposes to illustrate how the factory function can work with other providers available through DI.

### Example with NgModule-based application

```
function initializeApp() {
  const http = inject(HttpClient);
  return firstValueFrom(
    http
      .get("https://someUrl.com/api/user")
      .pipe(tap(user => { ... }))
  );
}

@NgModule({
  imports: [BrowserModule, HttpClientModule],
  declarations: [AppComponent],
  bootstrap: [AppComponent],
  providers: [{
    provide: APP_INITIALIZER,
    useValue: initializeApp,
    multi: true,
  }]
})
export class AppModule {}
```

### Example with standalone application

```
function initializeApp() {
  const http = inject(HttpClient);
  return firstValueFrom(
    http
      .get("https://someUrl.com/api/user")
      .pipe(tap(user => { ... }))
  );
}

bootstrapApplication(App, {
  providers: [
    provideHttpClient(),
    {
      provide: APP_INITIALIZER,
      useValue: initializeApp,
      multi: true,
    },
  ],
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/APP_INITIALIZER>
