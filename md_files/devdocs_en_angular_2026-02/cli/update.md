# update

update



# update

```
ng updateng [packages..][options]
```

Perform a basic update to the current stable release of the core framework and CLI by running the following command.

```
ng update @angular/cli @angular/core
```

To update to the next beta or pre-release version, use the `--next` option.

To update from one major version to another, use the format

```
ng update @angular/cli@^<major_version> @angular/core@^<major_version>
```

We recommend that you always update to the latest patch version, as it contains fixes we released since the initial major release. For example, use the following command to take the latest 10.x.x version and use that to update.

```
ng update @angular/cli@^10 @angular/core@^10
```

For detailed information and guidance on updating your application, see the interactive [Angular Update Guide](https://update.angular.dev/).

## Arguments

### packages

The names of package(s) to update.

#### Value Type

`array`

#### Default

## Options

### allow-dirty

Whether to allow updating when the repository contains modified or untracked files.

#### Value Type

`boolean`

#### Default

`false`

### create-commits

Create source control commits for updates and migrations.

#### Value Type

`boolean`

#### Default

`false`

### force

Ignore peer dependency version mismatches.

#### Value Type

`boolean`

#### Default

`false`

### from

Version from which to migrate from. Only available when a single package is updated, and only with 'migrate-only'.

#### Value Type

`string`

### help

Shows a help message for this command in the console.

#### Value Type

`boolean`

### migrate-only

Only perform a migration, do not update the installed version.

#### Value Type

`boolean`

### name

The name of the migration to run. Only available when a single package is updated.

#### Value Type

`string`

### next

Use the prerelease version, including beta and RCs.

#### Value Type

`boolean`

#### Default

`false`

### to

Version up to which to apply migrations. Only available when a single package is updated, and only with 'migrate-only' option. Requires 'from' to be specified. Default to the installed version detected.

#### Value Type

`string`

### verbose

Display additional details about internal operations during execution.

#### Value Type

`boolean`

#### Default

`false`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/update>
