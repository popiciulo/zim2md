# ViewContainerRef

ViewContainerRef



# ViewContainerRef

Represents a container where one or more views can be attached to a component.

[ComponentRef](componentref)[EmbeddedViewRef](embeddedviewref)

## API

```
abstract class ViewContainerRef {
  abstract readonly element: ElementRef<any>;
  abstract readonly injector: Injector;
  abstract readonly parentInjector: Injector;
  abstract clear(): void;
  abstract get(index: number): ViewRef | null;
  abstract readonly length: number;
  abstract createEmbeddedView<C>(templateRef: TemplateRef<C>, context?: C | undefined, options?: { index?: number | undefined; injector?: Injector | undefined; } | undefined): EmbeddedViewRef<C>;
  abstract createEmbeddedView<C>(templateRef: TemplateRef<C>, context?: C | undefined, index?: number | undefined): EmbeddedViewRef<C>;
  abstract createComponent<C>(componentType: Type<C>, options?: { index?: number | undefined; injector?: Injector | undefined; ngModuleRef?: NgModuleRef<unknown> | undefined; environmentInjector?: EnvironmentInjector | NgModuleRef<unknown> | undefined; projectableNodes?: Node[][] | undefined; directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined; bindings?: Binding[] | undefined; } | undefined): ComponentRef<C>;
  abstract createComponent<C>(componentFactory: ComponentFactory<C>, index?: number | undefined, injector?: Injector | undefined, projectableNodes?: any[][] | undefined, environmentInjector?: EnvironmentInjector | NgModuleRef<any> | undefined, directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined, bindings?: Binding[] | undefined): ComponentRef<C>;
  abstract insert(viewRef: ViewRef, index?: number | undefined): ViewRef;
  abstract move(viewRef: ViewRef, currentIndex: number): ViewRef;
  abstract indexOf(viewRef: ViewRef): number;
  abstract remove(index?: number | undefined): void;
  abstract detach(index?: number | undefined): ViewRef | null;
}
```

### element

`ElementRef<any>`

Anchor element that specifies the location of this container in the containing view. Each view container can have only one anchor element, and each anchor element can have only a single view container.

Root elements of views attached to this container become siblings of the anchor element in the rendered view.

Access the [`ViewContainerRef`](viewcontainerref) of an element by placing a [`Directive`](directive) injected with [`ViewContainerRef`](viewcontainerref) on the element, or use a [`ViewChild`](viewchild) query.

### injector

`Injector`

The dependency injector for this view container.

### parentInjector

`Injector`

@deprecated

No replacement

### clear

`void`

Destroys all views in this container.

@returns`void`

### get

`ViewRef | null`

Retrieves a view from this container.

@paramindex`number`

The 0-based index of the view to retrieve.

@returns`ViewRef | null`

### length

`number`

Reports how many views are currently attached to this container.

### createEmbeddedView

2 overloads

Instantiates an embedded view and inserts it into this container.

@paramtemplateRef`TemplateRef<C>`

The HTML template that defines the view.

@paramcontext`C | undefined`

The data-binding context of the embedded view, as declared in the `<ng-template>` usage.

@paramoptions`{ index?: number | undefined; injector?: Injector | undefined; } | undefined`

Extra configuration for the created view. Includes:

- index: The 0-based index at which to insert the new view into this container. If not specified, appends the new view as the last entry.
- injector: Injector to be used within the embedded view.

@returns`EmbeddedViewRef<C>`

Instantiates an embedded view and inserts it into this container.

@paramtemplateRef`TemplateRef<C>`

The HTML template that defines the view.

@paramcontext`C | undefined`

The data-binding context of the embedded view, as declared in the `<ng-template>` usage.

@paramindex`number | undefined`

The 0-based index at which to insert the new view into this container. If not specified, appends the new view as the last entry.

@returns`EmbeddedViewRef<C>`

### createComponent

2 overloads

Instantiates a component and inserts its host view into this view container.

@paramcomponentType`Type<C>`

Component Type to use.

