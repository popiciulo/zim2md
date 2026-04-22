# PipeTransform

PipeTransform



# PipeTransform

An interface that is implemented by pipes in order to perform a transformation. Angular invokes the `transform` method with the value of a binding as the first argument, and any parameters as the second argument in list form.

## API

```
interface PipeTransform {
  transform(value: any, ...args: any[]): any;
}
```

### transform

`any`

@paramvalue`any`

@paramargs`any[]`

@returns`any`

## Usage Notes

In the following example, `TruncatePipe` returns the shortened value with an added ellipses.

Invoking `{{ 'It was the best of times' | truncate }}` in a template will produce `It was...`.

In the following example, `TruncatePipe` takes parameters that sets the truncated length and the string to append with.

Invoking `{{ 'It was the best of times' | truncate:4:'....' }}` in a template will produce `It was the best....`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/PipeTransform>
