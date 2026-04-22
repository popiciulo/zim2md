# downgradeInjectable

downgradeInjectable



# downgradeInjectable

A helper function to allow an Angular service to be accessible from AngularJS.

## API

```
function downgradeInjectable(token: any, downgradedModule?: string): Function;
```

### downgradeInjectable

`Function`

A helper function to allow an Angular service to be accessible from AngularJS.

*Part of the [upgrade/static](../../../api?query=upgrade%2Fstatic) library for hybrid upgrade apps that support AOT compilation*

This helper function returns a factory function that provides access to the Angular service identified by the `token` parameter.

@paramtoken`any`

an `InjectionToken` that identifies a service provided from Angular.

@paramdowngradedModule`string`

the name of the downgraded module (if any) that the injectable "belongs to", as returned by a call to [`downgradeModule()`](downgrademodule). It is the module, whose injector will be used for instantiating the injectable.  
 (This option is only necessary when using [`downgradeModule()`](downgrademodule) to downgrade more than one Angular module.)

@returns`Function`

Usage notes

### Examples

First ensure that the service to be downgraded is provided in an [`NgModule`](../../core/ngmodule) that will be part of the upgrade application. For example, let's assume we have defined `HeroesService`

{@example upgrade/static/ts/full/module.ts region="ng2-heroes-service"}

and that we have included this in our upgrade app [`NgModule`](../../core/ngmodule)

{@example upgrade/static/ts/full/module.ts region="ng2-module"}

Now we can register the [`downgradeInjectable`](downgradeinjectable) factory function for the service on an AngularJS module.

{@example upgrade/static/ts/full/module.ts region="downgrade-ng2-heroes-service"}

Inside an AngularJS component's controller we can get hold of the downgraded service via the name we gave when downgrading.

{@example upgrade/static/ts/full/module.ts region="example-app"}

When using [`downgradeModule()`](downgrademodule), downgraded injectables will not be available until the Angular module that provides them is instantiated. In order to be safe, you need to ensure that the downgraded injectables are not used anywhere *outside* the part of the app where it is guaranteed that their module has been instantiated.

For example, it is *OK* to use a downgraded service in an upgraded component that is only used from a downgraded Angular component provided by the same Angular module as the injectable, but it is *not OK* to use it in an AngularJS component that may be used independently of Angular or use it in a downgraded Angular component from a different module.

## Description

A helper function to allow an Angular service to be accessible from AngularJS.

*Part of the [upgrade/static](../../../api?query=upgrade%2Fstatic) library for hybrid upgrade apps that support AOT compilation*

This helper function returns a factory function that provides access to the Angular service identified by the `token` parameter.

## Usage Notes

### Examples

First ensure that the service to be downgraded is provided in an [`NgModule`](../../core/ngmodule) that will be part of the upgrade application. For example, let's assume we have defined `HeroesService`

```
// This Angular service will be "downgraded" to be used in AngularJS
@Injectable()
export class HeroesService {
  heroes: Hero[] = [
    {name: 'superman', description: 'The man of steel'},
    {name: 'wonder woman', description: 'Princess of the Amazons'},
    {name: 'thor', description: 'The hammer-wielding god'},
  ];

  constructor(textFormatter: TextFormatter) {
    // Change all the hero names to title case, using the "upgraded" AngularJS service
    this.heroes.forEach((hero: Hero) => (hero.name = textFormatter.titleCase(hero.name)));
  }

  addHero() {
    this.heroes = this.heroes.concat([
      {name: 'Kamala Khan', description: 'Epic shape-shifting healer'},
    ]);
  }

  removeHero(hero: Hero) {
    this.heroes = this.heroes.filter((item: Hero) => item !== hero);
  }
}
```

and that we have included this in our upgrade app [`NgModule`](../../core/ngmodule)

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

Now we can register the [`downgradeInjectable`](downgradeinjectable) factory function for the service on an AngularJS module.

```
// Register an AngularJS service, whose value is the "downgraded" Angular injectable.
ng1AppModule.factory('heroesService', downgradeInjectable(HeroesService) as any);
```

Inside an AngularJS component's controller we can get hold of the downgraded service via the name we gave when downgrading.

```
// This is our top level application component
ng1AppModule.component('exampleApp', {
  // We inject the "downgraded" HeroesService into this AngularJS component
  // (We don't need the `HeroesService` type for AngularJS DI - it just helps with TypeScript
  // compilation)
  controller: [
    'heroesService',
    function (heroesService: HeroesService) {
      this.heroesService = heroesService;
    },
  ],
  // This template makes use of the downgraded `ng2-heroes` component
  // Note that because its element is compiled by AngularJS we must use kebab-case attributes
  // for inputs and outputs
  template: `<link rel="stylesheet" href="./styles.css">
          <ng2-heroes [heroes]="$ctrl.heroesService.heroes" (add-hero)="$ctrl.heroesService.addHero()" (remove-hero)="$ctrl.heroesService.removeHero($event)">
            <h1>Heroes</h1>
            <p class="extra">There are {{ $ctrl.heroesService.heroes.length }} heroes.</p>
          </ng2-heroes>`,
});
```

When using [`downgradeModule()`](downgrademodule), downgraded injectables will not be available until the Angular module that provides them is instantiated. In order to be safe, you need to ensure that the downgraded injectables are not used anywhere *outside* the part of the app where it is guaranteed that their module has been instantiated.

For example, it is *OK* to use a downgraded service in an upgraded component that is only used from a downgraded Angular component provided by the same Angular module as the injectable, but it is *not OK* to use it in an AngularJS component that may be used independently of Angular or use it in a downgraded Angular component from a different module.

Super-powered by Google ©2010–2025.
