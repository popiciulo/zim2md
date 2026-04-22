# SimpleChange

SimpleChange



# SimpleChange

Represents a basic change from a previous to a new value for a single property on a directive instance. Passed as a value in a [`SimpleChanges`](simplechanges) object to the `ngOnChanges` hook.

[OnChanges](onchanges)

## API

```
class SimpleChange<T = any> {
  constructor(previousValue: T, currentValue: T, firstChange: boolean): SimpleChange<T>;
  override previousValue: T;
  override currentValue: T;
  override firstChange: boolean;
  isFirstChange(): boolean;
}
```

### constructor

`SimpleChange<T>`

@parampreviousValue`T`

@paramcurrentValue`T`

@paramfirstChange`boolean`

@returns`SimpleChange<T>`

### previousValue

`T`

### currentValue

`T`

### firstChange

`boolean`

### isFirstChange

`boolean`

Check whether the new value is the first value assigned.

@returns`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/SimpleChange>
