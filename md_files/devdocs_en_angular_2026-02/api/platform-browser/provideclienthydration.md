# provideClientHydration

provideClientHydration



# provideClientHydration

Sets up providers necessary to enable hydration functionality for the application.

[withNoHttpTransferCache](withnohttptransfercache)[withHttpTransferCacheOptions](withhttptransfercacheoptions)[withI18nSupport](withi18nsupport)[withEventReplay](witheventreplay)

## API

```
function provideClientHydration(
  ...features: HydrationFeature<HydrationFeatureKind>[]
): EnvironmentProviders;
```

### provideClientHydration

`EnvironmentProviders`

Sets up providers necessary to enable hydration functionality for the application.

By default, the function enables the recommended set of features for the optimal performance for most of the applications. It includes the following features:

- Reconciling DOM hydration. Learn more about it [here](../../guide/hydration).
- [`HttpClient`](../common/http/httpclient) response caching while running on the server and transferring this cache to the client to avoid extra HTTP requests. Learn more about data caching [here](../../guide/ssr#caching-data-when-using-httpclient).

These functions allow you to disable some of the default features or enable new ones:

- [`withNoHttpTransferCache`](withnohttptransfercache) to disable HTTP transfer cache
- [`withHttpTransferCacheOptions`](withhttptransfercacheoptions) to configure some HTTP transfer cache options
- [`withI18nSupport`](withi18nsupport) to enable hydration support for i18n blocks
- [`withEventReplay`](witheventreplay) to enable support for replaying user events

@paramfeatures`HydrationFeature<HydrationFeatureKind>[]`

Optional features to configure additional hydration behaviors.

@returns`EnvironmentProviders`

Usage notes

Basic example of how you can enable hydration in your application when [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration()]
});
```

Alternatively if you are using NgModules, you would add [`provideClientHydration`](provideclienthydration) to your root app module's provider list.

```
@NgModule({
  declarations: [RootCmp],
  bootstrap: [RootCmp],
  providers: [provideClientHydration()],
})
export class AppModule {}
```

## Description

Sets up providers necessary to enable hydration functionality for the application.

By default, the function enables the recommended set of features for the optimal performance for most of the applications. It includes the following features:

- Reconciling DOM hydration. Learn more about it [here](../../guide/hydration).
- [`HttpClient`](../common/http/httpclient) response caching while running on the server and transferring this cache to the client to avoid extra HTTP requests. Learn more about data caching [here](../../guide/ssr#caching-data-when-using-httpclient).

These functions allow you to disable some of the default features or enable new ones:

- [`withNoHttpTransferCache`](withnohttptransfercache) to disable HTTP transfer cache
- [`withHttpTransferCacheOptions`](withhttptransfercacheoptions) to configure some HTTP transfer cache options
- [`withI18nSupport`](withi18nsupport) to enable hydration support for i18n blocks
- [`withEventReplay`](witheventreplay) to enable support for replaying user events

## Usage Notes

Basic example of how you can enable hydration in your application when [`bootstrapApplication`](bootstrapapplication) function is used:

```
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration()]
});
```

Alternatively if you are using NgModules, you would add [`provideClientHydration`](provideclienthydration) to your root app module's provider list.

```
@NgModule({
  declarations: [RootCmp],
  bootstrap: [RootCmp],
  providers: [provideClientHydration()],
})
export class AppModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/provideClientHydration>
