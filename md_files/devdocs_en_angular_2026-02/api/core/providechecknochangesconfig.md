# provideCheckNoChangesConfig

provideCheckNoChangesConfig



# provideCheckNoChangesConfig

## API

```
function provideCheckNoChangesConfig(options: {
  exhaustive: false;
}): EnvironmentProviders;
function provideCheckNoChangesConfig(options: {
  interval?: number | undefined;
  exhaustive: true;
}): EnvironmentProviders;
```

```
function provideCheckNoChangesConfig(options: { exhaustive: false; }): EnvironmentProviders;
```

Used to disable exhaustive checks when verifying no expressions changed after they were checked.

This means that `OnPush` components that are not marked for check will not be checked. This behavior is the current default behavior in Angular. When running change detection on a view tree, views marked for check are refreshed and the flag to check it is removed. When Angular checks views a second time to ensure nothing has changed, `OnPush` components will no longer be marked and not be checked.

@paramoptions`{ exhaustive: false; }`

@returns`EnvironmentProviders`

```
function provideCheckNoChangesConfig(options: { interval?: number | undefined; exhaustive: true; }): EnvironmentProviders;
```

- `interval` will periodically run `checkNoChanges` on application views. This can be useful in zoneless applications to periodically ensure no changes have been made without notifying Angular that templates need to be refreshed.
- The exhaustive option will treat all application views as if they were [`ChangeDetectionStrategy.Default`](changedetectionstrategy#Default) when verifying no expressions have changed. All views attached to [`ApplicationRef`](applicationref) and all the descendants of those views will be checked for changes (excluding those subtrees which are detached via [`ChangeDetectorRef.detach()`](changedetectorref#detach)). This is useful because the check that runs after regular change detection does not work for components using [`ChangeDetectionStrategy.OnPush`](changedetectionstrategy#OnPush). This check is will surface any existing errors hidden by `OnPush` components.

@paramoptions`{ interval?: number | undefined; exhaustive: true; }`

@returns`EnvironmentProviders`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/provideCheckNoChangesConfig>
