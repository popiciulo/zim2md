# build

build



# build

```
ng buildng [project][options]
```

```
ng bng [project][options]
```

The command can be used to build a project of type "application" or "library". When used to build a library, a different builder is invoked, and only the `ts-config`, `configuration`, `poll` and `watch` options are applied. All other options apply only to building applications.

The application builder uses the [esbuild](https://esbuild.github.io/) build tool, with default configuration options specified in the workspace configuration file (`angular.json`) or with a named alternative configuration. A "development" configuration is created by default when you use the CLI to create the project, and you can use that configuration by specifying the `--configuration development`.

The configuration options generally correspond to the command options. You can override individual configuration defaults by specifying the corresponding options on the command line. The command can accept option names given in dash-case. Note that in the configuration file, you must specify names in camelCase.

Some additional options can only be set through the configuration file, either by direct editing or with the `ng config` command. These include `assets`, `styles`, and `scripts` objects that provide runtime-global resources to include in the project. Resources in CSS, such as images and fonts, are automatically written and fingerprinted at the root of the output folder.

For further details, see [Workspace Configuration](https://angular.dev/reference/configs/workspace-config).

## Arguments

### project

The name of the project to build. Can be an application or a library.

#### Value Type

`string`

## Options

### allowed-common-js-dependencies

A list of CommonJS or AMD packages that are allowed to be used without a build time warning. Use `'*'` to allow all.

#### Value Type

`array`

### aot

Build using Ahead of Time compilation.

#### Value Type

`boolean`

#### Default

`true`

### app-shell

Generates an application shell during build time.

#### Value Type

`boolean`

### base-href

Base url for the application being built.

#### Value Type

`string`

### browser

The full path for the browser entry point to the application, relative to the current workspace.

#### Value Type

`string`

### clear-screen

Automatically clear the terminal screen during rebuilds.

#### Value Type

`boolean`

#### Default

`false`

### conditions

Custom package resolution conditions used to resolve conditional exports/imports. Defaults to ['module', 'development'/'production']. The following special conditions are always present if the requirements are satisfied: 'default', 'import', 'require', 'browser', 'node'.

#### Value Type

`array`

### configuration

One or more named builder configurations as a comma-separated list as specified in the "configurations" section in angular.json. The builder uses the named configurations to run the given target. For more information, see <https://angular.dev/reference/configs/workspace-config#alternate-build-configurations>.

#### Value Type

`string`

### cross-origin

Define the crossorigin attribute setting of elements that provide CORS support.

#### Value Type

`string`

#### Allowed Values

`anonymous`, `none`, `use-credentials`

#### Default

`none`

### define

Defines global identifiers that will be replaced with a specified constant value when found in any JavaScript or TypeScript code including libraries. The value will be used directly. String values must be put in quotes. Identifiers within Angular metadata such as Component Decorators will not be replaced.

#### Value Type

`array`

### delete-output-path

Delete the output path before building.

#### Value Type

`boolean`

#### Default

`true`

### deploy-url

Customize the base path for the URLs of resources in 'index.html' and component stylesheets. This option is only necessary for specific deployment scenarios, such as with Angular Elements or when utilizing different CDN locations.

#### Value Type

`string`

### external-dependencies

Exclude the listed external dependencies from being bundled into the bundle. Instead, the created bundle relies on these dependencies to be available during runtime. Note: `@foo/bar` marks all paths within the `@foo/bar` package as external, including sub-paths like `@foo/bar/baz`.

#### Value Type

`array`

### extract-licenses

Extract all licenses in a separate file.

#### Value Type

`boolean`

#### Default

`true`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### i18n-duplicate-translation

How to handle duplicate translations for i18n.

#### Value Type

`string`

#### Allowed Values

`error`, `ignore`, `warning`

#### Default

`warning`

### i18n-missing-translation

How to handle missing translations for i18n.

#### Value Type

`string`

#### Allowed Values

`error`, `ignore`, `warning`

#### Default

`warning`

### index

Configures the generation of the application's HTML index.

#### Value Type

`string`

### inline-style-language

The stylesheet language to use for the application's inline component styles.

#### Value Type

`string`

#### Allowed Values

`css`, `less`, `sass`, `scss`

#### Default

`css`

### localize

Translate the bundles in one or more locales.

#### Value Type

`boolean`

### named-chunks

Use file name for lazy loaded chunks.

#### Value Type

`boolean`

#### Default

`false`

### optimization

Enables optimization of the build output. Including minification of scripts and styles, tree-shaking, dead-code elimination, inlining of critical CSS and fonts inlining. For more information, see <https://angular.dev/reference/configs/workspace-config#optimization-configuration>.

#### Value Type

`boolean`

#### Default

`true`

### output-hashing

Define the output filename cache-busting hashing mode.

- `none`: No hashing.
- `all`: Hash for all output bundles.
- `media`: Hash for all output media (e.g., images, fonts, etc. that are referenced in CSS files).
- `bundles`: Hash for output of lazy and main bundles.

#### Value Type

`string`

#### Allowed Values

`all`, `bundles`, `media`, `none`

#### Default

`none`

### output-mode

Defines the type of build output artifact. 'static': Generates a static site build artifact for deployment on any static hosting service. 'server': Generates a server application build artifact, required for applications using hybrid rendering or APIs.

#### Value Type

`string`

#### Allowed Values

`server`, `static`

### output-path

Specify the output path relative to workspace root.

#### Value Type

`string`

### poll

Enable and define the file watching poll time period in milliseconds.

#### Value Type

`number`

### polyfills

A list of polyfills to include in the build. Can be a full path for a file, relative to the current workspace or module specifier. Example: 'zone.js'.

#### Value Type

`array`

### prerender

Prerender (SSG) pages of your application during build time.

#### Value Type

`boolean`

### preserve-symlinks

Do not use the real path when resolving modules. If unset then will default to `true` if NodeJS option --preserve-symlinks is set.

#### Value Type

`boolean`

### progress

Log progress to the console while building.

#### Value Type

`boolean`

#### Default

`true`

### scripts

Global scripts to be included in the build.

#### Value Type

`array`

### server

The full path for the server entry point to the application, relative to the current workspace.

#### Value Type

`string`

### service-worker

Generates a service worker configuration.

#### Value Type

`string`

### source-map

Output source maps for scripts and styles. For more information, see <https://angular.dev/reference/configs/workspace-config#source-map-configuration>.

#### Value Type

`boolean`

#### Default

`false`

### ssr

Server side render (SSR) pages of your application during runtime.

#### Value Type

`boolean`

#### Default

`false`

### stats-json

Generates a 'stats.json' file which can be analyzed with <https://esbuild.github.io/analyze/>.

#### Value Type

`boolean`

#### Default

`false`

### styles

Global styles to be included in the build.

#### Value Type

`array`

### subresource-integrity

Enables the use of subresource integrity validation.

#### Value Type

`boolean`

#### Default

`false`

### ts-config

The full path for the TypeScript configuration file, relative to the current workspace.

#### Value Type

`string`

### verbose

Adds more details to output logging.

#### Value Type

`boolean`

#### Default

`false`

### watch

Run build when files change.

#### Value Type

`boolean`

#### Default

`false`

### web-worker-ts-config

TypeScript configuration for Web Worker modules.

#### Value Type

`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/build>
