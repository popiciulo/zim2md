# NgModuleRef

NgModuleRef



# NgModuleRef

Represents an instance of an [`NgModule`](ngmodule) created by an [`NgModuleFactory`](ngmodulefactory). Provides access to the [`NgModule`](ngmodule) instance and related objects.

## API

```
abstract class NgModuleRef<T> {
  abstract readonly injector: EnvironmentInjector;
  abstract readonly componentFactoryResolver: ComponentFactoryResolver;
  abstract readonly instance: T;
  abstract destroy(): void;
  abstract onDestroy(callback: () => void): void;
}
```

### injector

`EnvironmentInjector`

The injector that contains all of the providers of the [`NgModule`](ngmodule).

### componentFactoryResolver

`ComponentFactoryResolver`

@deprecated

Angular no longer requires Component factories. Please use other APIs where Component class can be used directly.

The resolver that can retrieve component factories in a context of this module.

Note: since v13, dynamic component creation via [`ViewContainerRef.createComponent`](viewcontainerref#createComponent) does **not** require resolving component factory: component class can be used directly.

### instance

`T`

The [`NgModule`](ngmodule) instance.

### destroy

`void`

Destroys the module instance and all of the data structures associated with it.

@returns`void`

### onDestroy

`void`

Registers a callback to be executed when the module is destroyed.

@paramcallback`() => void`

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/NgModuleRef>
