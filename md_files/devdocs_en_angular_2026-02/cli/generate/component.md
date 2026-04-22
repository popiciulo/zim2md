# generate component

generate component



# generate component

```
ng generate component[name][options]
```

```
ng generate c[name][options]
```

Creates a new Angular component. Components are the basic building blocks of Angular applications. Each component consists of a TypeScript class, an HTML template, and an optional CSS stylesheet. Use this schematic to generate a new component in your project.

## Arguments

### name

The name for the new component. This will be used to create the component's class, template, and stylesheet files. For example, if you provide `my-component`, the files will be named `my-component.ts`, `my-component.html`, and `my-component.css`.

#### Value Type

`string`

## Options

### add-type-to-class-name

When true, the 'type' option will be appended to the generated class name. When false, only the file name will include the type.

#### Value Type

`boolean`

#### Default

`true`

### change-detection

Configures the change detection strategy for the component.

#### Value Type

`string`

#### Allowed Values

`Default`, `OnPush`

#### Default

`Default`

### display-block

Adds `:host { display: block; }` to the component's stylesheet, ensuring the component renders as a block-level element. This is useful for layout purposes.

#### Value Type

`boolean`

#### Default

`false`

### export

Automatically export the component from the specified NgModule, making it accessible to other modules in the application.

#### Value Type

`boolean`

#### Default

`false`

### export-default

Use a default export for the component in its TypeScript file instead of a named export.

#### Value Type

`boolean`

#### Default

`false`

### flat

Create the component files directly in the project's `src/app` directory instead of creating a new folder for them.

#### Value Type

`boolean`

#### Default

`false`

### inline-style

Include the component's styles directly in the `component.ts` file. By default, a separate stylesheet file (e.g., `my-component.css`) is created.

#### Value Type

`boolean`

#### Default

`false`

### inline-template

Include the component's HTML template directly in the `component.ts` file. By default, a separate template file (e.g., `my-component.html`) is created.

#### Value Type

`boolean`

#### Default

`false`

### module

Specify the NgModule where the component should be declared. If not provided, the CLI will attempt to find the closest NgModule in the component's path.

#### Value Type

`string`

### ng-html

Generate component template files with an '.ng.html' file extension instead of '.html'.

#### Value Type

`boolean`

#### Default

`false`

### prefix

A prefix to be added to the component's selector. For example, if the prefix is `app` and the component name is `my-component`, the selector will be `app-my-component`.

#### Value Type

`string`

### project

The name of the project where the component should be added. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### selector

The HTML selector to use for this component. If not provided, a selector will be generated based on the component name (e.g., `app-my-component`).

#### Value Type

`string`

### skip-import

Do not automatically import the new component into its closest NgModule.

#### Value Type

`boolean`

#### Default

`false`

### skip-selector

Skip the generation of an HTML selector for the component.

#### Value Type

`boolean`

#### Default

`false`

### skip-tests

Skip the generation of unit test files `spec.ts`.

#### Value Type

`boolean`

#### Default

`false`

### standalone

Generate a standalone component. Standalone components are self-contained and don't need to be declared in an NgModule. They can be used independently or imported directly into other standalone components.

#### Value Type

`boolean`

#### Default

`true`

### style

Specify the type of stylesheet to be created for the component, or `none` to skip creating a stylesheet.

#### Value Type

`string`

#### Allowed Values

`css`, `less`, `none`, `sass`, `scss`

#### Default

`css`

### type

Append a custom type to the component's filename. For example, if you set the type to `container`, the file will be named `my-component.container.ts`.

#### Value Type

`string`

### view-encapsulation

Sets the view encapsulation mode for the component. This determines how the component's styles are scoped and applied.

#### Value Type

`string`

#### Allowed Values

`Emulated`, `None`, `ShadowDom`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/component>
