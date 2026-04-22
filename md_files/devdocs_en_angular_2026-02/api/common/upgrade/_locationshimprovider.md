# $locationShimProvider

$locationShimProvider



# $locationShimProvider

The factory function used to create an instance of the [`$locationShim`]($locationshim) in Angular, and provides an API-compatible `$locationProvider` for AngularJS.

## API

```
class $locationShimProvider {
  constructor(ngUpgrade: UpgradeModule, location: Location, platformLocation: PlatformLocation, urlCodec: UrlCodec, locationStrategy: LocationStrategy): $locationShimProvider;
  $get(): $locationShim;
  hashPrefix(prefix?: string | undefined): void;
  html5Mode(mode?: any): void;
}
```

### constructor

`$locationShimProvider`

@paramngUpgrade`UpgradeModule`

@paramlocation`Location`

@paramplatformLocation`PlatformLocation`

@paramurlCodec`UrlCodec`

@paramlocationStrategy`LocationStrategy`

@returns`$locationShimProvider`

### $get

`$locationShim`

Factory method that returns an instance of the $locationShim

@returns`$locationShim`

### hashPrefix

`void`

Stub method used to keep API compatible with AngularJS. This setting is configured through the LocationUpgradeModule's `config` method in your Angular app.

@paramprefix`string | undefined`

@returns`void`

### html5Mode

`void`

Stub method used to keep API compatible with AngularJS. This setting is configured through the LocationUpgradeModule's `config` method in your Angular app.

@parammode`any`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/upgrade/$locationShimProvider>
