# deploy

deploy



# deploy

```
ng deployng [project][options]
```

The command takes an optional project name, as specified in the `projects` section of the `angular.json` workspace configuration file. When a project name is not supplied, executes the `deploy` builder for the default project.

To use the `ng deploy` command, use `ng add` to add a package that implements deployment capabilities to your favorite platform. Adding the package automatically updates your workspace configuration, adding a deployment [CLI builder](https://angular.dev/tools/cli/cli-builder). For example:

```
"projects": {
  "my-project": {
    ...
    "architect": {
      ...
      "deploy": {
        "builder": "@angular/fire:deploy",
        "options": {}
      }
    }
  }
}
```

## Arguments

### project

The name of the project to build. Can be an application or a library.

#### Value Type

`string`

## Options

### configuration

One or more named builder configurations as a comma-separated list as specified in the "configurations" section in angular.json. The builder uses the named configurations to run the given target. For more information, see <https://angular.dev/reference/configs/workspace-config#alternate-build-configurations>.

#### Value Type

`string`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/deploy>
