# setUpLocationSync

setUpLocationSync



# setUpLocationSync

Sets up a location change listener to trigger `history.pushState`. Works around the problem that `onPopState` does not trigger `history.pushState`. Must be called *after* calling [`UpgradeModule.bootstrap`](../../upgrade/static/upgrademodule#bootstrap).

[HashLocationStrategy](../../common/hashlocationstrategy)[PathLocationStrategy](../../common/pathlocationstrategy)

## API

```
function setUpLocationSync(
  ngUpgrade: UpgradeModule,
  urlType?: 'path' | 'hash',
): void;
```

### setUpLocationSync

`void`

Sets up a location change listener to trigger `history.pushState`. Works around the problem that `onPopState` does not trigger `history.pushState`. Must be called *after* calling [`UpgradeModule.bootstrap`](../../upgrade/static/upgrademodule#bootstrap).

@paramngUpgrade`UpgradeModule`

The upgrade NgModule.

@paramurlType`"path" | "hash"`

The location strategy.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/upgrade/setUpLocationSync>
