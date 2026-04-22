# AsyncValidatorOptions

AsyncValidatorOptions



# AsyncValidatorOptions

Options that indicate how to create a resource for async validation for a field, and map its result to validation errors.

## API

```
interface AsyncValidatorOptions<TValue, TParams, TResult, TPathKind extends PathKind = PathKind.Root> {
  readonly params: (ctx: FieldContext<TValue, TPathKind>) => TParams;
  readonly factory: (params: Signal<TParams | undefined>) => ResourceRef<TResult | undefined>;
  readonly onError: (error: unknown, ctx: FieldContext<TValue, TPathKind>) => TreeValidationResult;
  readonly onSuccess: MapToErrorsFn<TValue, TResult, TPathKind>;
}
```

### params

`(ctx: FieldContext<TValue, TPathKind>) => TParams`

A function that receives the field context and returns the params for the resource.

### factory

`(params: Signal<TParams | undefined>) => ResourceRef<TResult | undefined>`

A function that receives the resource params and returns a resource of the given params. The given params should be used as is to create the resource. The forms system will report the params as `undefined` when this validation doesn't need to be run.

### onError

`(error: unknown, ctx: FieldContext<TValue, TPathKind>) => TreeValidationResult`

A function to handle errors thrown by httpResource (HTTP errors, network errors, etc.). Receives the error and the field context, returns a list of validation errors.

### onSuccess

`MapToErrorsFn<TValue, TResult, TPathKind>`

A function that takes the resource result, and the current field context and maps it to a list of validation errors.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/AsyncValidatorOptions>
