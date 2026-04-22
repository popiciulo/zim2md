# UpgradeModule

UpgradeModule



# UpgradeModule

An [`NgModule`](../../core/ngmodule), which you import to provide AngularJS core services, and has an instance method used to bootstrap the hybrid upgrade application.

## API

```
class UpgradeModule {
  constructor(injector: Injector, ngZone: NgZone, platformRef: PlatformRef): UpgradeModule;
  $injector: any;
  injector: Injector;
  override ngZone: NgZone;
  bootstrap(element: Element, modules?: string[], config?: any): any;
}
```

### constructor

`UpgradeModule`

@paraminjector`Injector`

The root [`Injector`](../../core/injector) for the upgrade application.

@paramngZone`NgZone`

The bootstrap zone for the upgrade application

@paramplatformRef`PlatformRef`

The owning [`NgModuleRef`](../../core/ngmoduleref)s [`PlatformRef`](../../core/platformref) instance. This is used to tie the lifecycle of the bootstrapped AngularJS apps to that of the Angular [`PlatformRef`](../../core/platformref).

@returns`UpgradeModule`

### $injector

`any`

The AngularJS `$injector` for the upgrade application.

### injector

`Injector`

The Angular Injector \*

### ngZone

`NgZone`

The bootstrap zone for the upgrade application

### bootstrap

`any`

Bootstrap an AngularJS application from this NgModule

@paramelement`Element`

the element on which to bootstrap the AngularJS application

@parammodules`string[]`

the AngularJS modules to bootstrap for this application

@paramconfig`any`

optional extra AngularJS bootstrap configuration

@returns`any`

## Description

An [`NgModule`](../../core/ngmodule), which you import to provide AngularJS core services, and has an instance method used to bootstrap the hybrid upgrade application.

*Part of the [upgrade/static](../../../api?query=upgrade/static) library for hybrid upgrade apps that support AOT compilation*

The `upgrade/static` package contains helpers that allow AngularJS and Angular components to be used together inside a hybrid upgrade application, which supports AOT compilation.

Specifically, the classes and functions in the `upgrade/static` module allow the following:

