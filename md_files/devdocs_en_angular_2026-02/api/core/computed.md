# computed

computed



# computed

Create a computed [`Signal`](signal) which derives a reactive value from an expression.

[Computed signals](../../guide/signals#computed-signals)

## API

```
function computed<T>(
  computation: () => T,
  options?: CreateComputedOptions<T> | undefined,
): Signal<T>;
```

### computed

`Signal<T>`

Create a computed [`Signal`](signal) which derives a reactive value from an expression.

@paramcomputation`() => T`

@paramoptions`CreateComputedOptions<T> | undefined`

@returns`Signal<T>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/computed>
