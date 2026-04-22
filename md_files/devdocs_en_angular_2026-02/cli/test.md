# test

test



# test

```
ng testng [project][options]
```

```
ng tng [project][options]
```

Takes the name of the project, as specified in the `projects` section of the `angular.json` workspace configuration file. When a project name is not supplied, it will execute for all projects.

## Arguments

### project

The name of the project to build. Can be an application or a library.

#### Value Type

`string`

## Options

### browser-viewport

Specifies the browser viewport dimensions for browser-based tests in the format `widthxheight`.

#### Value Type

`string`

### browsers

Specifies the browsers to use for test execution. When not specified, tests are run in a Node.js environment using jsdom. For both Vitest and Karma, browser names ending with 'Headless' (e.g., 'ChromeHeadless') will enable headless mode.

#### Value Type

`array`

### build-target

Specifies the build target to use for the unit test build in the format `project:target[:configuration]`. This defaults to the `build` target of the current project with the `development` configuration. You can also pass a comma-separated list of configurations. Example: `project:target:production,staging`.

#### Value Type

`string`

### configuration

One or more named builder configurations as a comma-separated list as specified in the "configurations" section in angular.json. The builder uses the named configurations to run the given target. For more information, see <https://angular.dev/reference/configs/workspace-config#alternate-build-configurations>.

#### Value Type

`string`

### coverage

Enables coverage reporting for tests.

#### Value Type

`boolean`

#### Default

`false`

### coverage-exclude

Specifies glob patterns of files to exclude from the coverage report.

#### Value Type

`array`

### coverage-include

Specifies glob patterns of files to include in the coverage report.

#### Value Type

`array`

### coverage-reporters

Specifies the reporters to use for coverage results. Each reporter can be a string representing its name, or a tuple containing the name and an options object. Built-in reporters include 'html', 'lcov', 'lcovonly', 'text', 'text-summary', 'cobertura', 'json', and 'json-summary'.

#### Value Type

`array`

#### Allowed Values

`cobertura`, `html`, `json`, `json-summary`, `lcov`, `lcovonly`, `text`, `text-summary`

### debug

Enables debugging mode for tests, allowing the use of the Node Inspector.

#### Value Type

`boolean`

#### Default

`false`

### exclude

Specifies glob patterns of files to exclude from testing, relative to the project root.

#### Value Type

`array`

### filter

Specifies a regular expression pattern to match against test suite and test names. Only tests with a name matching the pattern will be executed. For example, `^App` will run only tests in suites beginning with 'App'.

#### Value Type

`string`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### include

Specifies glob patterns of files to include for testing, relative to the project root. This option also has special handling for directory paths (includes all test files within) and file paths (includes the corresponding test file if one exists).

#### Value Type

`array`

#### Default

`**/*.spec.ts,**/*.test.ts`

### list-tests

Lists all discovered test files and exits the process without building or executing the tests.

#### Value Type

`boolean`

#### Default

`false`

### output-file

Specifies a file path for the test report, applying only to the first reporter. To configure output files for multiple reporters, use the tuple format `['reporter-name', { outputFile: '...' }]` within the `reporters` option. When not provided, output is written to the console.

#### Value Type

`string`

### progress

Shows build progress information in the console. Defaults to the `progress` setting of the specified `buildTarget`.

#### Value Type

`boolean`

### providers-file

Specifies the path to a TypeScript file that provides an array of Angular providers for the test environment. The file must contain a default export of the provider array.

#### Value Type

`string`

### reporters

Specifies the reporters to use during test execution. Each reporter can be a string representing its name, or a tuple containing the name and an options object. Built-in reporters include 'default', 'verbose', 'dots', 'json', 'junit', 'tap', 'tap-flat', and 'html'. You can also provide a path to a custom reporter.

#### Value Type

`array`

### runner

Specifies the test runner to use for test execution.

#### Value Type

`string`

#### Allowed Values

`karma`, `vitest`

#### Default

`vitest`

### runner-config

Specifies the configuration file for the selected test runner. If a string is provided, it will be used as the path to the configuration file. If `true`, the builder will search for a default configuration file (e.g., `vitest.config.ts` or `karma.conf.js`). If `false`, no external configuration file will be used.\nFor Vitest, this enables advanced options and the use of custom plugins. Please note that while the file is loaded, the Angular team does not provide direct support for its specific contents or any third-party plugins used within it.

#### Value Type

`string`

### setup-files

A list of paths to global setup files that are executed before the test files. The application's polyfills and the Angular TestBed are always initialized before these files.

#### Value Type

`array`

### ts-config

The path to the TypeScript configuration file, relative to the workspace root. Defaults to `tsconfig.spec.json` in the project root if it exists. If not specified and the default does not exist, the `tsConfig` from the specified `buildTarget` will be used.

#### Value Type

`string`

### ui

Enables the Vitest UI for interactive test execution. This option is only available for the Vitest runner.

#### Value Type

`boolean`

#### Default

`false`

### watch

Enables watch mode, which re-runs tests when source files change. Defaults to `true` in TTY environments and `false` otherwise.

#### Value Type

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/test>
