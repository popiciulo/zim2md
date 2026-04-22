# twoWayBinding

twoWayBinding



# twoWayBinding

Creates a two-way binding.

[Binding inputs, outputs and setting host directives at creation](../../guide/components/programmatic-rendering#binding-inputs-outputs-and-setting-host-directives-at-creation)

## API

```
function twoWayBinding(
  publicName: string,
  value: WritableSignal<unknown>,
): Binding;
```

### twoWayBinding

`Binding`

Creates a two-way binding.

@parampublicName`string`

@paramvalue`WritableSignal<unknown>`

Writable signal from which to get the current value and to which to write new values.

### Usage example

In this example we create an instance of the `MyCheckbox` component and bind to its `value` input using a two-way binding.

```
const checkboxValue = signal('');

createComponent(MyCheckbox, {
bindings: [
twoWayBinding('value', checkboxValue),
],
});
```

@returns`Binding`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/twoWayBinding>
