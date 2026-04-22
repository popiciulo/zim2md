# pattern

pattern



# pattern

Binds a validator to the given path that requires the value to match a specific regex pattern. This function can only be called on string paths. In addition to binding a validator, this function adds [`PATTERN`](pattern) property to the field.

## API

```
function pattern<TPathKind extends PathKind = PathKind.Root>(
  path: SchemaPath<string, 1, TPathKind>,
  pattern: RegExp | LogicFn<string | undefined, RegExp | undefined, TPathKind>,
  config?: BaseValidatorConfig<string, TPathKind> | undefined,
): void;
```

### pattern

`void`

Binds a validator to the given path that requires the value to match a specific regex pattern. This function can only be called on string paths. In addition to binding a validator, this function adds [`PATTERN`](pattern) property to the field.

@parampath`SchemaPath<string, 1, TPathKind>`

Path of the field to validate

@parampattern`RegExp | LogicFn<string | undefined, RegExp | undefined, TPathKind>`

The RegExp pattern to match, or a LogicFn that returns the RegExp pattern.

@paramconfig`BaseValidatorConfig<string, TPathKind> | undefined`

Optional, allows providing any of the following options:

- `error`: Custom validation error(s) to be used instead of the default [`ValidationError.pattern(pattern)`](validationerror#pattern(pattern)) or a function that receives the [`FieldContext`](fieldcontext) and returns custom validation error(s).

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/pattern>
