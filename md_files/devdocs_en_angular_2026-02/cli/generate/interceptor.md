# generate interceptor

generate interceptor



# generate interceptor

```
ng generate interceptor[name][options]
```

Creates a new interceptor in your project. Interceptors are used to intercept and modify HTTP requests and responses before they reach their destination. This allows you to perform tasks like adding authentication headers, handling errors, or logging requests. This schematic generates the necessary files and boilerplate code for a new interceptor.

## Arguments

### name

The name for the new interceptor. This will be used to create the interceptor's class and spec files (e.g., `my-interceptor.interceptor.ts` and `my-interceptor.interceptor.spec.ts`).

#### Value Type

`string`

## Options

### flat

Creates the new interceptor files at the top level of the current project. If set to false, a new folder with the interceptor's name will be created to contain the files.

#### Value Type

`boolean`

#### Default

`true`

### functional

Creates the interceptor as a function `HttpInterceptorFn` instead of a class. Functional interceptors can be simpler for basic scenarios.

#### Value Type

`boolean`

#### Default

`true`

### project

The name of the project where the interceptor should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### skip-tests

Skip the generation of a unit test file `spec.ts` for the new interceptor.

#### Value Type

`boolean`

#### Default

`false`

### type-separator

The separator character to use before the type within the generated file's name. For example, if you set the option to `.`, the file will be named `example.interceptor.ts`.

#### Value Type

`string`

#### Allowed Values

`-`, `.`

#### Default

`-`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/interceptor>
