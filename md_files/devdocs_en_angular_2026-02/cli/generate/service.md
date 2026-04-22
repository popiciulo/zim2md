# generate service

generate service



# generate service

```
ng generate service[name][options]
```

```
ng generate s[name][options]
```

Creates a new service in your project. Services are used to encapsulate reusable logic, such as data access, API calls, or utility functions. This schematic simplifies the process of generating a new service with the necessary files and boilerplate code.

## Arguments

### name

The name for the new service. This will be used to create the service's class and spec files (e.g., `my-service.service.ts` and `my-service.service.spec.ts`).

#### Value Type

`string`

## Options

### add-type-to-class-name

When true, the 'type' option will be appended to the generated class name. When false, only the file name will include the type.

#### Value Type

`boolean`

#### Default

`true`

### flat

Creates files at the top level of the project or the given path. If set to false, a new folder with the service's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### project

The name of the project where the service should be added. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the service.

#### Value Type

`boolean`

#### Default

`false`

### type

Append a custom type to the service's filename. For example, if you set the type to `service`, the file will be named `my-service.service.ts`.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/service>
