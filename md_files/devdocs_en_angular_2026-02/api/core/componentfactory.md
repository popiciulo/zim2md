# ComponentFactory

ComponentFactory



# ComponentFactory

Base class for a factory that can create a component dynamically. Instantiate a factory for a given type of component with `resolveComponentFactory()`. Use the resulting [`ComponentFactory.create()`](componentfactory#create) method to create a component of that type.

Deprecation warning

Angular no longer requires Component factories. Please use other APIs where Component class can be used directly.

## API

```
abstract class ComponentFactory<C> {
  abstract readonly selector: string;
  abstract readonly componentType: Type<any>;
  abstract readonly ngContentSelectors: string[];
  abstract readonly inputs: { propName: string; templateName: string; transform?: ((value: any) => any) | undefined; isSignal: boolean; }[];
  abstract readonly outputs: { propName: string; templateName: string; }[];
  abstract create(injector: Injector, projectableNodes?: any[][] | undefined, rootSelectorOrNode?: any, environmentInjector?: EnvironmentInjector | NgModuleRef<any> | undefined, directives?: (Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined, bindings?: Binding[] | undefined): ComponentRef<C>;
}
```

### selector

`string`

The component's HTML selector.

### componentType

`Type<any>`

The type of component the factory will create.

### ngContentSelectors

`string[]`

Selector for all  elements in the component.

### inputs

`{ propName: string; templateName: string; transform?: ((value: any) => any) | undefined; isSignal: boolean; }[]`

The inputs of the component.

### outputs

`{ propName: string; templateName: string; }[]`

The outputs of the component.

### create

`ComponentRef<C>`

Creates a new component.

@paraminjector`Injector`

@paramprojectableNodes`any[][] | undefined`

@paramrootSelectorOrNode`any`

@paramenvironmentInjector`EnvironmentInjector | NgModuleRef<any> | undefined`

@paramdirectives`(Type<unknown> | DirectiveWithBindings<unknown>)[] | undefined`

@parambindings`Binding[] | undefined`

@returns`ComponentRef<C>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ComponentFactory>
