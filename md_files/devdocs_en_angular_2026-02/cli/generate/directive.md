# generate directive

generate directive



# generate directive

```
ng generate directive[name][options]
```

```
ng generate d[name][options]
```

Creates a new directive in your project. Directives are used to extend the behavior or appearance of HTML elements and components. They allow you to manipulate the DOM, add custom attributes, and respond to events. This schematic generates the necessary files and boilerplate code for a new directive.

## Arguments

### name

The name for the new directive. This will be used to create the directive's class and spec files (e.g., `my-directive.directive.ts` and `my-directive.directive.spec.ts`).

#### Value Type

`string`

## Options

### add-type-to-class-name

When true, the 'type' option will be appended to the generated class name. When false, only the file name will include the type.

#### Value Type

`boolean`

#### Default

`true`

### export

Automatically export the directive from the specified NgModule, making it accessible to other modules in the application.

#### Value Type

`boolean`

#### Default

`false`

### flat

Creates the new directive files at the top level of the current project. If set to false, a new folder with the directive's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### module

Specify the NgModule where the directive should be declared. If not provided, the CLI will attempt to find the closest NgModule in the directive's path.

#### Value Type

`string`

### prefix

A prefix to be added to the directive's selector. For example, if the prefix is `app` and the directive name is `highlight`, the selector will be `appHighlight`.

#### Value Type

`string`

### project

The name of the project where the directive should be added. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### selector

The HTML selector to use for this directive. If not provided, a selector will be generated based on the directive's name (e.g., `appHighlight`).

#### Value Type

`string`

### skip-import

Do not automatically import the new directive into its closest NgModule.

#### Value Type

`boolean`

#### Default

`false`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the new directive.

#### Value Type

`boolean`

#### Default

`false`

### standalone

Generate a standalone directive. Standalone directives are self-contained and don't need to be declared in an NgModule. They can be used independently or imported directly into other standalone components or directives.

#### Value Type

`boolean`

#### Default

`true`

### type

Append a custom type to the directive's filename. For example, if you set the type to `directive`, the file will be named `example.directive.ts`.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/directive>
