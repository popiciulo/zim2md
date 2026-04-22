# generate application

generate application



# generate application

```
ng generate application[name][options]
```

```
ng generate app[name][options]
```

Generates a new Angular application within your workspace. This schematic sets up the foundational structure of your project, including the root component, module, and configuration files. You can customize various aspects of the application, such as routing, styling, and testing.

## Arguments

### name

The name for the new application. This name will be used for the project directory and various identifiers throughout the application's code.

#### Value Type

`string`

## Options

### file-name-style-guide

The file naming convention to use for generated files. The '2025' style guide (default) uses a concise format (e.g., `app.ts` for the root component), while the '2016' style guide includes the type in the file name (e.g., `app.component.ts`). For more information, see the Angular Style Guide (<https://angular.dev/style-guide>).

#### Value Type

`string`

#### Allowed Values

`2016`, `2025`

#### Default

`2025`

### inline-style

Include the styles for the root component directly within the `app.component.ts` file. Only CSS styles can be included inline. By default, a separate stylesheet file (e.g., `app.component.css`) is created.

#### Value Type

`boolean`

### inline-template

Include the HTML template for the root component directly within the `app.component.ts` file. By default, a separate template file (e.g., `app.component.html`) is created.

#### Value Type

`boolean`

### minimal

Generate a minimal project without any testing frameworks. This is intended for learning purposes and simple experimentation, not for production applications.

#### Value Type

`boolean`

#### Default

`false`

### prefix

A prefix to be added to the selectors of components generated within this application. For example, if the prefix is `my-app` and you generate a component named `my-component`, the selector will be `my-app-my-component`.

#### Value Type

`string`

#### Default

`app`

### project-root

The directory where the new application's files will be created, relative to the workspace root. If not specified, the application will be created in a subfolder within the `projects` directory, using the application's name.

#### Value Type

`string`

### routing

Generate an application with routing already configured. This sets up the necessary files and modules for managing navigation between different views in your application.

#### Value Type

`boolean`

#### Default

`true`

### skip-install

Skip the automatic installation of packages. You will need to manually install the dependencies later.

#### Value Type

`boolean`

#### Default

`false`

### skip-package-json

Do not add dependencies to the `package.json` file.

#### Value Type

`boolean`

#### Default

`false`

### skip-tests

Skip the generation of a unit test files `spec.ts`.

#### Value Type

`boolean`

#### Default

`false`

### ssr

Configure the application for Server-Side Rendering (SSR) and Static Site Generation (SSG/Prerendering).

#### Value Type

`boolean`

#### Default

`false`

### standalone

Create an application that utilizes the standalone API, eliminating the need for NgModules. This can simplify the structure of your application.

#### Value Type

`boolean`

#### Default

`true`

### strict

Enable stricter bundle budget settings for the application. This helps to keep your application's bundle size small and improve performance. For more information, see <https://angular.dev/tools/cli/template-typecheck#strict-mode>

#### Value Type

`boolean`

#### Default

`true`

### style

The type of stylesheet files to be created for components in the application.

#### Value Type

`string`

#### Allowed Values

`css`, `less`, `sass`, `scss`, `tailwind`

#### Default

`css`

### test-runner

The unit testing runner to use.

#### Value Type

`string`

#### Allowed Values

`karma`, `vitest`

#### Default

`vitest`

### view-encapsulation

Sets the view encapsulation mode for the application's components. This determines how component styles are scoped and applied.

#### Value Type

`string`

#### Allowed Values

`Emulated`, `None`, `ShadowDom`

### zoneless

Generate an application that does not use `zone.js`.

#### Value Type

`boolean`

#### Default

`true`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/application>
