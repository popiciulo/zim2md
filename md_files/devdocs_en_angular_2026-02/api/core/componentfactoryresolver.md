# ComponentFactoryResolver

ComponentFactoryResolver



# ComponentFactoryResolver

A simple registry that maps `Components` to generated [`ComponentFactory`](componentfactory) classes that can be used to create instances of components. Use to obtain the factory for a given component type, then use the factory's `create()` method to create a component of that type.

Deprecation warning

Angular no longer requires Component factories. Please use other APIs where Component class can be used directly.

## API

```
abstract class ComponentFactoryResolver {
  abstract resolveComponentFactory<T>(component: Type<T>): ComponentFactory<T>;
  static NULL: ComponentFactoryResolver;
}
```

### resolveComponentFactory

`ComponentFactory<T>`

Retrieves the factory object that creates a component of the given type.

@paramcomponent`Type<T>`

The component type.

@returns`ComponentFactory<T>`

### NULL

`ComponentFactoryResolver`

## Description

A simple registry that maps `Components` to generated [`ComponentFactory`](componentfactory) classes that can be used to create instances of components. Use to obtain the factory for a given component type, then use the factory's `create()` method to create a component of that type.

Note: since v13, dynamic component creation via [`ViewContainerRef.createComponent`](viewcontainerref#createComponent) does **not** require resolving component factory: component class can be used directly.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ComponentFactoryResolver>
