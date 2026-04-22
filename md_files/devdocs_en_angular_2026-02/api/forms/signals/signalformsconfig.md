# SignalFormsConfig

SignalFormsConfig



# SignalFormsConfig

Configuration options for signal forms.

## API

```
interface SignalFormsConfig {
  classes?: { [className: string]: (state: FieldState<unknown, string | number>) => boolean; } | undefined;
}
```

### classes

`{ [className: string]: (state: FieldState<unknown, string | number>) => boolean; } | undefined`

A map of CSS class names to predicate functions that determine when to apply them.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/SignalFormsConfig>
