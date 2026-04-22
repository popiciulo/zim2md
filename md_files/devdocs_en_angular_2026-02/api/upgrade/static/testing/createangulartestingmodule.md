# createAngularTestingModule

createAngularTestingModule



# createAngularTestingModule

A helper function to use when unit testing Angular services that depend upon upgraded AngularJS services.

## API

```
function createAngularTestingModule(
  angularJSModules: string[],
  strictDi?: boolean | undefined,
): Type<any>;
```

### createAngularTestingModule

`Type<any>`

A helper function to use when unit testing Angular services that depend upon upgraded AngularJS services.

This function returns an [`NgModule`](../../../core/ngmodule) decorated class that is configured to wire up the Angular and AngularJS injectors without the need to actually bootstrap a hybrid application. This makes it simpler and faster to unit test services.

Use the returned class as an "import" when configuring the [`TestBed`](../../../core/testing/testbed).

In the following code snippet, we are configuring the TestBed with two imports. The `Ng2AppModule` is the Angular part of our hybrid application and the `ng1AppModule` is the AngularJS part.

{@example upgrade/static/ts/full/module.spec.ts region='angular-setup'}

Once this is done we can get hold of services via the Angular [`Injector`](../../../core/injector) as normal. Services that are (or have dependencies on) an upgraded AngularJS service, will be instantiated as needed by the AngularJS `$injector`.

In the following code snippet, `HeroesService` is an Angular service that depends upon an AngularJS service, `titleCase`.

{@example upgrade/static/ts/full/module.spec.ts region='angular-spec'}

This helper is for testing services not Components. For Component testing you must still bootstrap a hybrid app. See `UpgradeModule` or `downgradeModule` for more information.

The resulting configuration does not wire up AngularJS digests to Zone hooks. It is the responsibility of the test writer to call `$rootScope.$apply`, as necessary, to trigger AngularJS handlers of async events from Angular.

The helper sets up global variables to hold the shared Angular and AngularJS injectors.

- Only call this helper once per spec.
- Do not use [`createAngularTestingModule`](createangulartestingmodule) in the same spec as [`createAngularJSTestingModule`](createangularjstestingmodule).

Here is the example application and its unit tests that use [`createAngularTestingModule`](createangulartestingmodule) and [`createAngularJSTestingModule`](createangularjstestingmodule).

@paramangularJSModules`string[]`

a collection of the names of AngularJS modules to include in the configuration.

@paramstrictDi`boolean | undefined`

whether the AngularJS injector should have `strictDI` enabled.

@returns`Type<any>`

## Description

A helper function to use when unit testing Angular services that depend upon upgraded AngularJS services.

This function returns an [`NgModule`](../../../core/ngmodule) decorated class that is configured to wire up the Angular and AngularJS injectors without the need to actually bootstrap a hybrid application. This makes it simpler and faster to unit test services.

Use the returned class as an "import" when configuring the [`TestBed`](../../../core/testing/testbed).

In the following code snippet, we are configuring the TestBed with two imports. The `Ng2AppModule` is the Angular part of our hybrid application and the `ng1AppModule` is the AngularJS part.

```
import {TestBed} from '@angular/core/testing';
import {
  createAngularJSTestingModule,
  createAngularTestingModule,
} from '@angular/upgrade/static/testing';

import {HeroesService, ng1AppModule, Ng2AppModule} from './module';

const {module, inject} = (window as any).angular.mock;

beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [createAngularTestingModule([ng1AppModule.name]), Ng2AppModule],
    });
  });
```

Once this is done we can get hold of services via the Angular [`Injector`](../../../core/injector) as normal. Services that are (or have dependencies on) an upgraded AngularJS service, will be instantiated as needed by the AngularJS `$injector`.

In the following code snippet, `HeroesService` is an Angular service that depends upon an AngularJS service, `titleCase`.

```
it('should have access to the HeroesService', () => {
    const heroesService = TestBed.inject(HeroesService);
    expect(heroesService).toBeDefined();
  });
```

This helper is for testing services not Components. For Component testing you must still bootstrap a hybrid app. See `UpgradeModule` or `downgradeModule` for more information.

The resulting configuration does not wire up AngularJS digests to Zone hooks. It is the responsibility of the test writer to call `$rootScope.$apply`, as necessary, to trigger AngularJS handlers of async events from Angular.

The helper sets up global variables to hold the shared Angular and AngularJS injectors.

- Only call this helper once per spec.
- Do not use [`createAngularTestingModule`](createangulartestingmodule) in the same spec as [`createAngularJSTestingModule`](createangularjstestingmodule).

Here is the example application and its unit tests that use [`createAngularTestingModule`](createangulartestingmodule) and [`createAngularJSTestingModule`](createangularjstestingmodule).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/upgrade/static/testing/createAngularTestingModule>
