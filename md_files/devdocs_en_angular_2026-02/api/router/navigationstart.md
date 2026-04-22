# NavigationStart

NavigationStart



# NavigationStart

An event triggered when a navigation starts.

## API

```
class NavigationStart extends RouterEvent {
  constructor(id: number, url: string, navigationTrigger?: NavigationTrigger, restoredState?: { [k: string]: any; navigationId: number; } | null): NavigationStart;
  readonly type: EventType.NavigationStart;
  navigationTrigger?: NavigationTrigger | undefined;
  restoredState?: { [k: string]: any; navigationId: number; } | null | undefined;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`NavigationStart`

@paramid`number`

@paramurl`string`

@paramnavigationTrigger`NavigationTrigger`

@paramrestoredState`{ [k: string]: any; navigationId: number; } | null`

@returns`NavigationStart`

### type

`EventType.NavigationStart`

### navigationTrigger

`NavigationTrigger | undefined`

Identifies the call or event that triggered the navigation. An `imperative` trigger is a call to `router.navigateByUrl()` or `router.navigate()`.

### restoredState

`{ [k: string]: any; navigationId: number; } | null | undefined`

The navigation state that was previously supplied to the `pushState` call, when the navigation is triggered by a `popstate` event. Otherwise null.

The state object is defined by [`NavigationExtras`](navigationextras), and contains any developer-defined state value, as well as a unique ID that the router assigns to every router transition/navigation.

From the perspective of the router, the router never "goes back". When the user clicks on the back button in the browser, a new navigation ID is created.

Use the ID in this previous-state object to differentiate between a newly created state and one returned to by a `popstate` event, so that you can restore some remembered state, such as scroll position.

### toString

`string`

@returns`string`

### id

`number`

A unique ID that the router assigns to every router navigation.

### url

`string`

The URL that is the destination for this navigation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationStart>
