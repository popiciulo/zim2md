# numberAttribute

numberAttribute



# numberAttribute

Transforms a value (typically a string) to a number. Intended to be used as a transform function of an input.

[Built-in transformations](../../guide/components/inputs#built-in-transformations)

## API

```
function numberAttribute(value: unknown, fallbackValue?: number): number;
```

### numberAttribute

`number`

Transforms a value (typically a string) to a number. Intended to be used as a transform function of an input.

@paramvalue`unknown`

Value to be transformed.

@paramfallbackValue`number`

Value to use if the provided value can't be parsed as a number.

@returns`number`

Usage notes

```
 status = input({ transform: numberAttribute });
```

## Usage Notes

```
 status = input({ transform: numberAttribute });
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/numberAttribute>
