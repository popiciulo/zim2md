# run

run



# run

```
ng runng <target>[options]
```

Architect is the tool that the CLI uses to perform complex tasks such as compilation, according to provided configurations. The CLI commands run Architect targets such as `build`, `serve`, `test`, and `lint`. Each named target has a default configuration, specified by an `options` object, and an optional set of named alternate configurations in the `configurations` object.

For example, the `serve` target for a newly generated app has a predefined alternate configuration named `production`.

You can define new targets and their configuration options in the `architect` section of the `angular.json` file which you can run them from the command line using the `ng run` command.

## Arguments

### target

The Architect target to run provided in the following format `project:target[:configuration]`.

#### Value Type

`string`

## Options

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/run>