@paramoptions`{ index?: number | undefined; injector?: Injector | undefined; ngModuleRef?: NgModuleRef<unknown> | undefined; environmentInjector?: EnvironmentInjector | NgModuleRef<unknown> | undefined; projectableNodes?: Node[][] | undefined; directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined; bindings?: Binding[] | undefined; } | undefined`

An object that contains extra parameters:

- index: the index at which to insert the new component's host view into this container. If not specified, appends the new view as the last entry.
- injector: the injector to use as the parent for the new component.
- ngModuleRef: an NgModuleRef of the component's NgModule, you should almost always provide this to ensure that all expected providers are available for the component instantiation.
- environmentInjector: an EnvironmentInjector which will provide the component's environment. you should almost always provide this to ensure that all expected providers are available for the component instantiation. This option is intended to replace the `ngModuleRef` parameter.
- projectableNodes: list of DOM nodes that should be projected through [`<ng-content>`](ng-content) of the new component instance.
- directives: Directives that should be applied to the component.
- bindings: Bindings that should be applied to the component.

@returns`ComponentRef<C>`

Instantiates a single component and inserts its host view into this container.

@deprecated

Angular no longer requires component factories to dynamically create components. Use different signature of the [`createComponent`](createcomponent) method, which allows passing Component class directly.

@paramcomponentFactory`ComponentFactory<C>`

Component factory to use.

@paramindex`number | undefined`

The index at which to insert the new component's host view into this container. If not specified, appends the new view as the last entry.

@paraminjector`Injector | undefined`

The injector to use as the parent for the new component.

@paramprojectableNodes`any[][] | undefined`

List of DOM nodes that should be projected through [`<ng-content>`](ng-content) of the new component instance.

@paramenvironmentInjector`EnvironmentInjector | NgModuleRef<any> | undefined`

@paramdirectives`(Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined`

Directives that should be applied to the component.

@parambindings`Binding[] | undefined`

Bindings that should be applied to the component.

@returns`ComponentRef<C>`

### insert

`ViewRef`

Inserts a view into this container.

@paramviewRef`ViewRef`

The view to insert.

@paramindex`number | undefined`

The 0-based index at which to insert the view. If not specified, appends the new view as the last entry.

@returns`ViewRef`

### move

`ViewRef`

Moves a view to a new location in this container.

@paramviewRef`ViewRef`

The view to move.

@paramcurrentIndex`number`

@returns`ViewRef`

### indexOf

`number`

Returns the index of a view within the current container.

@paramviewRef`ViewRef`

The view to query.

@returns`number`

### remove

`void`

Destroys a view attached to this container

@paramindex`number | undefined`

The 0-based index of the view to destroy. If not specified, the last view in the container is removed.

@returns`void`

### detach

`ViewRef | null`

Detaches a view from this container without destroying it. Use along with `insert()` to move a view within the current container.

@paramindex`number | undefined`

The 0-based index of the view to detach. If not specified, the last view in the container is detached.

@returns`ViewRef | null`

## Description

Represents a container where one or more views can be attached to a component.

Can contain *host views* (created by instantiating a component with the [`createComponent()`](createcomponent) method), and *embedded views* (created by instantiating a [`TemplateRef`](templateref) with the `createEmbeddedView()` method).

A view container instance can contain other view containers, creating a view hierarchy.

## Usage Notes

The example below demonstrates how the [`createComponent`](createcomponent) function can be used to create an instance of a ComponentRef dynamically and attach it to an ApplicationRef, so that it gets included into change detection cycles.

Note: the example uses standalone components, but the function can also be used for non-standalone components (declared in an NgModule) as well.

```
@Component({
  selector: 'dynamic',
  template: `<span>This is a content of a dynamic component.</span>`,
})
class DynamicComponent {
  vcr = inject(ViewContainerRef);
}

@Component({
  selector: 'app',
  template: `<main>Hi! This is the main content.</main>`,
})
class AppComponent {
  vcr = inject(ViewContainerRef);

  ngAfterViewInit() {
    const compRef = this.vcr.createComponent(DynamicComponent);
    compRef.changeDetectorRef.detectChanges();
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ViewContainerRef>
