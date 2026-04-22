# generate guard

generate guard



# generate guard

```
ng generate guard[name][options]
```

```
ng generate g[name][options]
```

Creates a new route guard in your project. Route guards are used to control access to parts of your application by checking certain conditions before a route is activated. This schematic generates a new guard with the specified name, type, and options.

## Arguments

### name

The name for the new route guard. This will be used to create the guard's class and spec files (e.g., `my-guard.guard.ts` and `my-guard.guard.spec.ts`).

#### Value Type

`string`

## Options

### flat

Creates the new guard files at the top level of the current project. If set to false, a new folder with the guard's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### functional

Generate the guard as a function instead of a class. Functional guards can be simpler for basic scenarios.

#### Value Type

`boolean`

#### Default

`true`

### implements

Specifies the type(s) of guard to create. You can choose one or more of the following: `CanActivate` (controls access to a route), `CanActivateChild` (controls access to child routes), `CanDeactivate` (asks for confirmation before leaving a route), `CanMatch` (determines if a route can be matched).

#### Value Type

`array`

#### Allowed Values

`CanActivate`, `CanActivateChild`, `CanDeactivate`, `CanMatch`

#### Default

`CanActivate`

### project

The name of the project where the guard should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the new guard.

#### Value Type

`boolean`

#### Default

`false`

### type-separator

The separator character to use before the type within the generated file's name. For example, if you set the option to `.`, the file will be named `example.guard.ts`.

#### Value Type

`string`

#### Allowed Values

`-`, `.`

#### Default

`-`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/guard>
