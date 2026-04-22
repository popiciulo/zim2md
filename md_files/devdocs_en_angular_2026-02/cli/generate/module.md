# generate module

generate module



# generate module

```
ng generate module[name][options]
```

```
ng generate m[name][options]
```

Creates a new, generic NgModule definition in the given project.

## Arguments

### name

The name of the NgModule.

#### Value Type

`string`

## Options

### flat

Create the new files at the top level of the current project root.

#### Value Type

`boolean`

#### Default

`false`

### module

The declaring NgModule.

#### Value Type

`string`

### project

The name of the project.

#### Value Type

`string`

### route

The route path for a lazy-loaded module. When supplied, creates a component in the new module, and adds the route to that component in the `Routes` array declared in the module provided in the `--module` option.

#### Value Type

`string`

### routing

Create a routing module.

#### Value Type

`boolean`

#### Default

`false`

### routing-scope

The scope for the new routing module.

#### Value Type

`string`

#### Allowed Values

`Child`, `Root`

#### Default

`Child`

### type-separator

The separator character to use before the type within the generated file's name. For example, if you set the option to `.`, the file will be named `example.module.ts`.

#### Value Type

`string`

#### Allowed Values

`-`, `.`

#### Default

`-`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/module>
