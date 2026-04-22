# NgValidationError

NgValidationError



# NgValidationError

The base class for all built-in, non-custom errors. This class can be used to check if an error is one of the standard kinds, allowing you to switch on the kind to further narrow the type.

## API

```
const NgValidationError: abstract new () => NgValidationError;
```

## Usage Notes

```
const f = form(...);
for (const e of form().errors()) {
  if (e instanceof NgValidationError) {
    switch(e.kind) {
      case 'required':
        console.log('This is required!');
        break;
      case 'min':
        console.log(`Must be at least ${e.min}`);
        break;
      ...
    }
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/NgValidationError>
