# InputOptions

InputOptions



# InputOptions

[Input aliases](../../guide/components/inputs#input-aliases)[Input transforms](../../guide/components/inputs#input-transforms)

## API

```
interface InputOptions<T, TransformT> {
  alias?: string | undefined;
  transform?: ((v: TransformT) => T) | undefined;
  debugName?: string | undefined;
}
```

### alias

`string | undefined`

Optional public name for the input. By default, the class field name is used.

### transform

`((v: TransformT) => T) | undefined`

Optional transform that runs whenever a new value is bound. Can be used to transform the input value before the input is updated.

The transform function can widen the type of the input. For example, consider an input for `disabled`. In practice, as the component author, you want to only deal with a boolean, but users may want to bind a string if they just use the attribute form to bind to the input via `<my-dir input>`. A transform can then handle such string values and convert them to `boolean`. See: [`booleanAttribute`](booleanattribute).

### debugName

`string | undefined`

A debug name for the input signal. Used in Angular DevTools to identify the signal.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/InputOptions>
