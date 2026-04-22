# downgradeComponent

downgradeComponent



# downgradeComponent

A helper function that allows an Angular component to be used from AngularJS.

## API

```
function downgradeComponent(info: {
  component: Type<any>;
  downgradedModule?: string | undefined;
  propagateDigest?: boolean | undefined;
  inputs?: string[] | undefined;
  outputs?: string[] | undefined;
  selectors?: string[] | undefined;
}): any;
```

### downgradeComponent

`any`

A helper function that allows an Angular component to be used from AngularJS.

*Part of the [upgrade/static](../../../api?query=upgrade%2Fstatic) library for hybrid upgrade apps that support AOT compilation*

This helper function returns a factory function to be used for registering an AngularJS wrapper directive for "downgrading" an Angular component.

@paraminfo`{ component: Type<any>; downgradedModule?: string | undefined; propagateDigest?: boolean | undefined; inputs?: string[] | undefined; outputs?: string[] | undefined; selectors?: string[] | undefined; }`

contains information about the Component that is being downgraded:

- `component: Type<any>`: The type of the Component that will be downgraded
- `downgradedModule?: string`: The name of the downgraded module (if any) that the component "belongs to", as returned by a call to [`downgradeModule()`](downgrademodule). It is the module, whose corresponding Angular module will be bootstrapped, when the component needs to be instantiated.

  
 (This option is only necessary when using `downgradeModule()` to downgrade more than one Angular module.) - `propagateDigest?: boolean`: Whether to perform [`detectChanges`](../../core/changedetectorref#detectChanges) on the component on every [`$digest`](https://docs.angularjs.org/api/ng/type/$rootScope.Scope#$digest). If set to `false`, change detection will still be performed when any of the component's inputs changes. (Default: true)

@returns`any`

Usage notes

### Examples

Let's assume that you have an Angular component called `ng2Heroes` that needs to be made available in AngularJS templates.

{@example upgrade/static/ts/full/module.ts region="ng2-heroes"}

We must create an AngularJS [directive](https://docs.angularjs.org/guide/directive) that will make this Angular component available inside AngularJS templates. The [`downgradeComponent()`](downgradecomponent) function returns a factory function that we can use to define the AngularJS directive that wraps the "downgraded" component.

{@example upgrade/static/ts/full/module.ts region="ng2-heroes-wrapper"}

For more details and examples on downgrading Angular components to AngularJS components please visit the [Upgrade guide](https://angular.io/guide/upgrade#using-angular-components-from-angularjs-code).

## Description

A helper function that allows an Angular component to be used from AngularJS.

*Part of the [upgrade/static](../../../api?query=upgrade%2Fstatic) library for hybrid upgrade apps that support AOT compilation*

This helper function returns a factory function to be used for registering an AngularJS wrapper directive for "downgrading" an Angular component.

## Usage Notes

### Examples

Let's assume that you have an Angular component called `ng2Heroes` that needs to be made available in AngularJS templates.

```
// This Angular component will be "downgraded" to be used in AngularJS
@Component({
  selector: 'ng2-heroes',
  // This template uses the upgraded `ng1-hero` component
  // Note that because its element is compiled by Angular we must use camelCased attribute names
  template: `<header><ng-content selector="h1"></ng-content></header>
    <ng-content selector=".extra"></ng-content>
    <div *ngFor="let hero of heroes()">
      <ng1-hero [hero]="hero" (onRemove)="removeHero.emit(hero)"
        ><strong>Super Hero</strong></ng1-hero
      >
      </div>
    <button (click)="addHero.emit()">Add Hero</button>`,
  standalone: false,
})
export class Ng2HeroesComponent {
  heroes = input<Hero[]>([]);
  addHero = output<void>();
  removeHero = output<Hero>();
}
```

We must create an AngularJS [directive](https://docs.angularjs.org/guide/directive) that will make this Angular component available inside AngularJS templates. The [`downgradeComponent()`](downgradecomponent) function returns a factory function that we can use to define the AngularJS directive that wraps the "downgraded" component.

```
// This directive will act as the interface to the "downgraded" Angular component
ng1AppModule.directive('ng2Heroes', downgradeComponent({component: Ng2HeroesComponent}));
```

For more details and examples on downgrading Angular components to AngularJS components please visit the [Upgrade guide](https://angular.io/guide/upgrade#using-angular-components-from-angularjs-code).

Super-powered by Google ©2010–2025.
