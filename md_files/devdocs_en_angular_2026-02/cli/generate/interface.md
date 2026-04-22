# generate interface

generate interface



# generate interface

```
ng generate interface[name] [type][options]
```

```
ng generate i[name] [type][options]
```

Creates a new interface in your project. Interfaces define the structure of objects in TypeScript, ensuring type safety and code clarity. This schematic generates a new interface with the specified name and type.

## Arguments

### name

The name for the new interface. This will be used to create the interface file (e.g., `my-interface.interface.ts`).

#### Value Type

`string`

### type

Adds a custom type to the filename, allowing you to create more descriptive interface names. For example, if you set the type to `data`, the filename will be `my-interface.data.ts`.

#### Value Type

`string`

## Options

### prefix

A prefix to be added to the interface name. This is typically not used for interfaces, as they don't have selectors like components or directives.

#### Value Type

`string`

### project

The name of the project where the interface should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/interface>
