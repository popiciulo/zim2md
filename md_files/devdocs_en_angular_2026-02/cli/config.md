# config

config



# config

```
ng configng [json-path] [value][options]
```

A workspace has a single CLI configuration file, `angular.json`, at the top level. The `projects` object contains a configuration object for each project in the workspace.

You can edit the configuration directly in a code editor, or indirectly on the command line using this command.

The configurable property names match command option names, except that in the configuration file, all names must use camelCase, while on the command line options can be given dash-case.

For further details, see [Workspace Configuration](https://angular.dev/reference/configs/workspace-config).

For configuration of CLI usage analytics, see [ng analytics](analytics).

## Arguments

### json-path

The configuration key to set or query, in JSON path format. For example: "a[3].foo.bar[2]". If no new value is provided, returns the current value of this key.

#### Value Type

`string`

### value

If provided, a new value for the given configuration key.

#### Value Type

`string`

## Options

### global

Access the global configuration in the caller's home directory.

#### Value Type

`boolean`

#### Default

`false`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/config>
