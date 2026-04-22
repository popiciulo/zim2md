# TitleStrategy

TitleStrategy



# TitleStrategy

Provides a strategy for setting the page title after a router navigation.

[Page title guide](../../guide/routing/define-routes#using-titlestrategy-for-page-titles)

## API

```
abstract class TitleStrategy {
  abstract updateTitle(snapshot: RouterStateSnapshot): void;
  buildTitle(snapshot: RouterStateSnapshot): string | undefined;
  getResolvedTitleForRoute(snapshot: ActivatedRouteSnapshot): any;
}
```

### updateTitle

`void`

Performs the application title update.

@paramsnapshot`RouterStateSnapshot`

@returns`void`

### buildTitle

`string | undefined`

@paramsnapshot`RouterStateSnapshot`

@returns`string | undefined`

### getResolvedTitleForRoute

`any`

Given an [`ActivatedRouteSnapshot`](activatedroutesnapshot), returns the final value of the [`Route.title`](route#title) property, which can either be a static string or a resolved value.

@paramsnapshot`ActivatedRouteSnapshot`

@returns`any`

## Description

Provides a strategy for setting the page title after a router navigation.

The built-in implementation traverses the router state snapshot and finds the deepest primary outlet with `title` property. Given the [`Routes`](routes) below, navigating to `/base/child(popup:aux)` would result in the document title being set to "child".

```
[
  {path: 'base', title: 'base', children: [
    {path: 'child', title: 'child'},
  ],
  {path: 'aux', outlet: 'popup', title: 'popupTitle'}
]
```

This class can be used as a base class for custom title strategies. That is, you can create your own class that extends the [`TitleStrategy`](titlestrategy). Note that in the above example, the `title` from the named outlet is never used. However, a custom strategy might be implemented to incorporate titles in named outlets.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/TitleStrategy>
