# provideZoneChangeDetection

provideZoneChangeDetection



# provideZoneChangeDetection

Provides [`NgZone`](ngzone)-based change detection for the application bootstrapped using `bootstrapApplication`.

[bootstrapApplication](../platform-browser/bootstrapapplication)[NgZoneOptions](ngzoneoptions)

## API

```
function provideZoneChangeDetection(
  options?: NgZoneOptions | undefined,
): EnvironmentProviders;
```

### provideZoneChangeDetection

`EnvironmentProviders`

Provides [`NgZone`](ngzone)-based change detection for the application bootstrapped using `bootstrapApplication`.

[`NgZone`](ngzone) is already provided in applications by default. This provider allows you to configure options like `eventCoalescing` in the [`NgZone`](ngzone). This provider is not available for `platformBrowser().bootstrapModule`, which uses [`BootstrapOptions`](bootstrapoptions) instead.

@paramoptions`NgZoneOptions | undefined`

@returns`EnvironmentProviders`

Usage notes

```
bootstrapApplication(MyApp, {providers: [
  provideZoneChangeDetection({eventCoalescing: true}),
]});
```

## Description

Provides [`NgZone`](ngzone)-based change detection for the application bootstrapped using `bootstrapApplication`.

[`NgZone`](ngzone) is already provided in applications by default. This provider allows you to configure options like `eventCoalescing` in the [`NgZone`](ngzone). This provider is not available for `platformBrowser().bootstrapModule`, which uses [`BootstrapOptions`](bootstrapoptions) instead.

## Usage Notes

```
bootstrapApplication(MyApp, {providers: [
  provideZoneChangeDetection({eventCoalescing: true}),
]});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/provideZoneChangeDetection>
