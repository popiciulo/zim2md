# generate pipe

generate pipe



# generate pipe

```
ng generate pipe[name][options]
```

```
ng generate p[name][options]
```

Creates a new pipe in your project. Pipes are used to transform data for display in templates. They take input values and apply a specific transformation, such as formatting dates, currency, or filtering arrays. This schematic generates the necessary files and boilerplate code for a new pipe.

## Arguments

### name

The name for the new pipe. This will be used to create the pipe's class and spec files (e.g., `my-pipe.pipe.ts` and `my-pipe.pipe.spec.ts`).

#### Value Type

`string`

## Options

### export

Automatically export the pipe from the specified NgModule, making it accessible to other modules in the application.

#### Value Type

`boolean`

#### Default

`false`

### flat

Creates the new pipe files at the top level of the current project. If set to false, a new folder with the pipe's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### module

Specify the NgModule where the pipe should be declared. If not provided, the CLI will attempt to find the closest NgModule in the pipe's path.

#### Value Type

`string`

### project

The name of the project where the pipe should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-import

Do not automatically import the new pipe into its closest NgModule.

#### Value Type

`boolean`

#### Default

`false`

### skip-tests

Prevent the generation of a unit test file `spec.ts` for the new pipe.

#### Value Type

`boolean`

#### Default

`false`

### standalone

Generate a standalone pipe. Standalone pipes are self-contained and don't need to be declared in an NgModule. They can be used independently or imported directly into other standalone components, directives, or pipes.

#### Value Type

`boolean`

#### Default

`true`

### type-separator

The separator character to use before the type within the generated file's name. For example, if you set the option to `.`, the file will be named `example.pipe.ts`.

#### Value Type

`string`

#### Allowed Values

`-`, `.`

#### Default

`-`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/pipe>
