# form

form



# form

## API

```
function form<TModel>(model: WritableSignal<TModel>): FieldTree<TModel>;
function form<TModel>(
  model: WritableSignal<TModel>,
  schemaOrOptions: FormOptions | SchemaOrSchemaFn<TModel>,
): FieldTree<TModel>;
function form<TModel>(
  model: WritableSignal<TModel>,
  schema: SchemaOrSchemaFn<TModel>,
  options: FormOptions,
): FieldTree<TModel>;
```

```
function form<TModel>(model: WritableSignal<TModel>): FieldTree<TModel>;
```

Creates a form wrapped around the given model data. A form is represented as simply a [`FieldTree`](fieldtree) of the model data.

[`form`](form) uses the given model as the source of truth and *does not* maintain its own copy of the data. This means that updating the value on a [`FieldState`](fieldstate) updates the originally passed in model as well.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@returns`FieldTree<TModel>`

Usage notes

```
const nameModel = signal({first: '', last: ''});
const nameForm = form(nameModel);
nameForm.first().value.set('John');
nameForm().value(); // {first: 'John', last: ''}
nameModel(); // {first: 'John', last: ''}
```

```
function form<TModel>(model: WritableSignal<TModel>, schemaOrOptions: FormOptions | SchemaOrSchemaFn<TModel>): FieldTree<TModel>;
```

Creates a form wrapped around the given model data. A form is represented as simply a [`FieldTree`](fieldtree) of the model data.

[`form`](form) uses the given model as the source of truth and *does not* maintain its own copy of the data. This means that updating the value on a [`FieldState`](fieldstate) updates the originally passed in model as well.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@paramschemaOrOptions`FormOptions | SchemaOrSchemaFn<TModel>`

The second argument can be either

1. A schema or a function used to specify logic for the form (e.g. validation, disabled fields, etc.). When passing a schema, the form options can be passed as a third argument if needed.
2. The form options

@returns`FieldTree<TModel>`

Usage notes

```
const nameModel = signal({first: '', last: ''});
const nameForm = form(nameModel);
nameForm.first().value.set('John');
nameForm().value(); // {first: 'John', last: ''}
nameModel(); // {first: 'John', last: ''}
```

The form can also be created with a schema, which is a set of rules that define the logic for the form. The schema can be either a pre-defined schema created with the [`schema`](schema) function, or a function that builds the schema by binding logic to a parts of the field structure.

```
const nameForm = form(signal({first: '', last: ''}), (name) => {
  required(name.first);
  pattern(name.last, /^[a-z]+$/i, {message: 'Alphabet characters only'});
});
nameForm().valid(); // false
nameForm().value.set({first: 'John', last: 'Doe'});
nameForm().valid(); // true
```

```
function form<TModel>(model: WritableSignal<TModel>, schema: SchemaOrSchemaFn<TModel>, options: FormOptions): FieldTree<TModel>;
```

Creates a form wrapped around the given model data. A form is represented as simply a [`FieldTree`](fieldtree) of the model data.

[`form`](form) uses the given model as the source of truth and *does not* maintain its own copy of the data. This means that updating the value on a [`FieldState`](fieldstate) updates the originally passed in model as well.

@parammodel`WritableSignal<TModel>`

A writable signal that contains the model data for the form. The resulting field structure will match the shape of the model and any changes to the form data will be written to the model.

@paramschema`SchemaOrSchemaFn<TModel>`

A schema or a function used to specify logic for the form (e.g. validation, disabled fields, etc.)

@paramoptions`FormOptions`

The form options

@returns`FieldTree<TModel>`

Usage notes

```
const nameModel = signal({first: '', last: ''});
const nameForm = form(nameModel);
nameForm.first().value.set('John');
nameForm().value(); // {first: 'John', last: ''}
nameModel(); // {first: 'John', last: ''}
```

The form can also be created with a schema, which is a set of rules that define the logic for the form. The schema can be either a pre-defined schema created with the [`schema`](schema) function, or a function that builds the schema by binding logic to a parts of the field structure.

```
const nameForm = form(signal({first: '', last: ''}), (name) => {
  required(name.first);
  validate(name.last, ({value}) => !/^[a-z]+$/i.test(value()) ? customError({kind: 'alphabet-only'}) : undefined);
});
nameForm().valid(); // false
nameForm().value.set({first: 'John', last: 'Doe'});
nameForm().valid(); // true
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/form>
