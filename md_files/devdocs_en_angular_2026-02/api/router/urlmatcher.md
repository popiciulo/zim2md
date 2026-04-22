# UrlMatcher

UrlMatcher



# UrlMatcher

A function for matching a route against URLs. Implement a custom URL matcher for [`Route.matcher`](route#matcher) when a combination of `path` and `pathMatch` is not expressive enough. Cannot be used together with `path` and `pathMatch`.

[Creating custom route matches](../../guide/routing/routing-with-urlmatcher)

## API

```
type UrlMatcher = (
  segments: UrlSegment[],
  group: UrlSegmentGroup,
  route: Route,
) => UrlMatchResult | null
```

## Description

A function for matching a route against URLs. Implement a custom URL matcher for [`Route.matcher`](route#matcher) when a combination of `path` and `pathMatch` is not expressive enough. Cannot be used together with `path` and `pathMatch`.

The function takes the following arguments and returns a [`UrlMatchResult`](urlmatchresult) object.

- *segments* : An array of URL segments.
- *group* : A segment group.
- *route* : The route to match against.

The following example implementation matches HTML files.

```
export function htmlFiles(url: UrlSegment[]) {
  return url.length === 1 && url[0].path.endsWith('.html') ? ({consumed: url}) : null;
}

export const routes = [{ matcher: htmlFiles, component: AnyComponent }];
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlMatcher>
