# Setting up HttpClient

Setting up HttpClient



# Setting up [`HttpClient`](../../api/common/http/httpclient)

  

Before you can use [`HttpClient`](../../api/common/http/httpclient) in your app, you must configure it using [dependency injection](../di).

## Providing HttpClient through dependency injection

[`HttpClient`](../../api/common/http/httpclient) is provided using the [`provideHttpClient`](../../api/common/http/providehttpclient) helper function, which most apps include in the application `providers` in `app.config.ts`.

```
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
  ]
};
```

If your app is using NgModule-based bootstrap instead, you can include [`provideHttpClient`](../../api/common/http/providehttpclient) in the providers of your app's NgModule:

```
@NgModule({
  providers: [
    provideHttpClient(),
  ],
  // ... other application configuration
})
export class AppModule {}
```

You can then inject the [`HttpClient`](../../api/common/http/httpclient) service as a dependency of your components, services, or other classes:

```
@Injectable({providedIn: 'root'})
export class ConfigService {
  private http = inject(HttpClient);
  // This service can now make HTTP requests via `this.http`.
}
```

## Configuring features of HttpClient

[`provideHttpClient`](../../api/common/http/providehttpclient) accepts a list of optional feature configurations, to enable or configure the behavior of different aspects of the client. This section details the optional features and their usages.

### withFetch

```
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withFetch(),
    ),
  ]
};
```

By default, [`HttpClient`](../../api/common/http/httpclient) uses the [`XMLHttpRequest`](https://developer.mozilla.org/docs/Web/API/XMLHttpRequest) API to make requests. The [`withFetch`](../../api/common/http/withfetch) feature switches the client to use the [`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API) API instead.

`fetch` is a more modern API and is available in a few environments where `XMLHttpRequest` is not supported. It does have a few limitations, such as not producing upload progress events.

### withInterceptors(...)

[`withInterceptors`](../../api/common/http/withinterceptors) configures the set of interceptor functions which will process requests made through [`HttpClient`](../../api/common/http/httpclient). See the [interceptor guide](interceptors) for more information.

### withInterceptorsFromDi()

[`withInterceptorsFromDi`](../../api/common/http/withinterceptorsfromdi) includes the older style of class-based interceptors in the [`HttpClient`](../../api/common/http/httpclient) configuration. See the [interceptor guide](interceptors) for more information.

**HELPFUL:** Functional interceptors (through [`withInterceptors`](../../api/common/http/withinterceptors)) have more predictable ordering and we recommend them over DI-based interceptors.

### withRequestsMadeViaParent()

By default, when you configure [`HttpClient`](../../api/common/http/httpclient) using [`provideHttpClient`](../../api/common/http/providehttpclient) within a given injector, this configuration overrides any configuration for [`HttpClient`](../../api/common/http/httpclient) which may be present in the parent injector.

When you add [`withRequestsMadeViaParent()`](../../api/common/http/withrequestsmadeviaparent), [`HttpClient`](../../api/common/http/httpclient) is configured to instead pass requests up to the [`HttpClient`](../../api/common/http/httpclient) instance in the parent injector, once they've passed through any configured interceptors at this level. This is useful if you want to *add* interceptors in a child injector, while still sending the request through the parent injector's interceptors as well.

**CRITICAL:** You must configure an instance of [`HttpClient`](../../api/common/http/httpclient) above the current injector, or this option is not valid and you'll get a runtime error when you try to use it.

### withJsonpSupport()

Including [`withJsonpSupport`](../../api/common/http/withjsonpsupport) enables the `.jsonp()` method on [`HttpClient`](../../api/common/http/httpclient), which makes a GET request via the [JSONP convention](https://en.wikipedia.org/wiki/JSONP) for cross-domain loading of data.

**HELPFUL:** Prefer using [CORS](https://developer.mozilla.org/docs/Web/HTTP/CORS) to make cross-domain requests instead of JSONP when possible.

### withXsrfConfiguration(...)

Including this option allows for customization of [`HttpClient`](../../api/common/http/httpclient)'s built-in XSRF security functionality. See the [security guide](https://angular.dev/best-practices/security) for more information.

### withNoXsrfProtection()

Including this option disables [`HttpClient`](../../api/common/http/httpclient)'s built-in XSRF security functionality. See the [security guide](https://angular.dev/best-practices/security) for more information.

## HttpClientModule-based configuration

Some applications may configure [`HttpClient`](../../api/common/http/httpclient) using the older API based on NgModules.

This table lists the NgModules available from `@angular/common/http` and how they relate to the provider configuration functions above.

| **NgModule** | [`provideHttpClient()`](../../api/common/http/providehttpclient) equivalent |
| --- | --- |
| [`HttpClientModule`](../../api/common/http/httpclientmodule) | `provideHttpClient(withInterceptorsFromDi())` |
| [`HttpClientJsonpModule`](../../api/common/http/httpclientjsonpmodule) | [`withJsonpSupport()`](../../api/common/http/withjsonpsupport) |
| `HttpClientXsrfModule.withOptions(...)` | `withXsrfConfiguration(...)` |
| [`HttpClientXsrfModule.disable()`](../../api/common/http/httpclientxsrfmodule#disable) | [`withNoXsrfProtection()`](../../api/common/http/withnoxsrfprotection) |

### Use caution when using HttpClientModule in multiple injectors

When [`HttpClientModule`](../../api/common/http/httpclientmodule) is present in multiple injectors, the behavior of interceptors is poorly defined and depends on the exact options and provider/import ordering.

Prefer [`provideHttpClient`](../../api/common/http/providehttpclient) for multi-injector configurations, as it has more stable behavior. See the [`withRequestsMadeViaParent`](../../api/common/http/withrequestsmadeviaparent) feature above.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/http/setup>
