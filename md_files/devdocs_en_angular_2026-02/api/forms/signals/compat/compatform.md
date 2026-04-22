# compatForm

compatForm



# compatForm

## API

```
function compatForm<TModel>(model: WritableSignal<TModel>): FieldTree<TModel>;
function compatForm<TModel>(
  model: WritableSignal<TModel>,
  schemaOrOptions: any,
): FieldTree<TModel>;
function compatForm<TModel>(
  model: WritableSignal<TModel>,
  schema: SchemaOrSchemaFn<TModel>,
  options: CompatFormOptions,
): FieldTree<TModel>;
```

```
function compatForm<TModel>(model: WritableSignal<TModel>): FieldTree<TModel>;
```

Creates a compatibility form wrapped around the given model data.

[`compatForm`](compatform) is a version of the `form` function that is designed for backwards compatibility with Reactive forms by accepting Reactive controls as a part of the data.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@returns`FieldTree<TModel>`

Usage notes

```
const lastName = new FormControl('lastName');

const nameModel = signal({
   first: '',
   last: lastName
});

const nameForm = compatForm(nameModel, (name) => {
  required(name.first);
});

nameForm.last().value(); // lastName, not FormControl
```

```
function compatForm<TModel>(model: WritableSignal<TModel>, schemaOrOptions: any): FieldTree<TModel>;
```

Creates a compatibility form wrapped around the given model data.

[`compatForm`](compatform) is a version of the `form` function that is designed for backwards compatibility with Reactive forms by accepting Reactive controls as a part of the data.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@paramschemaOrOptions`any`

The second argument can be either

1. A schema or a function used to specify logic for the form (e.g. validation, disabled fields, etc.). When passing a schema, the form options can be passed as a third argument if needed.
2. The form options (excluding adapter, since it's provided).

@returns`FieldTree<TModel>`

Usage notes

```
const lastName = new FormControl('lastName');

const nameModel = signal({
   first: '',
   last: lastName
});

const nameForm = compatForm(nameModel, (name) => {
  required(name.first);
});

nameForm.last().value(); // lastName, not FormControl
```

```
function compatForm<TModel>(model: WritableSignal<TModel>, schema: SchemaOrSchemaFn<TModel>, options: CompatFormOptions): FieldTree<TModel>;
```

Creates a compatibility form wrapped around the given model data.

[`compatForm`](compatform) is a version of the `form` function that is designed for backwards compatibility with Reactive forms by accepting Reactive controls as a part of the data.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@paramschema`SchemaOrSchemaFn<TModel>`

@paramoptions`CompatFormOptions`

The form options (excluding adapter, since it's provided).

@returns`FieldTree<TModel>`

Usage notes

```
const lastName = new FormControl('lastName');

const nameModel = signal({
   first: '',
   last: lastName
});

const nameForm = compatForm(nameModel, (name) => {
  required(name.first);
});

nameForm.last().value(); // lastName, not FormControl
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/compat/compatForm>
