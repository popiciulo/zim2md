# submit

submit



# submit

Submits a given [`FieldTree`](fieldtree) using the given action function and applies any server errors resulting from the action to the field. Server errors returned by the `action` will be integrated into the field as a [`ValidationError`](validationerror) on the sub-field indicated by the `field` property of the server error.

## API

```
function submit<TModel>(
  form: FieldTree<TModel>,
  action: (form: FieldTree<TModel>) => Promise<TreeValidationResult>,
): Promise<void>;
```

### submit

`Promise<void>`

Submits a given [`FieldTree`](fieldtree) using the given action function and applies any server errors resulting from the action to the field. Server errors returned by the `action` will be integrated into the field as a [`ValidationError`](validationerror) on the sub-field indicated by the `field` property of the server error.

@paramform`FieldTree<TModel>`

The field to submit.

@paramaction`(form: FieldTree<TModel>) => Promise<TreeValidationResult>`

An asynchronous action used to submit the field. The action may return server errors.

@returns`Promise<void>`

Usage notes

```
async function registerNewUser(registrationForm: FieldTree<{username: string, password: string}>) {
  const result = await myClient.registerNewUser(registrationForm().value());
  if (result.errorCode === myClient.ErrorCode.USERNAME_TAKEN) {
    return [{
      field: registrationForm.username,
      error: {kind: 'server', message: 'Username already taken'}
    }];
  }
  return undefined;
}

const registrationForm = form(signal({username: 'god', password: ''}));
submit(registrationForm, async (f) => {
  return registerNewUser(registrationForm);
});
registrationForm.username().errors(); // [{kind: 'server', message: 'Username already taken'}]
```

## Usage Notes

```
async function registerNewUser(registrationForm: FieldTree<{username: string, password: string}>) {
  const result = await myClient.registerNewUser(registrationForm().value());
  if (result.errorCode === myClient.ErrorCode.USERNAME_TAKEN) {
    return [{
      field: registrationForm.username,
      error: {kind: 'server', message: 'Username already taken'}
    }];
  }
  return undefined;
}

const registrationForm = form(signal({username: 'god', password: ''}));
submit(registrationForm, async (f) => {
  return registerNewUser(registrationForm);
});
registrationForm.username().errors(); // [{kind: 'server', message: 'Username already taken'}]
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/submit>
