# disabled

disabled



# disabled

Adds logic to a field to conditionally disable it. A disabled field does not contribute to the validation, touched/dirty, or other state of its parent field.

## API

```
function disabled<TValue, TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<TValue, 1, TPathKind>,
  logic?:
    | string
    | NoInfer<LogicFn<TValue, string | boolean, TPathKind>>
    | undefined,
): void;
```

### disabled

`void`

Adds logic to a field to conditionally disable it. A disabled field does not contribute to the validation, touched/dirty, or other state of its parent field.

@parampath`SchemaPath<TValue, 1, TPathKind>`

The target path to add the disabled logic to.

@paramlogic`string | NoInfer<LogicFn<TValue, string | boolean, TPathKind>> | undefined`

A reactive function that returns `true` (or a string reason) when the field is disabled, and `false` when it is not disabled.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/disabled>
