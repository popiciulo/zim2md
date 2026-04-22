# generate resolver

generate resolver



# generate resolver

```
ng generate resolver[name][options]
```

```
ng generate r[name][options]
```

Creates a new resolver in your project. Resolvers are used to pre-fetch data before a route is activated, ensuring that the necessary data is available before the component is displayed. This can improve the user experience by preventing delays and loading states. This schematic generates a new resolver with the specified name and options.

## Arguments

### name

The name for the new resolver. This will be used to create the resolver's class and spec files (e.g., `my-resolver.resolver.ts` and `my-resolver.resolver.spec.ts`).

#### Value Type

`string`

## Options

### flat

Creates the new resolver files at the top level of the current project. If set to false, a new folder with the resolver's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### functional

Creates the resolver as a function `ResolveFn` instead of a class. Functional resolvers can be simpler for basic scenarios.

#### Value Type

`boolean`

#### Default

`true`

### project

The name of the project where the resolver should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the new resolver.

#### Value Type

`boolean`

#### Default

`false`

### type-separator

The separator character to use before the type within the generated file's name. For example, if you set the option to `.`, the file will be named `example.resolver.ts`.

#### Value Type

`string`

#### Allowed Values

`-`, `.`

#### Default

`-`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/resolver>
