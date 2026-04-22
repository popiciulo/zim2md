# extract-i18n

extract-i18n



# extract-i18n

```
ng extract-i18nng [project][options]
```

Extracts i18n messages from source code.

## Arguments

### project

The name of the project to build. Can be an application or a library.

#### Value Type

`string`

## Options

### build-target

A builder target to extract i18n messages in the format of `project:target[:configuration]`. You can also pass in more than one configuration name as a comma-separated list. Example: `project:target:production,staging`.

#### Value Type

`string`

### configuration

One or more named builder configurations as a comma-separated list as specified in the "configurations" section in angular.json. The builder uses the named configurations to run the given target. For more information, see <https://angular.dev/reference/configs/workspace-config#alternate-build-configurations>.

#### Value Type

`string`

### format

Output format for the generated file.

#### Value Type

`string`

#### Allowed Values

`arb`, `json`, `legacy-migrate`, `xlf`, `xlf2`, `xlif`, `xliff`, `xliff2`, `xmb`

#### Default

`xlf`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### i18n-duplicate-translation

How to handle duplicate translations.

#### Value Type

`string`

#### Allowed Values

`error`, `ignore`, `warning`

### out-file

Name of the file to output.

#### Value Type

`string`

### output-path

Path where output will be placed.

#### Value Type

`string`

### progress

Log progress to the console.

#### Value Type

`boolean`

#### Default

`true`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/extract-i18n>
