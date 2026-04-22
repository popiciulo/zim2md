# AbstractType

AbstractType



# AbstractType

Represents an abstract class `T`, if applied to a concrete class it would stop being instantiable.

## API

```
interface AbstractType<T> extends Function {
  override apply(this: Function, thisArg: any, argArray?: any): any;
  override call(this: Function, thisArg: any, ...argArray: any[]): any;
  override bind(this: Function, thisArg: any, ...argArray: any[]): any;
  override toString(): string;
  readonly override length: number;
  override arguments: any;
  override caller: Function;
  readonly override name: string;
  override [Symbol.hasInstance](value: any): boolean;
}
```

### apply

`any`

Calls the function, substituting the specified object for the this value of the function, and the specified array for the arguments of the function.

@paramthis`Function`

@paramthisArg`any`

The object to be used as the this object.

@paramargArray`any`

A set of arguments to be passed to the function.

@returns`any`

### call

`any`

Calls a method of an object, substituting another object for the current object.

@paramthis`Function`

@paramthisArg`any`

The object to be used as the current object.

@paramargArray`any[]`

A list of arguments to be passed to the method.

@returns`any`

### bind

`any`

For a given function, creates a bound function that has the same body as the original function. The this object of the bound function is associated with the specified object, and has the specified initial parameters.

@paramthis`Function`

@paramthisArg`any`

An object to which the this keyword can refer inside the new function.

@paramargArray`any[]`

A list of arguments to be passed to the new function.

@returns`any`

### toString

`string`

Returns a string representation of a function.

@returns`string`

### length

`number`

### arguments

`any`

### caller

`Function`

### name

`string`

Returns the name of the function. Function names are read-only and can not be changed.

### [Symbol.hasInstance]

`boolean`

Determines whether the given value inherits from this function if this function was used as a constructor function.

A constructor function can control which objects are recognized as its instances by 'instanceof' by overriding this method.

@paramvalue`any`

@returns`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AbstractType>
