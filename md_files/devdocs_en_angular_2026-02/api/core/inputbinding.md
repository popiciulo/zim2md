# inputBinding

inputBinding



# inputBinding

Creates an input binding.

[Binding inputs, outputs and setting host directives at creation](../../guide/components/programmatic-rendering#binding-inputs-outputs-and-setting-host-directives-at-creation)

## API

```
function inputBinding(publicName: string, value: () => unknown): Binding;
```

### inputBinding

`Binding`

Creates an input binding.

@parampublicName`string`

Public name of the input to bind to.

@paramvalue`() => unknown`

Callback that returns the current value for the binding. Can be either a signal or a plain getter function.

### Usage Example

In this example we create an instance of the `MyButton` component and bind the value of the `isDisabled` signal to its `disabled` input.

```
const isDisabled = signal(false);

createComponent(MyButton, {
bindings: [inputBinding('disabled', isDisabled)]
});
```

@returns`Binding`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/inputBinding>