1. Creation of an Angular directive that wraps and exposes an AngularJS component so that it can be used in an Angular template. See [`UpgradeComponent`](upgradecomponent).
2. Creation of an AngularJS directive that wraps and exposes an Angular component so that it can be used in an AngularJS template. See [`downgradeComponent`](downgradecomponent).
3. Creation of an Angular root injector provider that wraps and exposes an AngularJS service so that it can be injected into an Angular context. See [`Upgrading an AngularJS service`](upgrademodule#upgrading-an-angular-1-service) below.
4. Creation of an AngularJS service that wraps and exposes an Angular injectable so that it can be injected into an AngularJS context. See [`downgradeInjectable`](downgradeinjectable).
5. Bootstrapping of a hybrid Angular application which contains both of the frameworks coexisting in a single application.

## Usage Notes

```
import {UpgradeModule} from '@angular/upgrade/static';
```

See also the [`examples`](upgrademodule#examples) below.

### Mental Model

When reasoning about how a hybrid application works it is useful to have a mental model which describes what is happening and explains what is happening at the lowest level.

1. There are two independent frameworks running in a single application, each framework treats the other as a black box.
2. Each DOM element on the page is owned exactly by one framework. Whichever framework instantiated the element is the owner. Each framework only updates/interacts with its own DOM elements and ignores others.
3. AngularJS directives always execute inside the AngularJS framework codebase regardless of where they are instantiated.
4. Angular components always execute inside the Angular framework codebase regardless of where they are instantiated.
5. An AngularJS component can be "upgraded"" to an Angular component. This is achieved by defining an Angular directive, which bootstraps the AngularJS component at its location in the DOM. See [`UpgradeComponent`](upgradecomponent).
6. An Angular component can be "downgraded" to an AngularJS component. This is achieved by defining an AngularJS directive, which bootstraps the Angular component at its location in the DOM. See [`downgradeComponent`](downgradecomponent).
7. Whenever an "upgraded"/"downgraded" component is instantiated the host element is owned by the framework doing the instantiation. The other framework then instantiates and owns the view for that component.
   1. This implies that the component bindings will always follow the semantics of the instantiation framework.
   2. The DOM attributes are parsed by the framework that owns the current template. So attributes in AngularJS templates must use kebab-case, while AngularJS templates must use camelCase.
   3. However the template binding syntax will always use the Angular style, e.g. square brackets (`[...]`) for property binding.
8. Angular is bootstrapped first; AngularJS is bootstrapped second. AngularJS always owns the root component of the application.
9. The new application is running in an Angular zone, and therefore it no longer needs calls to `$apply()`.

### The UpgradeModule class

This class is an [`NgModule`](../../core/ngmodule), which you import to provide AngularJS core services, and has an instance method used to bootstrap the hybrid upgrade application.

- Core AngularJS services  
   Importing this [`NgModule`](../../core/ngmodule) will add providers for the core [AngularJS services](https://docs.angularjs.org/api/ng/service) to the root injector.
- Bootstrap  
   The runtime instance of this class contains a [`bootstrap()`](upgrademodule#bootstrap) method, which you use to bootstrap the top level AngularJS module onto an element in the DOM for the hybrid upgrade app.

  It also contains properties to access the [`root injector`](upgrademodule#injector), the bootstrap [`NgZone`](../../core/ngzone) and the [AngularJS $injector](https://docs.angularjs.org/api/auto/service/$injector).

### Examples

Import the [`UpgradeModule`](upgrademodule) into your top level Angular [`NgModule`](../../core/ngmodule).

```
// This NgModule represents the Angular pieces of the application
@NgModule({
  declarations: [Ng2HeroesComponent, Ng1HeroComponentWrapper],
  providers: [
    HeroesService,
    // Register an Angular provider whose value is the "upgraded" AngularJS service
    {provide: TextFormatter, useFactory: (i: any) => i.get('textFormatter'), deps: ['$injector']},
  ],
  // We must import `UpgradeModule` to get access to the AngularJS core services
  imports: [BrowserModule, UpgradeModule],
})
export class Ng2AppModule {
}
```

Then inject [`UpgradeModule`](upgrademodule) into your Angular [`NgModule`](../../core/ngmodule) and use it to bootstrap the top level [AngularJS module](https://docs.angularjs.org/api/ng/type/angular.Module) in the `ngDoBootstrap()` method.

```
export class Ng2AppModule {
  constructor(private upgrade: UpgradeModule) {}

  ngDoBootstrap() {
    // We bootstrap the AngularJS app.
    this.upgrade.bootstrap(document.body, [ng1AppModule.name]);
  }
}
```

Finally, kick off the whole process, by bootstrapping your top level Angular [`NgModule`](../../core/ngmodule).

```
// We bootstrap the Angular module as we would do in a normal Angular app.
// (We are using the dynamic browser platform as this example has not been compiled AOT.)
platformBrowser().bootstrapModule(Ng2AppModule);
```

### Upgrading an AngularJS service

There is no specific API for upgrading an AngularJS service. Instead you should just follow the following recipe:

Let's say you have an AngularJS service:

```
export class TextFormatter {
  titleCase(value: string) {
    return value.replace(/((^|\s)[a-z])/g, (_, c) => c.toUpperCase());
  }
}

// This AngularJS service will be "upgraded" to be used in Angular
ng1AppModule.service('textFormatter', [TextFormatter]);
```

Then you should define an Angular provider to be included in your [`NgModule`](../../core/ngmodule) `providers` property.

```
// Register an Angular provider whose value is the "upgraded" AngularJS service
    {provide: TextFormatter, useFactory: (i: any) => i.get('textFormatter'), deps: ['$injector']},
```

Then you can use the "upgraded" AngularJS service by injecting it into an Angular component or service.

```
constructor(textFormatter: TextFormatter) {
    // Change all the hero names to title case, using the "upgraded" AngularJS service
    this.heroes.forEach((hero: Hero) => (hero.name = textFormatter.titleCase(hero.name)));
  }
```

Super-powered by Google ©2010–2025.
