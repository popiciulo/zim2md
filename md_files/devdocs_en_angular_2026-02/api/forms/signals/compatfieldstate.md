# CompatFieldState

CompatFieldState



# CompatFieldState

This is FieldState also providing access to the wrapped FormControl.

## API

```
type CompatFieldState<TControl extends AbstractControl, TKey extends string | number = string | number> = FieldState<TControl extends AbstractControl<unknown, infer TValue> ? TValue : never, TKey> & {
  control: Signal<TControl>;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/CompatFieldState>
