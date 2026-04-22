# ComponentMirror

ComponentMirror



# ComponentMirror

An interface that describes the subset of component metadata that can be retrieved using the [`reflectComponentType`](reflectcomponenttype) function.

## API

```
interface ComponentMirror<C> {
  readonly selector: string;
  readonly type: Type<C>;
  readonly inputs: readonly { readonly propName: string; readonly templateName: string; readonly transform?: ((value: any) => any) | undefined; readonly isSignal: boolean; }[];
  readonly outputs: readonly { readonly propName: string; readonly templateName: string; }[];
  readonly ngContentSelectors: readonly string[];
  readonly isStandalone: boolean;
}
```

### selector

`string`

The component's HTML selector.

### type

`Type<C>`

The type of component the factory will create.

### inputs

`readonly { readonly propName: string; readonly templateName: string; readonly transform?: ((value: any) => any) | undefined; readonly isSignal: boolean; }[]`

The inputs of the component.

### outputs

`readonly { readonly propName: string; readonly templateName: string; }[]`

The outputs of the component.

### ngContentSelectors

`readonly string[]`

Selector for all  elements in the component.

### isStandalone

`boolean`

Whether this component is marked as standalone. Note: an extra flag, not present in [`ComponentFactory`](componentfactory).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ComponentMirror>
