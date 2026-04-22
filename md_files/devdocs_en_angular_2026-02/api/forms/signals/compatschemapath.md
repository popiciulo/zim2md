# CompatSchemaPath

CompatSchemaPath



# CompatSchemaPath

Schema path used if the value is an AbstractControl.

## API

```
type CompatSchemaPath<TControl extends AbstractControl, TPathKind extends PathKind = PathKind.Root> = SchemaPath<
  TControl extends AbstractControl<unknown, infer TValue> ? TValue : never,
  SchemaPathRules.Unsupported,
  TPathKind
> &
  // & also we capture the control type, so that `stateOf(p)` can unwrap
  // to a correctly typed `CompatFieldState`.
  {
    [ɵɵTYPE]: {control: TControl};
  }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/CompatSchemaPath>
