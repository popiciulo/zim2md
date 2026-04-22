# generate library

generate library



# generate library

```
ng generate library[name][options]
```

```
ng generate lib[name][options]
```

Creates a new library project in your Angular workspace. Libraries are reusable collections of components, services, and other Angular artifacts that can be shared across multiple applications. This schematic simplifies the process of generating a new library with the necessary files and configurations.

## Arguments

### name

The name for the new library. This name will be used for the project directory and various identifiers within the library's code.

#### Value Type

`string`

## Options

### entry-file

The path to the library's public API file, relative to the workspace root. This file defines what parts of the library are accessible to applications that import it.

#### Value Type

`string`

#### Default

`public-api`

### prefix

A prefix to be added to the selectors of components generated within this library. For example, if the prefix is `my-lib` and you generate a component named `my-component`, the selector will be `my-lib-my-component`.

#### Value Type

`string`

#### Default

`lib`

### project-root

The root directory for the new library, relative to the workspace root. If not specified, the library will be created in a subfolder within the `projects` directory, using the library's name.

#### Value Type

`string`

### skip-install

Skip the automatic installation of packages. You will need to manually install the dependencies later.

#### Value Type

`boolean`

#### Default

`false`

### skip-package-json

Do not automatically add dependencies to the `package.json` file.

#### Value Type

`boolean`

#### Default

`false`

### skip-ts-config

Do not update the workspace `tsconfig.json` file to add a path mapping for the new library. The path mapping is needed to use the library in an application, but can be disabled here to simplify development.

#### Value Type

`boolean`

#### Default

`false`

### standalone

Create a library that utilizes the standalone API, eliminating the need for NgModules. This can simplify the structure of your library and its usage in applications.

#### Value Type

`boolean`

#### Default

`true`

### test-runner

The unit testing runner to use.

#### Value Type

`string`

#### Allowed Values

`karma`, `vitest`

#### Default

`vitest`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/library>
