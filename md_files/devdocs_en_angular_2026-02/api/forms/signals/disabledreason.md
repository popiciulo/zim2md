# DisabledReason

DisabledReason



# DisabledReason

A reason for a field's disablement.

## API

```
interface DisabledReason {
  readonly field: FieldTree<unknown, string | number>;
  readonly message?: string | undefined;
}
```

### field

`FieldTree<unknown, string | number>`

The field that is disabled.

### message

`string | undefined`

A user-facing message describing the reason for the disablement.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/DisabledReason>
