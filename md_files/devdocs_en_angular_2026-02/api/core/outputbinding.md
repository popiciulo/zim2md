# outputBinding

outputBinding



# outputBinding

Creates an output binding.

[Binding inputs, outputs and setting host directives at creation](../../guide/components/programmatic-rendering#binding-inputs-outputs-and-setting-host-directives-at-creation)

## API

```
function outputBinding<T>(
  eventName: string,
  listener: (event: T) => unknown,
): Binding;
```

### outputBinding

`Binding`

Creates an output binding.

@parameventName`string`

Public name of the output to listen to.

@paramlistener`(event: T) => unknown`

Function to be called when the output emits.

### Usage example

In this example we create an instance of the `MyCheckbox` component and listen to its `onChange` event.

```
interface CheckboxChange {
value: string;
}

createComponent(MyCheckbox, {
bindings: [
outputBinding<CheckboxChange>('onChange', event => console.log(event.value))
],
});
```

@returns`Binding`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/outputBinding>
