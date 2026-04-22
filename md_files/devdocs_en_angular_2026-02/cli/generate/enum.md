# generate enum

generate enum



# generate enum

```
ng generate enum[name][options]
```

```
ng generate e[name][options]
```

Creates a new enum in your project. Enums (enumerations) are a way to define a set of named constants, making your code more readable and maintainable. This schematic generates a new enum with the specified name and type.

## Arguments

### name

The name for the new enum. This will be used to create the enum file (e.g., `my-enum.enum.ts`).

#### Value Type

`string`

## Options

### project

The name of the project where the enum should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### type

Adds a custom type to the filename, allowing you to create more descriptive enum names. For example, if you set the type to `status`, the filename will be `my-enum.status.ts`.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/enum>
