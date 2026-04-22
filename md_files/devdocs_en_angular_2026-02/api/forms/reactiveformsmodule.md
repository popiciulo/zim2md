# ReactiveFormsModule

ReactiveFormsModule



# ReactiveFormsModule

Exports the required infrastructure and directives for reactive forms, making them available for import by NgModules that import this module.

[Forms Overview](../../guide/forms)[Reactive Forms Guide](../../guide/forms/reactive-forms)

## API

```
class ReactiveFormsModule {
  static withConfig(opts: { warnOnNgModelWithFormControl?: "always" | "never" | "once" | undefined; callSetDisabledState?: SetDisabledStateOption | undefined; }): ModuleWithProviders<ReactiveFormsModule>;
}
```

### withConfig

`ModuleWithProviders<ReactiveFormsModule>`

Provides options for configuring the reactive forms module.

@paramopts`{ warnOnNgModelWithFormControl?: "always" | "never" | "once" | undefined; callSetDisabledState?: SetDisabledStateOption | undefined; }`

An object of configuration options

- `warnOnNgModelWithFormControl` Configures when to emit a warning when an `ngModel` binding is used with reactive form directives.
- `callSetDisabledState` Configures whether to `always` call `setDisabledState`, which is more correct, or to only call it `whenDisabled`, which is the legacy behavior.

@returns`ModuleWithProviders<ReactiveFormsModule>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/ReactiveFormsModule>
