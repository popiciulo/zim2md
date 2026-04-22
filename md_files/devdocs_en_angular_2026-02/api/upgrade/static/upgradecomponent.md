# UpgradeComponent

UpgradeComponent



# UpgradeComponent

A helper class that allows an AngularJS component to be used from Angular.

## API

```
class UpgradeComponent implements OnInit ,OnChanges ,DoCheck ,OnDestroy {
  constructor(name: string, elementRef: ElementRef<any>, injector: Injector): UpgradeComponent;
}
```

### constructor

`UpgradeComponent`

Create a new [`UpgradeComponent`](upgradecomponent) instance. You should not normally need to do this. Instead you should derive a new class from this one and call the super constructor from the base class.

```
// This Angular directive will act as an interface to the "upgraded" AngularJS component
@Directive({
  selector: 'ng1-hero',
  standalone: false,
})
export class Ng1HeroComponentWrapper extends UpgradeComponent {
  // The names of the input and output properties here must match the names of the
  // `<` and `&` bindings in the AngularJS component that is being wrapped
  hero = input.required<Hero>();
  onRemove = output<void>();

  constructor(elementRef: ElementRef, injector: Injector) {
    // We must pass the name of the directive as used by AngularJS to the super
    super('ng1Hero', elementRef, injector);
  }
}
```

- The `name` parameter should be the name of the AngularJS directive.
- The `elementRef` and `injector` parameters should be acquired from Angular by dependency injection into the base class constructor.

@paramname`string`

@paramelementRef`ElementRef<any>`

@paraminjector`Injector`

@returns`UpgradeComponent`

## Description

A helper class that allows an AngularJS component to be used from Angular.

*Part of the [upgrade/static](../../../api?query=upgrade%2Fstatic) library for hybrid upgrade apps that support AOT compilation.*

This helper class should be used as a base class for creating Angular directives that wrap AngularJS components that need to be "upgraded".

## Usage Notes

### Examples

Let's assume that you have an AngularJS component called `ng1Hero` that needs to be made available in Angular templates.

```
// This AngularJS component will be "upgraded" to be used in Angular
ng1AppModule.component('ng1Hero', {
  bindings: {hero: '<', onRemove: '&'},
  transclude: true,
  template: `<div class="title" ng-transclude></div>
             <h2>{{ $ctrl.hero.name }}</h2>
             <p>{{ $ctrl.hero.description }}</p>
             <button ng-click="$ctrl.onRemove()">Remove</button>`,
});
```

We must create a [`Directive`](../../core/directive) that will make this AngularJS component available inside Angular templates.

```
// This Angular directive will act as an interface to the "upgraded" AngularJS component
@Directive({
  selector: 'ng1-hero',
  standalone: false,
})
export class Ng1HeroComponentWrapper extends UpgradeComponent {
  // The names of the input and output properties here must match the names of the
  // `<` and `&` bindings in the AngularJS component that is being wrapped
  hero = input.required<Hero>();
  onRemove = output<void>();

  constructor(elementRef: ElementRef, injector: Injector) {
    // We must pass the name of the directive as used by AngularJS to the super
    super('ng1Hero', elementRef, injector);
  }
}
```

In this example you can see that we must derive from the [`UpgradeComponent`](upgradecomponent) base class but also provide an `@Directive` decorator. This is because the AOT compiler requires that this information is statically available at compile time.

Note that we must do the following:

- specify the directive's selector (`ng1-hero`)
- specify all inputs and outputs that the AngularJS component expects
- derive from [`UpgradeComponent`](upgradecomponent)
- call the base class from the constructor, passing
  - the AngularJS name of the component (`ng1Hero`)
  - the [`ElementRef`](../../core/elementref) and [`Injector`](../../core/injector) for the component wrapper

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/upgrade/static/UpgradeComponent>
