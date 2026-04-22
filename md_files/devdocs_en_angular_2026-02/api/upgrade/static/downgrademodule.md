# downgradeModule

downgradeModule



# downgradeModule

A helper function for creating an AngularJS module that can bootstrap an Angular module "on-demand" (possibly lazily) when a [`downgraded component`](downgradecomponent) needs to be instantiated.

## API

```
function downgradeModule<T>(
  moduleOrBootstrapFn:
    | Type<T>
    | ((extraProviders: StaticProvider[]) => Promise<NgModuleRef<T>>),
): string;
function downgradeModule<T>(moduleOrBootstrapFn: NgModuleFactory<T>): string;
```

```
function downgradeModule<T>(moduleOrBootstrapFn: Type<T> | ((extraProviders: StaticProvider[]) => Promise<NgModuleRef<T>>)): string;
```

A helper function for creating an AngularJS module that can bootstrap an Angular module "on-demand" (possibly lazily) when a [`downgraded component`](downgradecomponent) needs to be instantiated.

*Part of the [upgrade/static](../../../api?query=upgrade/static) library for hybrid upgrade apps that support AOT compilation.*

It allows loading/bootstrapping the Angular part of a hybrid application lazily and not having to pay the cost up-front. For example, you can have an AngularJS application that uses Angular for specific routes and only instantiate the Angular modules if/when the user visits one of these routes.

The Angular module will be bootstrapped once (when requested for the first time) and the same reference will be used from that point onwards.

[`downgradeModule()`](downgrademodule) requires either an [`NgModuleFactory`](../../core/ngmodulefactory), [`NgModule`](../../core/ngmodule) class or a function:

