# FormControlStatus

FormControlStatus



# FormControlStatus

A form can have several different statuses. Each possible status is returned as a string literal.

## API

```
type FormControlStatus = 'VALID' | 'INVALID' | 'PENDING' | 'DISABLED'
```

## Description

A form can have several different statuses. Each possible status is returned as a string literal.

- **VALID**: Reports that a control is valid, meaning that no errors exist in the input value.
- **INVALID**: Reports that a control is invalid, meaning that an error exists in the input value.
- **PENDING**: Reports that a control is pending, meaning that async validation is occurring and errors are not yet available for the input value.
- **DISABLED**: Reports that a control is disabled, meaning that the control is exempt from ancestor calculations of validity or value.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/FormControlStatus>
