# createComponent

createComponent



# createComponent

Creates a [`ComponentRef`](componentref) instance based on provided component type and a set of options.

[Host view using `ViewContainerRef.createComponent`](../../guide/components/programmatic-rendering#host-view-using-viewcontainerrefcreatecomponent)[Popup attached to `document.body` with `createComponent` + `hostElement`](../../guide/components/programmatic-rendering#popup-attached-to-documentbody-with-createcomponent--hostelement)

## API

```
function createComponent<C>(
  component: Type<C>,
  options: {
    environmentInjector: EnvironmentInjector;
    hostElement?: Element | undefined;
    elementInjector?: Injector | undefined;
    projectableNodes?: Node[][] | undefined;
    directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined;
    bindings?: Binding[] | undefined;
  },
): ComponentRef<C>;
```

### createComponent

`ComponentRef<C>`

Creates a [`ComponentRef`](componentref) instance based on provided component type and a set of options.

@paramcomponent`Type<C>`

Component class reference.

@paramoptions`{ environmentInjector: EnvironmentInjector; hostElement?: Element | undefined; elementInjector?: Injector | undefined; projectableNodes?: Node[][] | undefined; directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined; bindings?: Binding[] | undefined; }`

Set of options to use:

- `environmentInjector`: An [`EnvironmentInjector`](environmentinjector) instance to be used for the component.
- `hostElement` (optional): A DOM node that should act as a host node for the component. If not provided, Angular creates one based on the tag name used in the component selector (and falls back to using `div` if selector doesn't have tag name info).
- `elementInjector` (optional): An `ElementInjector` instance, see additional info about it [here](../../guide/di/hierarchical-dependency-injection#elementinjector).
- `projectableNodes` (optional): A list of DOM nodes that should be projected through [`<ng-content>`](ng-content) of the new component instance, e.g., `[[element1, element2]]`: projects `element1` and `element2` into the same `<ng-content>`. `[[element1, element2], [element3]]`: projects `element1` and `element2` into one `<ng-content>`, and `element3` into a separate `<ng-content>`.
- `directives` (optional): Directives that should be applied to the component.
- `bindings` (optional): Bindings to apply to the root component.

@returns`ComponentRef<C>`

Usage notes

The example below demonstrates how the [`createComponent`](createcomponent) function can be used to create an instance of a ComponentRef dynamically and attach it to an ApplicationRef, so that it gets included into change detection cycles.

Note: the example uses standalone components, but the function can also be used for non-standalone components (declared in an NgModule) as well.

```
@Component({
  template: `Hello {{ name }}!`
})
class HelloComponent {
  name = 'Angular';
}

@Component({
  template: `<div id="hello-component-host"></div>`
})
class RootComponent {}

// Bootstrap an application.
const applicationRef = await bootstrapApplication(RootComponent);

// Locate a DOM node that would be used as a host.
const hostElement = document.getElementById('hello-component-host');

// Get an `EnvironmentInjector` instance from the `ApplicationRef`.
const environmentInjector = applicationRef.injector;

// We can now create a `ComponentRef` instance.
const componentRef = createComponent(HelloComponent, {hostElement, environmentInjector});

// Last step is to register the newly created ref using the `ApplicationRef` instance
// to include the component view into change detection cycles.
applicationRef.attachView(componentRef.hostView);
componentRef.changeDetectorRef.detectChanges();
```

## Usage Notes

The example below demonstrates how the [`createComponent`](createcomponent) function can be used to create an instance of a ComponentRef dynamically and attach it to an ApplicationRef, so that it gets included into change detection cycles.

Note: the example uses standalone components, but the function can also be used for non-standalone components (declared in an NgModule) as well.

```
@Component({
  template: `Hello {{ name }}!`
})
class HelloComponent {
  name = 'Angular';
}

@Component({
  template: `<div id="hello-component-host"></div>`
})
class RootComponent {}

// Bootstrap an application.
const applicationRef = await bootstrapApplication(RootComponent);

// Locate a DOM node that would be used as a host.
const hostElement = document.getElementById('hello-component-host');

// Get an `EnvironmentInjector` instance from the `ApplicationRef`.
const environmentInjector = applicationRef.injector;

// We can now create a `ComponentRef` instance.
const componentRef = createComponent(HelloComponent, {hostElement, environmentInjector});

// Last step is to register the newly created ref using the `ApplicationRef` instance
// to include the component view into change detection cycles.
applicationRef.attachView(componentRef.hostView);
componentRef.changeDetectorRef.detectChanges();
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/createComponent>
