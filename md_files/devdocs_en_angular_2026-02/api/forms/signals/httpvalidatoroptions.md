# HttpValidatorOptions

HttpValidatorOptions



# HttpValidatorOptions

Options that indicate how to create an httpResource for async validation for a field, and map its result to validation errors.

## API

```
interface HttpValidatorOptions<TValue, TResult, TPathKind extends PathKind = PathKind.Root> {
  readonly request: ((ctx: FieldContext<TValue, TPathKind>) => string | undefined) | ((ctx: FieldContext<TValue, TPathKind>) => HttpResourceRequest | undefined);
  readonly onSuccess: MapToErrorsFn<TValue, TResult, TPathKind>;
  readonly onError: (error: unknown, ctx: FieldContext<TValue, TPathKind>) => TreeValidationResult;
  readonly options?: HttpResourceOptions<TResult, unknown> | undefined;
}
```

### request

`((ctx: FieldContext<TValue, TPathKind>) => string | undefined) | ((ctx: FieldContext<TValue, TPathKind>) => HttpResourceRequest | undefined)`

A function that receives the field context and returns the url or request for the httpResource. If given a URL, the underlying httpResource will perform an HTTP GET on it.

### onSuccess

`MapToErrorsFn<TValue, TResult, TPathKind>`

A function that takes the httpResource result, and the current field context and maps it to a list of validation errors.

### onError

`(error: unknown, ctx: FieldContext<TValue, TPathKind>) => TreeValidationResult`

A function to handle errors thrown by httpResource (HTTP errors, network errors, etc.). Receives the error and the field context, returns a list of validation errors.

### options

`HttpResourceOptions<TResult, unknown> | undefined`

The options to use when creating the httpResource.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/HttpValidatorOptions>
