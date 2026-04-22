# ValidationError

ValidationError



# ValidationError

Common interface for all validation errors.

## API

```
interface ValidationError {
  readonly kind: string;
  readonly message?: string | undefined;
}
```

### kind

`string`

Identifies the kind of error.

### message

`string | undefined`

Human readable error message.

### ValidationError.WithField

`interface`

Validation error with a field.

This is returned from field state, e.g., catField.errors() would be of a list of errors with `field: catField` bound to state.

```
interface WithField extends ValidationError {
  readonly field: FieldTree<unknown>;
  readonly override kind: string;
  readonly override message?: string | undefined;
}
```

### ValidationError.WithOptionalField

`interface`

Validation error with optional field.

This is generally used in places where the result might have a field. e.g., as a result of a [`validateTree`](validatetree), or when handling form submission.

```
interface WithOptionalField extends ValidationError {
  readonly field?: FieldTree<unknown> | undefined;
  readonly override kind: string;
  readonly override message?: string | undefined;
}
```

### ValidationError.WithoutField

`interface`

Validation error with no field.

This is used to strongly enforce that fields are not allowed in validation result.

```
interface WithoutField extends ValidationError {
  readonly field?: undefined;
  readonly override kind: string;
  readonly override message?: string | undefined;
}
```

## Description

Common interface for all validation errors.

This can be returned from validators.

It's also used by the creation functions to create an instance (e.g. [`requiredError`](requirederror), [`minError`](minerror), etc.).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/ValidationError>
