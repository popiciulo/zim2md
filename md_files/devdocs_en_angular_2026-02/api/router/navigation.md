# Navigation

Navigation



# Navigation

Information about a navigation operation. Retrieve the most recent navigation object with the [Router.currentNavigation() method](router#currentNavigation) .

## API

```
interface Navigation {
  id: number;
  initialUrl: UrlTree;
  extractedUrl: UrlTree;
  finalUrl?: UrlTree | undefined;
  trigger: NavigationTrigger;
  extras: NavigationExtras;
  previousNavigation: Navigation | null;
  readonly abort: () => void;
}
```

### id

`number`

The unique identifier of the current navigation.

### initialUrl

`UrlTree`

The target URL passed into the [`Router#navigateByUrl()`](router#navigateByUrl) call before navigation. This is the value before the router has parsed or applied redirects to it.

### extractedUrl

`UrlTree`

The initial target URL after being parsed with [`UrlHandlingStrategy.extract()`](urlhandlingstrategy#extract).

### finalUrl

`UrlTree | undefined`

The extracted URL after redirects have been applied. This URL may not be available immediately, therefore this property can be `undefined`. It is guaranteed to be set after the [`RoutesRecognized`](routesrecognized) event fires.

### trigger

`NavigationTrigger`

Identifies how this navigation was triggered.

### extras

`NavigationExtras`

Options that controlled the strategy used for this navigation. See [`NavigationExtras`](navigationextras).

### previousNavigation

`Navigation | null`

The previously successful [`Navigation`](navigation) object. Only one previous navigation is available, therefore this previous [`Navigation`](navigation) object has a `null` value for its own `previousNavigation`.

### abort

`() => void`

Aborts the navigation if it has not yet been completed or reached the point where routes are being activated. This function is a no-op if the navigation is beyond the point where it can be aborted.

## Description

Information about a navigation operation. Retrieve the most recent navigation object with the [Router.currentNavigation() method](router#currentNavigation) .

- *id* : The unique identifier of the current navigation.
- *initialUrl* : The target URL passed into the [`Router#navigateByUrl()`](router#navigateByUrl) call before navigation. This is the value before the router has parsed or applied redirects to it.
- *extractedUrl* : The initial target URL after being parsed with [`UrlSerializer.extract()`](urlserializer#extract).
- *finalUrl* : The extracted URL after redirects have been applied. This URL may not be available immediately, therefore this property can be `undefined`. It is guaranteed to be set after the [`RoutesRecognized`](routesrecognized) event fires.
- *trigger* : Identifies how this navigation was triggered. -- 'imperative'--Triggered by `router.navigateByUrl` or `router.navigate`. -- 'popstate'--Triggered by a popstate event. -- 'hashchange'--Triggered by a hashchange event.
- *extras* : A [`NavigationExtras`](navigationextras) options object that controlled the strategy used for this navigation.
- *previousNavigation* : The previously successful [`Navigation`](navigation) object. Only one previous navigation is available, therefore this previous [`Navigation`](navigation) object has a `null` value for its own `previousNavigation`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/Navigation>
