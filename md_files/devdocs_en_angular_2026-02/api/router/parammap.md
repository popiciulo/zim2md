# ParamMap

ParamMap



# ParamMap

A map that provides access to the required and optional parameters specific to a route. The map supports retrieving a single value with `get()` or multiple values with `getAll()`.

[URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)

## API

```
interface ParamMap {
  has(name: string): boolean;
  get(name: string): string | null;
  getAll(name: string): string[];
  readonly keys: string[];
}
```

### has

`boolean`

Reports whether the map contains a given parameter.

@paramname`string`

The parameter name.

@returns`boolean`

### get

`string | null`

Retrieves a single value for a parameter.

@paramname`string`

The parameter name.

@returns`string | null`

### getAll

`string[]`

Retrieves multiple values for a parameter.

@paramname`string`

The parameter name.

@returns`string[]`

### keys

`string[]`

Names of the parameters in the map.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ParamMap>
