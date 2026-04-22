# serve

serve



# serve

```
ng serveng [project][options]
```

```
ng devng [project][options]
```

```
ng sng [project][options]
```

Builds and serves your application, rebuilding on file changes.

## Arguments

### project

The name of the project to build. Can be an application or a library.

#### Value Type

`string`

## Options

### allowed-hosts

The hosts that the development server will respond to. This option sets the Vite option of the same name. For further details: <https://vite.dev/config/server-options.html#server-allowedhosts>

#### Value Type

`boolean`

### build-target

A build builder target to serve in the format of `project:target[:configuration]`. You can also pass in more than one configuration name as a comma-separated list. Example: `project:target:production,staging`.

#### Value Type

`string`

### configuration

One or more named builder configurations as a comma-separated list as specified in the "configurations" section in angular.json. The builder uses the named configurations to run the given target. For more information, see <https://angular.dev/reference/configs/workspace-config#alternate-build-configurations>.

#### Value Type

`string`

### define

Defines global identifiers that will be replaced with a specified constant value when found in any JavaScript or TypeScript code including libraries. The value will be used directly. String values must be put in quotes. Identifiers within Angular metadata such as Component Decorators will not be replaced.

#### Value Type

`array`

### headers

Custom HTTP headers to be added to all responses.

#### Value Type

`array`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### hmr

Enable hot module replacement. Defaults to the value of 'liveReload'. Currently, only global and component stylesheets are supported.

#### Value Type

`boolean`

### host

Host to listen on.

#### Value Type

`string`

#### Default

`localhost`

### inspect

Activate debugging inspector. This option only has an effect when 'SSR' or 'SSG' are enabled.

#### Value Type

`string`

### live-reload

Whether to reload the page on change, using live-reload.

#### Value Type

`boolean`

#### Default

`true`

### open

Opens the url in default browser.

#### Value Type

`boolean`

#### Default

`false`

### poll

Enable and define the file watching poll time period in milliseconds.

#### Value Type

`number`

### port

Port to listen on.

#### Value Type

`number`

#### Default

`4200`

### prebundle

Enable and control the Vite-based development server's prebundling capabilities. To enable prebundling, the Angular CLI cache must also be enabled.

#### Value Type

`boolean`

#### Default

`true`

### proxy-config

Proxy configuration file. For more information, see <https://angular.dev/tools/cli/serve#proxying-to-a-backend-server>.

#### Value Type

`string`

### serve-path

The pathname where the application will be served.

#### Value Type

`string`

### ssl

Serve using HTTPS.

#### Value Type

`boolean`

#### Default

`false`

### ssl-cert

SSL certificate to use for serving HTTPS.

#### Value Type

`string`

### ssl-key

SSL key to use for serving HTTPS.

#### Value Type

`string`

### verbose

Adds more details to output logging.

#### Value Type

`boolean`

### watch

Rebuild on change.

#### Value Type

`boolean`

#### Default

`true`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/serve>
