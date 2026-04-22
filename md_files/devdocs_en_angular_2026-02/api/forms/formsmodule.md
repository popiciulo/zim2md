# FormsModule

FormsModule



# FormsModule

Exports the required providers and directives for template-driven forms, making them available for import by NgModules that import this module.

[Forms Overview](../../guide/forms)[Template-driven Forms Guide](../../guide/forms)

## API

```
class FormsModule {
  static withConfig(opts: { callSetDisabledState?: SetDisabledStateOption | undefined; }): ModuleWithProviders<FormsModule>;
}
```

### withConfig

`ModuleWithProviders<FormsModule>`

Provides options for configuring the forms module.

@paramopts`{ callSetDisabledState?: SetDisabledStateOption | undefined; }`

An object of configuration options

- `callSetDisabledState` Configures whether to `always` call `setDisabledState`, which is more correct, or to only call it `whenDisabled`, which is the legacy behavior.

@returns`ModuleWithProviders<FormsModule>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormsModule>
