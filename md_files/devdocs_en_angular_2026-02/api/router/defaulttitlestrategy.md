# DefaultTitleStrategy

DefaultTitleStrategy



# DefaultTitleStrategy

The default [`TitleStrategy`](titlestrategy) used by the router that updates the title using the [`Title`](../platform-browser/title) service.

## API

```
class DefaultTitleStrategy extends TitleStrategy {
  constructor(title: Title): DefaultTitleStrategy;
  updateTitle(snapshot: RouterStateSnapshot): void;
  override buildTitle(snapshot: RouterStateSnapshot): string | undefined;
  override getResolvedTitleForRoute(snapshot: ActivatedRouteSnapshot): any;
}
```

### constructor

`DefaultTitleStrategy`

@paramtitle`Title`

@returns`DefaultTitleStrategy`

### updateTitle

`void`

Sets the title of the browser to the given value.

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

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/DefaultTitleStrategy>
