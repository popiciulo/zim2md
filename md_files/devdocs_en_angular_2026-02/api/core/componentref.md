# ComponentRef

ComponentRef



# ComponentRef

Represents a component created by a [`ComponentFactory`](componentfactory). Provides access to the component instance and related objects, and provides the means of destroying the instance.

[Programmatically rendering components](../../guide/components/programmatic-rendering)

## API

```
abstract class ComponentRef<C> {
  abstract setInput(name: string, value: unknown): void;
  abstract readonly location: ElementRef<any>;
  abstract readonly injector: Injector;
  abstract readonly instance: C;
  abstract readonly hostView: ViewRef;
  abstract readonly changeDetectorRef: ChangeDetectorRef;
  abstract readonly componentType: Type<any>;
  abstract destroy(): void;
  abstract onDestroy(callback: Function): void;
}
```

### setInput

`void`

Updates a specified input name to a new value. Using this method will properly mark for check component using the `OnPush` change detection strategy. It will also assure that the [`OnChanges`](onchanges) lifecycle hook runs when a dynamically created component is change-detected.

@paramname`string`

The name of an input.

@paramvalue`unknown`

The new value of an input.

@returns`void`

### location

`ElementRef<any>`

The host or anchor element for this component instance.

### injector

`Injector`

The dependency injector for this component instance.

### instance

`C`

This component instance.

### hostView

`ViewRef`

The host view defined by the template for this component instance.

### changeDetectorRef

`ChangeDetectorRef`

The change detector for this component instance.

### componentType

`Type<any>`

The type of this component (as created by a [`ComponentFactory`](componentfactory) class).

### destroy

`void`

Destroys the component instance and all of the data structures associated with it.

@returns`void`

### onDestroy

`void`

A lifecycle hook that provides additional developer-defined cleanup functionality for the component.

@paramcallback`Function`

A handler function that cleans up developer-defined data associated with this component. Called when the `destroy()` method is invoked.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ComponentRef>
