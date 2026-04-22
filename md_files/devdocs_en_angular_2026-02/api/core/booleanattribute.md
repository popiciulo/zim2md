# booleanAttribute

booleanAttribute



# booleanAttribute

Transforms a value (typically a string) to a boolean. Intended to be used as a transform function of an input.

[Built-in transformations](../../guide/components/inputs#built-in-transformations)

## API

```
function booleanAttribute(value: unknown): boolean;
```

### booleanAttribute

`boolean`

Transforms a value (typically a string) to a boolean. Intended to be used as a transform function of an input.

@paramvalue`unknown`

Value to be transformed.

@returns`boolean`

Usage notes

```
status = input({ transform: booleanAttribute });
```

## Usage Notes

```
status = input({ transform: booleanAttribute });
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/booleanAttribute>
