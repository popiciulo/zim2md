# createCustomElement

createCustomElement



# createCustomElement

Creates a custom element class based on an Angular component.

[Angular Elements Overview](../../guide/elements "Turning Angular components into custom elements")

## API

```
function createCustomElement<P>(
  component: Type<any>,
  config: NgElementConfig,
): NgElementConstructor<P>;
```

### createCustomElement

`NgElementConstructor<P>`

Creates a custom element class based on an Angular component.

Builds a class that encapsulates the functionality of the provided component and uses the configuration information to provide more context to the class. Takes the component factory's inputs and outputs to convert them to the proper custom element API and add hooks to input changes.

The configuration's injector is the initial injector set on the class, and used by default for each created instance.This behavior can be overridden with the static property to affect all newly created instances, or as a constructor argument for one-off creations.

@paramcomponent`Type<any>`

The component to transform.

@paramconfig`NgElementConfig`

A configuration that provides initialization information to the created class.

@returns`NgElementConstructor<P>`

## Description

Creates a custom element class based on an Angular component.

Builds a class that encapsulates the functionality of the provided component and uses the configuration information to provide more context to the class. Takes the component factory's inputs and outputs to convert them to the proper custom element API and add hooks to input changes.

The configuration's injector is the initial injector set on the class, and used by default for each created instance.This behavior can be overridden with the static property to affect all newly created instances, or as a constructor argument for one-off creations.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/createCustomElement>
