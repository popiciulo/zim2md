# generate class

generate class



# generate class

```
ng generate class[name][options]
```

```
ng generate cl[name][options]
```

Creates a new class in your project. Classes are the fundamental building blocks for object-oriented programming in TypeScript. They provide a blueprint for creating objects with properties and methods. This schematic helps you generate a new class with the basic structure and optional test files.

## Arguments

### name

The name for the new class. This will be used to create the class file (e.g., `my-class.ts`) and, if enabled, the corresponding test file `my-class.spec.ts`.

#### Value Type

`string`

## Options

### project

The name of the project where the class should be added. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the new class.

#### Value Type

`boolean`

#### Default

`false`

### type

Adds a custom type to the filename, allowing you to create more descriptive class names. For example, if you set the type to `helper`, the filename will be `my-class.helper.ts`.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/class>
