# NavigationSkipped

NavigationSkipped



# NavigationSkipped

An event triggered when a navigation is skipped. This can happen for a couple reasons including onSameUrlHandling is set to `ignore` and the navigation URL is not different than the current state.

## API

```
class NavigationSkipped extends RouterEvent {
  constructor(id: number, url: string, reason: string, code?: NavigationSkippedCode | undefined): NavigationSkipped;
  readonly type: EventType.NavigationSkipped;
  override reason: string;
  override id: number;
  override url: string;
}
```

### constructor

`NavigationSkipped`

@paramid`number`

@paramurl`string`

@paramreason`string`

A description of why the navigation was skipped. For debug purposes only. Use `code` instead for a stable skipped reason that can be used in production.

@paramcode`NavigationSkippedCode | undefined`

A code to indicate why the navigation was skipped. This code is stable for the reason and can be relied on whereas the `reason` string could change and should not be used in production.

@returns`NavigationSkipped`

### type

`EventType.NavigationSkipped`

### reason

`string`

A description of why the navigation was skipped. For debug purposes only. Use `code` instead for a stable skipped reason that can be used in production.

### id

`number`

A unique ID that the router assigns to every router navigation.

### url

`string`

The URL that is the destination for this navigation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationSkipped>
