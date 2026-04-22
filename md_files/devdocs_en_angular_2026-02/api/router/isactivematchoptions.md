# IsActiveMatchOptions

IsActiveMatchOptions



# IsActiveMatchOptions

A set of options which specify how to determine if a [`UrlTree`](urltree) is active, given the [`UrlTree`](urltree) for the current router state.

[Router#isActive](router#isActive)

## API

```
interface IsActiveMatchOptions {
  matrixParams: "exact" | "subset" | "ignored";
  queryParams: "exact" | "subset" | "ignored";
  paths: "exact" | "subset";
  fragment: "exact" | "ignored";
}
```

### matrixParams

`"exact" | "subset" | "ignored"`

Defines the strategy for comparing the matrix parameters of two [`UrlTree`](urltree)s.

The matrix parameter matching is dependent on the strategy for matching the segments. That is, if the `paths` option is set to `'subset'`, only the matrix parameters of the matching segments will be compared.

- `'exact'`: Requires that matching segments also have exact matrix parameter matches.
- `'subset'`: The matching segments in the router's active [`UrlTree`](urltree) may contain extra matrix parameters, but those that exist in the [`UrlTree`](urltree) in question must match.
- `'ignored'`: When comparing [`UrlTree`](urltree)s, matrix params will be ignored.

### queryParams

`"exact" | "subset" | "ignored"`

Defines the strategy for comparing the query parameters of two [`UrlTree`](urltree)s.

- `'exact'`: the query parameters must match exactly.
- `'subset'`: the active [`UrlTree`](urltree) may contain extra parameters, but must match the key and value of any that exist in the [`UrlTree`](urltree) in question.
- `'ignored'`: When comparing [`UrlTree`](urltree)s, query params will be ignored.

### paths

`"exact" | "subset"`

Defines the strategy for comparing the [`UrlSegment`](urlsegment)s of the [`UrlTree`](urltree)s.

- `'exact'`: all segments in each [`UrlTree`](urltree) must match.
- `'subset'`: a [`UrlTree`](urltree) will be determined to be active if it is a subtree of the active route. That is, the active route may contain extra segments, but must at least have all the segments of the [`UrlTree`](urltree) in question.

### fragment

`"exact" | "ignored"`

- `'exact'`: indicates that the [`UrlTree`](urltree) fragments must be equal.
- `'ignored'`: the fragments will not be compared when determining if a [`UrlTree`](urltree) is active.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/IsActiveMatchOptions>