- [`NgModuleFactory`](../../core/ngmodulefactory): If you pass an [`NgModuleFactory`](../../core/ngmodulefactory), it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModuleFactory()`](../../core/platformref#bootstrapModuleFactory). NOTE: this type of the argument is deprecated. Please either provide an [`NgModule`](../../core/ngmodule) class or a bootstrap function instead.
- [`NgModule`](../../core/ngmodule) class: If you pass an NgModule class, it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModule()`](../../core/platformref#bootstrapModule).
- `Function`: If you pass a function, it is expected to return a promise resolving to an [`NgModuleRef`](../../core/ngmoduleref). The function is called with an array of extra [`Providers`](../../core/staticprovider) that are expected to be available from the returned [`NgModuleRef`](../../core/ngmoduleref)'s [`Injector`](../../core/injector).

[`downgradeModule()`](downgrademodule) returns the name of the created AngularJS wrapper module. You can use it to declare a dependency in your main AngularJS module.

{@example upgrade/static/ts/lite/module.ts region="basic-how-to"}

For more details on how to use [`downgradeModule()`](downgrademodule) see [Upgrading for Performance](https://angular.io/guide/upgrade).

@parammoduleOrBootstrapFn`Type<T> | ((extraProviders: StaticProvider[]) => Promise<NgModuleRef<T>>)`

@returns`string`

Usage notes

Apart from [`UpgradeModule`](upgrademodule), you can use the rest of the `upgrade/static` helpers as usual to build a hybrid application. Note that the Angular pieces (e.g. downgraded services) will not be available until the downgraded module has been bootstrapped, i.e. by instantiating a downgraded component.

You cannot use [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) in the same hybrid application.  
 Use one or the other.

### Differences with UpgradeModule

Besides their different API, there are two important internal differences between [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) that affect the behavior of hybrid applications:

1. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not bootstrap the main AngularJS module inside the [`Angular zone`](../../core/ngzone).
2. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not automatically run a [$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest) when changes are detected in the Angular part of the application.

What this means is that applications using [`UpgradeModule`](upgrademodule) will run change detection more frequently in order to ensure that both frameworks are properly notified about possible changes. This will inevitably result in more change detection runs than necessary.

[`downgradeModule()`](downgrademodule), on the other side, does not try to tie the two change detection systems as tightly, restricting the explicit change detection runs only to cases where it knows it is necessary (e.g. when the inputs of a downgraded component change). This improves performance, especially in change-detection-heavy applications, but leaves it up to the developer to manually notify each framework as needed.

For a more detailed discussion of the differences and their implications, see [Upgrading for Performance](https://angular.io/guide/upgrade).

You can manually trigger a change detection run in AngularJS using [scope.$apply(...)](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$apply) or [$rootScope.$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest).

You can manually trigger a change detection run in Angular using [`* ngZone.run(...)`](../../core/ngzone#run).

### Downgrading multiple modules

It is possible to downgrade multiple modules and include them in an AngularJS application. In that case, each downgraded module will be bootstrapped when an associated downgraded component or injectable needs to be instantiated.

Things to keep in mind, when downgrading multiple modules:

- Each downgraded component/injectable needs to be explicitly associated with a downgraded module. See [`downgradeComponent()`](downgradecomponent) and [`downgradeInjectable()`](downgradeinjectable) for more details.
- If you want some injectables to be shared among all downgraded modules, you can provide them as [`StaticProvider`](../../core/staticprovider)s, when creating the [`PlatformRef`](../../core/platformref) (e.g. via [`platformBrowser`](../../platform-browser/platformbrowser) or `platformBrowserDynamic`).
- When using [`bootstrapModule()`](../../core/platformref#bootstrapmodule) or [`bootstrapModuleFactory()`](../../core/platformref#bootstrapmodulefactory) to bootstrap the downgraded modules, each one is considered a "root" module. As a consequence, a new instance will be created for every injectable provided in `"root"` (via [`providedIn`](../../core/injectable#providedIn) If this is not your intention, you can have a shared module (that will act as act as the "root" module) and create all downgraded modules using that module's injector:

  {@example upgrade/static/ts/lite-multi-shared/module.ts region="shared-root-module"}

```
function downgradeModule<T>(moduleOrBootstrapFn: NgModuleFactory<T>): string;
```

A helper function for creating an AngularJS module that can bootstrap an Angular module "on-demand" (possibly lazily) when a [`downgraded component`](downgradecomponent) needs to be instantiated.

*Part of the [upgrade/static](../../../api?query=upgrade/static) library for hybrid upgrade apps that support AOT compilation.*

It allows loading/bootstrapping the Angular part of a hybrid application lazily and not having to pay the cost up-front. For example, you can have an AngularJS application that uses Angular for specific routes and only instantiate the Angular modules if/when the user visits one of these routes.

The Angular module will be bootstrapped once (when requested for the first time) and the same reference will be used from that point onwards.

[`downgradeModule()`](downgrademodule) requires either an [`NgModuleFactory`](../../core/ngmodulefactory), [`NgModule`](../../core/ngmodule) class or a function:

- [`NgModuleFactory`](../../core/ngmodulefactory): If you pass an [`NgModuleFactory`](../../core/ngmodulefactory), it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModuleFactory()`](../../core/platformref#bootstrapModuleFactory). NOTE: this type of the argument is deprecated. Please either provide an [`NgModule`](../../core/ngmodule) class or a bootstrap function instead.
- [`NgModule`](../../core/ngmodule) class: If you pass an NgModule class, it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModule()`](../../core/platformref#bootstrapModule).
- `Function`: If you pass a function, it is expected to return a promise resolving to an [`NgModuleRef`](../../core/ngmoduleref). The function is called with an array of extra [`Providers`](../../core/staticprovider) that are expected to be available from the returned [`NgModuleRef`](../../core/ngmoduleref)'s [`Injector`](../../core/injector).

[`downgradeModule()`](downgrademodule) returns the name of the created AngularJS wrapper module. You can use it to declare a dependency in your main AngularJS module.

{@example upgrade/static/ts/lite/module.ts region="basic-how-to"}

For more details on how to use [`downgradeModule()`](downgrademodule) see [Upgrading for Performance](https://angular.io/guide/upgrade).

@deprecated

Passing [`NgModuleFactory`](../../core/ngmodulefactory) as the [`downgradeModule`](downgrademodule) function argument is deprecated, please pass an NgModule class reference instead.

@parammoduleOrBootstrapFn`NgModuleFactory<T>`

@returns`string`

Usage notes

Apart from [`UpgradeModule`](upgrademodule), you can use the rest of the `upgrade/static` helpers as usual to build a hybrid application. Note that the Angular pieces (e.g. downgraded services) will not be available until the downgraded module has been bootstrapped, i.e. by instantiating a downgraded component.

You cannot use [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) in the same hybrid application.  
 Use one or the other.

### Differences with UpgradeModule

Besides their different API, there are two important internal differences between [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) that affect the behavior of hybrid applications:

1. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not bootstrap the main AngularJS module inside the [`Angular zone`](../../core/ngzone).
2. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not automatically run a [$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest) when changes are detected in the Angular part of the application.

What this means is that applications using [`UpgradeModule`](upgrademodule) will run change detection more frequently in order to ensure that both frameworks are properly notified about possible changes. This will inevitably result in more change detection runs than necessary.

[`downgradeModule()`](downgrademodule), on the other side, does not try to tie the two change detection systems as tightly, restricting the explicit change detection runs only to cases where it knows it is necessary (e.g. when the inputs of a downgraded component change). This improves performance, especially in change-detection-heavy applications, but leaves it up to the developer to manually notify each framework as needed.

For a more detailed discussion of the differences and their implications, see [Upgrading for Performance](https://angular.io/guide/upgrade).

You can manually trigger a change detection run in AngularJS using [scope.$apply(...)](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$apply) or [$rootScope.$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest).

You can manually trigger a change detection run in Angular using [`* ngZone.run(...)`](../../core/ngzone#run).

### Downgrading multiple modules

It is possible to downgrade multiple modules and include them in an AngularJS application. In that case, each downgraded module will be bootstrapped when an associated downgraded component or injectable needs to be instantiated.

Things to keep in mind, when downgrading multiple modules:

- Each downgraded component/injectable needs to be explicitly associated with a downgraded module. See [`downgradeComponent()`](downgradecomponent) and [`downgradeInjectable()`](downgradeinjectable) for more details.
- If you want some injectables to be shared among all downgraded modules, you can provide them as [`StaticProvider`](../../core/staticprovider)s, when creating the [`PlatformRef`](../../core/platformref) (e.g. via [`platformBrowser`](../../platform-browser/platformbrowser) or `platformBrowserDynamic`).
- When using [`bootstrapModule()`](../../core/platformref#bootstrapmodule) or [`bootstrapModuleFactory()`](../../core/platformref#bootstrapmodulefactory) to bootstrap the downgraded modules, each one is considered a "root" module. As a consequence, a new instance will be created for every injectable provided in `"root"` (via [`providedIn`](../../core/injectable#providedIn) If this is not your intention, you can have a shared module (that will act as act as the "root" module) and create all downgraded modules using that module's injector:

  {@example upgrade/static/ts/lite-multi-shared/module.ts region="shared-root-module"}

## Description

A helper function for creating an AngularJS module that can bootstrap an Angular module "on-demand" (possibly lazily) when a [`downgraded component`](downgradecomponent) needs to be instantiated.

*Part of the [upgrade/static](../../../api?query=upgrade/static) library for hybrid upgrade apps that support AOT compilation.*

It allows loading/bootstrapping the Angular part of a hybrid application lazily and not having to pay the cost up-front. For example, you can have an AngularJS application that uses Angular for specific routes and only instantiate the Angular modules if/when the user visits one of these routes.

The Angular module will be bootstrapped once (when requested for the first time) and the same reference will be used from that point onwards.

[`downgradeModule()`](downgrademodule) requires either an [`NgModuleFactory`](../../core/ngmodulefactory), [`NgModule`](../../core/ngmodule) class or a function:

- [`NgModuleFactory`](../../core/ngmodulefactory): If you pass an [`NgModuleFactory`](../../core/ngmodulefactory), it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModuleFactory()`](../../core/platformref#bootstrapModuleFactory). NOTE: this type of the argument is deprecated. Please either provide an [`NgModule`](../../core/ngmodule) class or a bootstrap function instead.
- [`NgModule`](../../core/ngmodule) class: If you pass an NgModule class, it will be used to instantiate a module using [`platformBrowser`](../../platform-browser/platformbrowser)'s [`bootstrapModule()`](../../core/platformref#bootstrapModule).
- `Function`: If you pass a function, it is expected to return a promise resolving to an [`NgModuleRef`](../../core/ngmoduleref). The function is called with an array of extra [`Providers`](../../core/staticprovider) that are expected to be available from the returned [`NgModuleRef`](../../core/ngmoduleref)'s [`Injector`](../../core/injector).

[`downgradeModule()`](downgrademodule) returns the name of the created AngularJS wrapper module. You can use it to declare a dependency in your main AngularJS module.

```
import {BrowserModule, platformBrowser} from '@angular/platform-browser';
import {downgradeComponent, downgradeModule, UpgradeComponent} from '@angular/upgrade/static';

// The function that will bootstrap the Angular module (when/if necessary).
// (This would be omitted if we provided an `NgModuleFactory` directly.)
const ng2BootstrapFn = (extraProviders: StaticProvider[]) =>
  platformBrowser(extraProviders).bootstrapModule(MyLazyAngularModule);
// This AngularJS module represents the AngularJS pieces of the application.
const myMainAngularJsModule = angular.module('myMainAngularJsModule', [
  // We declare a dependency on the "downgraded" Angular module.
  downgradeModule(ng2BootstrapFn),
  // or
  // downgradeModule(MyLazyAngularModuleFactory)
]);
```

For more details on how to use [`downgradeModule()`](downgrademodule) see [Upgrading for Performance](https://angular.io/guide/upgrade).

## Usage Notes

Apart from [`UpgradeModule`](upgrademodule), you can use the rest of the `upgrade/static` helpers as usual to build a hybrid application. Note that the Angular pieces (e.g. downgraded services) will not be available until the downgraded module has been bootstrapped, i.e. by instantiating a downgraded component.

You cannot use [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) in the same hybrid application.  
 Use one or the other.

### Differences with UpgradeModule

Besides their different API, there are two important internal differences between [`downgradeModule()`](downgrademodule) and [`UpgradeModule`](upgrademodule) that affect the behavior of hybrid applications:

1. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not bootstrap the main AngularJS module inside the [`Angular zone`](../../core/ngzone).
2. Unlike [`UpgradeModule`](upgrademodule), [`downgradeModule()`](downgrademodule) does not automatically run a [$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest) when changes are detected in the Angular part of the application.

What this means is that applications using [`UpgradeModule`](upgrademodule) will run change detection more frequently in order to ensure that both frameworks are properly notified about possible changes. This will inevitably result in more change detection runs than necessary.

[`downgradeModule()`](downgrademodule), on the other side, does not try to tie the two change detection systems as tightly, restricting the explicit change detection runs only to cases where it knows it is necessary (e.g. when the inputs of a downgraded component change). This improves performance, especially in change-detection-heavy applications, but leaves it up to the developer to manually notify each framework as needed.

For a more detailed discussion of the differences and their implications, see [Upgrading for Performance](https://angular.io/guide/upgrade).

You can manually trigger a change detection run in AngularJS using [scope.$apply(...)](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$apply) or [$rootScope.$digest()](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest).

You can manually trigger a change detection run in Angular using [`* ngZone.run(...)`](../../core/ngzone#run).

### Downgrading multiple modules

It is possible to downgrade multiple modules and include them in an AngularJS application. In that case, each downgraded module will be bootstrapped when an associated downgraded component or injectable needs to be instantiated.

Things to keep in mind, when downgrading multiple modules:

- Each downgraded component/injectable needs to be explicitly associated with a downgraded module. See [`downgradeComponent()`](downgradecomponent) and [`downgradeInjectable()`](downgradeinjectable) for more details.
- If you want some injectables to be shared among all downgraded modules, you can provide them as [`StaticProvider`](../../core/staticprovider)s, when creating the [`PlatformRef`](../../core/platformref) (e.g. via [`platformBrowser`](../../platform-browser/platformbrowser) or `platformBrowserDynamic`).
- When using [`bootstrapModule()`](../../core/platformref#bootstrapmodule) or [`bootstrapModuleFactory()`](../../core/platformref#bootstrapmodulefactory) to bootstrap the downgraded modules, each one is considered a "root" module. As a consequence, a new instance will be created for every injectable provided in `"root"` (via [`providedIn`](../../core/injectable#providedIn) If this is not your intention, you can have a shared module (that will act as act as the "root" module) and create all downgraded modules using that module's injector:

```
let rootInjectorPromise: Promise<Injector> | null = null;
const getRootInjector = (extraProviders: StaticProvider[]) => {
  if (!rootInjectorPromise) {
    rootInjectorPromise = platformBrowser(extraProviders)
      .bootstrapModule(Ng2RootModule)
      .then((moduleRef) => moduleRef.injector);
  }
  return rootInjectorPromise;
};

const downgradedNg2AModule = downgradeModule(async (extraProviders: StaticProvider[]) => {
  const rootInjector = await getRootInjector(extraProviders)!;
  const moduleAFactory = await rootInjector.get(Compiler).compileModuleAsync(Ng2AModule);
  return moduleAFactory.create(rootInjector);
});
const downgradedNg2BModule = downgradeModule(async (extraProviders: StaticProvider[]) => {
  const rootInjector = await getRootInjector(extraProviders)!;
  const moduleBFactory = await rootInjector.get(Compiler).compileModuleAsync(Ng2BModule);
  return moduleBFactory.create(rootInjector);
});
const appModule = angular
  .module('exampleAppModule', [downgradedNg2AModule, downgradedNg2BModule, downgradedNg2CModule])
```

Super-powered by Google ©2010–2025.
