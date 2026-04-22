# UrlHandlingStrategy

UrlHandlingStrategy



# UrlHandlingStrategy

Provides a way to migrate AngularJS applications to Angular.

[URL handling strategy](../../guide/routing/customizing-route-behavior#built-in-preloading-strategies)

## API

```
abstract class UrlHandlingStrategy {
  abstract shouldProcessUrl(url: UrlTree): boolean;
  abstract extract(url: UrlTree): UrlTree;
  abstract merge(newUrlPart: UrlTree, rawUrl: UrlTree): UrlTree;
}
```

### shouldProcessUrl

`boolean`

Tells the router if this URL should be processed.

When it returns true, the router will execute the regular navigation. When it returns false, the router will set the router state to an empty state. As a result, all the active components will be destroyed.

@paramurl`UrlTree`

@returns`boolean`

### extract

`UrlTree`

Extracts the part of the URL that should be handled by the router. The rest of the URL will remain untouched.

@paramurl`UrlTree`

@returns`UrlTree`

### merge

`UrlTree`

Merges the URL fragment with the rest of the URL.

@paramnewUrlPart`UrlTree`

@paramrawUrl`UrlTree`

@returns`UrlTree`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlHandlingStrategy>
