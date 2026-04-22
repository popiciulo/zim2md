# defaultUrlMatcher

defaultUrlMatcher



# defaultUrlMatcher

Matches the route configuration (`route`) against the actual URL (`segments`).

[UrlMatchResult](urlmatchresult)[Route](route)

## API

```
function defaultUrlMatcher(
  segments: UrlSegment[],
  segmentGroup: UrlSegmentGroup,
  route: Route,
): UrlMatchResult | null;
```

### defaultUrlMatcher

`UrlMatchResult | null`

Matches the route configuration (`route`) against the actual URL (`segments`).

When no matcher is defined on a [`Route`](route), this is the matcher used by the Router by default.

@paramsegments`UrlSegment[]`

The remaining unmatched segments in the current navigation

@paramsegmentGroup`UrlSegmentGroup`

The current segment group being matched

@paramroute`Route`

The [`Route`](route) to match against.

@returns`UrlMatchResult | null`

## Description

Matches the route configuration (`route`) against the actual URL (`segments`).

When no matcher is defined on a [`Route`](route), this is the matcher used by the Router by default.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/defaultUrlMatcher>
