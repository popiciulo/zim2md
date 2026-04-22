# NavigationBehaviorOptions

NavigationBehaviorOptions



# NavigationBehaviorOptions

Options that modify the [`Router`](router) navigation strategy. Supply an object containing any of these properties to a [`Router`](router) navigation function to control how the navigation should be handled.

[Router#navigate](router#navigate)[Router#navigateByUrl](router#navigateByUrl)[Routing and Navigation guide](../../guide/routing/common-router-tasks)

## API

```
interface NavigationBehaviorOptions {
  onSameUrlNavigation?: OnSameUrlNavigation | undefined;
  skipLocationChange?: boolean | undefined;
  replaceUrl?: boolean | undefined;
  state?: { [k: string]: any; } | undefined;
  readonly info?: unknown;
  readonly browserUrl?: string | UrlTree | undefined;
}
```

### onSameUrlNavigation

`OnSameUrlNavigation | undefined`

How to handle a navigation request to the current URL.

This value is a subset of the options available in [`OnSameUrlNavigation`](onsameurlnavigation) and will take precedence over the default value set for the [`Router`](router).

### skipLocationChange

`boolean | undefined`

When true, navigates without pushing a new state into history.

```
// Navigate silently to /view
this.router.navigate(['/view'], { skipLocationChange: true });
```

### replaceUrl

`boolean | undefined`

When true, navigates while replacing the current state in history.

```
// Navigate to /view
this.router.navigate(['/view'], { replaceUrl: true });
```

### state

`{ [k: string]: any; } | undefined`

Developer-defined state that can be passed to any navigation. Access this value through the [`Navigation.extras`](navigation#extras) object returned from the [Router.getCurrentNavigation() method](router#getcurrentnavigation) while a navigation is executing.

After a navigation completes, the router writes an object containing this value together with a `navigationId` to `history.state`. The value is written when `location.go()` or `location.replaceState()` is called before activating this route.

Note that `history.state` does not pass an object equality test because the router adds the `navigationId` on each navigation.

### info

`unknown`

Use this to convey transient information about this particular navigation, such as how it happened. In this way, it's different from the persisted value `state` that will be set to `history.state`. This object is assigned directly to the Router's current [`Navigation`](navigation) (it is not copied or cloned), so it should be mutated with caution.

One example of how this might be used is to trigger different single-page navigation animations depending on how a certain route was reached. For example, consider a photo gallery app, where you can reach the same photo URL and state via various routes:

- Clicking on it in a gallery view
- Clicking
- "next" or "previous" when viewing another photo in the album
- Etc.

Each of these wants a different animation at navigate time. This information doesn't make sense to store in the persistent URL or history entry state, but it's still important to communicate from the rest of the application, into the router.

This information could be used in coordination with the View Transitions feature and the `onViewTransitionCreated` callback. The information might be used in the callback to set classes on the document in order to control the transition animations and remove the classes when the transition has finished animating.

### browserUrl

`string | UrlTree | undefined`

When set, the Router will update the browser's address bar to match the given [`UrlTree`](urltree) instead of the one used for route matching.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/NavigationBehaviorOptions>
