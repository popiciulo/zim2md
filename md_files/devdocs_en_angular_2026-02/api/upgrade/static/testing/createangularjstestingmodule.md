# createAngularJSTestingModule

createAngularJSTestingModule



# createAngularJSTestingModule

A helper function to use when unit testing AngularJS services that depend upon downgraded Angular services.

## API

```
function createAngularJSTestingModule(angularModules: any[]): string;
```

### createAngularJSTestingModule

`string`

A helper function to use when unit testing AngularJS services that depend upon downgraded Angular services.

This function returns an AngularJS module that is configured to wire up the AngularJS and Angular injectors without the need to actually bootstrap a hybrid application. This makes it simpler and faster to unit test services.

Use the returned AngularJS module in a call to [`angular.mocks.module`](https://docs.angularjs.org/api/ngMock/function/angular.mock.module) to include this module in the unit test injector.

In the following code snippet, we are configuring the `$injector` with two modules: The AngularJS `ng1AppModule`, which is the AngularJS part of our hybrid application and the `Ng2AppModule`, which is the Angular part.

{@example upgrade/static/ts/full/module.spec.ts region='angularjs-setup'}

Once this is done we can get hold of services via the AngularJS `$injector` as normal. Services that are (or have dependencies on) a downgraded Angular service, will be instantiated as needed by the Angular root [`Injector`](../../../core/injector).

In the following code snippet, `heroesService` is a downgraded Angular service that we are accessing from AngularJS.

{@example upgrade/static/ts/full/module.spec.ts region='angularjs-spec'}

This helper is for testing services not components. For Component testing you must still bootstrap a hybrid app. See `UpgradeModule` or `downgradeModule` for more information.

The resulting configuration does not wire up AngularJS digests to Zone hooks. It is the responsibility of the test writer to call `$rootScope.$apply`, as necessary, to trigger AngularJS handlers of async events from Angular.

The helper sets up global variables to hold the shared Angular and AngularJS injectors.

- Only call this helper once per spec.
- Do not use [`createAngularJSTestingModule`](createangularjstestingmodule) in the same spec as [`createAngularTestingModule`](createangulartestingmodule).

Here is the example application and its unit tests that use [`createAngularTestingModule`](createangulartestingmodule) and [`createAngularJSTestingModule`](createangularjstestingmodule).

@paramangularModules`any[]`

a collection of Angular modules to include in the configuration.

@returns`string`

## Description

A helper function to use when unit testing AngularJS services that depend upon downgraded Angular services.

This function returns an AngularJS module that is configured to wire up the AngularJS and Angular injectors without the need to actually bootstrap a hybrid application. This makes it simpler and faster to unit test services.

Use the returned AngularJS module in a call to [`angular.mocks.module`](https://docs.angularjs.org/api/ngMock/function/angular.mock.module) to include this module in the unit test injector.

In the following code snippet, we are configuring the `$injector` with two modules: The AngularJS `ng1AppModule`, which is the AngularJS part of our hybrid application and the `Ng2AppModule`, which is the Angular part.

```
beforeEach(module(createAngularJSTestingModule([Ng2AppModule])));
  beforeEach(module(ng1AppModule.name));
```

Once this is done we can get hold of services via the AngularJS `$injector` as normal. Services that are (or have dependencies on) a downgraded Angular service, will be instantiated as needed by the Angular root [`Injector`](../../../core/injector).

In the following code snippet, `heroesService` is a downgraded Angular service that we are accessing from AngularJS.

```
it('should have access to the HeroesService', inject((heroesService: HeroesService) => {
    expect(heroesService).toBeDefined();
  }));
```

This helper is for testing services not components. For Component testing you must still bootstrap a hybrid app. See `UpgradeModule` or `downgradeModule` for more information.

The resulting configuration does not wire up AngularJS digests to Zone hooks. It is the responsibility of the test writer to call `$rootScope.$apply`, as necessary, to trigger AngularJS handlers of async events from Angular.

The helper sets up global variables to hold the shared Angular and AngularJS injectors.

- Only call this helper once per spec.
- Do not use [`createAngularJSTestingModule`](createangularjstestingmodule) in the same spec as [`createAngularTestingModule`](createangulartestingmodule).

Here is the example application and its unit tests that use [`createAngularTestingModule`](createangulartestingmodule) and [`createAngularJSTestingModule`](createangularjstestingmodule).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/upgrade/static/testing/createAngularJSTestingModule>
