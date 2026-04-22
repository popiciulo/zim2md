# FormOptions

FormOptions



# FormOptions

Options that may be specified when creating a form.

## API

```
interface FormOptions {
  injector?: Injector | undefined;
  name?: string | undefined;
  adapter?: FieldAdapter | undefined;
}
```

### injector

`Injector | undefined`

The injector to use for dependency injection. If this is not provided, the injector for the current [injection context](../../../guide/di/dependency-injection-context), will be used.

### name

`string | undefined`

### adapter

`FieldAdapter | undefined`

Adapter allows managing fields in a more flexible way. Currently this is used to support interop with reactive forms.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/FormOptions>
