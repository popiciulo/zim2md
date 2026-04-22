# ModelOptions

ModelOptions



# ModelOptions

## API

```
interface ModelOptions {
  alias?: string | undefined;
  debugName?: string | undefined;
}
```

### alias

`string | undefined`

Optional public name of the input side of the model. The output side will have the same name as the input, but suffixed with `Change`. By default, the class field name is used.

### debugName

`string | undefined`

A debug name for the model signal. Used in Angular DevTools to identify the signal.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ModelOptions>
