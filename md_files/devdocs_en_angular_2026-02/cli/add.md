# add

add



# add

```
ng addng <collection>[options]
```

Adds the npm package for a published library to your workspace, and configures the project in the current working directory to use that library, as specified by the library's schematic. For example, adding `@angular/pwa` configures your project for PWA support:

```
ng add @angular/pwa
```

## Arguments

### collection

The package to be added.

#### Value Type

`string`

## Options

### defaults

Disable interactive input prompts for options with a default.

#### Value Type

`boolean`

#### Default

`false`

### dry-run

Run through and reports activity without writing out results.

#### Value Type

`boolean`

#### Default

`false`

### force

Force overwriting of existing files.

#### Value Type

`boolean`

#### Default

`false`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### interactive

Enable interactive input prompts.

#### Value Type

`boolean`

#### Default

`true`

### registry

The NPM registry to use.

#### Value Type

`string`

### skip-confirmation

Skip asking a confirmation prompt before installing and executing the package. Ensure package name is correct prior to using this option.

#### Value Type

`boolean`

#### Default

`false`

### verbose

Display additional details about internal operations during execution.

#### Value Type

`boolean`

#### Default

`false`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/add>
