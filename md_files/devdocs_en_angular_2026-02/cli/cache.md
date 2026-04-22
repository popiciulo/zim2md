# cache

cache



# cache

```
ng cache[options]
```

Angular CLI saves a number of cachable operations on disk by default.

When you re-run the same build, the build system restores the state of the previous build and re-uses previously performed operations, which decreases the time taken to build and test your applications and libraries.

To amend the default cache settings, add the `cli.cache` object to your [Workspace Configuration](https://angular.dev/reference/configs/workspace-config). The object goes under `cli.cache` at the top level of the file, outside the `projects` sections.

```
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "cli": {
    "cache": {
      // ...
    },
  },
  "projects": {},
}
```

For more information, see [cache options](https://angular.dev/reference/configs/workspace-config#cache-options).

### Cache environments

By default, disk cache is only enabled for local environments. The value of environment can be one of the following:

- `all` - allows disk cache on all machines.
- `local` - allows disk cache only on development machines.
- `ci` - allows disk cache only on continuous integration (CI) systems.

To change the environment setting to `all`, run the following command:

```
ng config cli.cache.environment all
```

For more information, see `environment` in [cache options](https://angular.dev/reference/configs/workspace-config#cache-options).

The Angular CLI checks for the presence and value of the `CI` environment variable to determine in which environment it is running.

### Cache path

By default, `.angular/cache` is used as a base directory to store cache results.

To change this path to `.cache/ng`, run the following command:

```
ng config cli.cache.path ".cache/ng"
```

### Sub-commands

This command has the following sub-commands

- [clean](cache/clean)
- [disable](cache/disable)
- [enable](cache/enable)
- [info](cache/info)

## Options

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/cache>
