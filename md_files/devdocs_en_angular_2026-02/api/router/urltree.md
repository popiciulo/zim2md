# UrlTree

UrlTree



# UrlTree

Represents the parsed URL.

## API

```
class UrlTree {
  constructor(root?: UrlSegmentGroup, queryParams?: Params, fragment?: string | null): UrlTree;
  override root: UrlSegmentGroup;
  override queryParams: Params;
  override fragment: string | null;
  readonly queryParamMap: ParamMap;
  toString(): string;
}
```

### constructor

`UrlTree`

@paramroot`UrlSegmentGroup`

The root segment group of the URL tree

@paramqueryParams`Params`

The query params of the URL

@paramfragment`string | null`

The fragment of the URL

@returns`UrlTree`

### root

`UrlSegmentGroup`

The root segment group of the URL tree

### queryParams

`Params`

The query params of the URL

### fragment

`string | null`

The fragment of the URL

### queryParamMap

`ParamMap`

### toString

`string`

@returns`string`

## Description

Represents the parsed URL.

Since a router state is a tree, and the URL is nothing but a serialized state, the URL is a serialized tree. UrlTree is a data structure that provides a lot of affordances in dealing with URLs

## Usage Notes

### Example

```
@Component({templateUrl:'template.html'})
class MyComponent {
  constructor(router: Router) {
    const tree: UrlTree =
      router.parseUrl('/team/33/(user/victor//support:help)?debug=true#fragment');
    const f = tree.fragment; // return 'fragment'
    const q = tree.queryParams; // returns {debug: 'true'}
    const g: UrlSegmentGroup = tree.root.children[PRIMARY_OUTLET];
    const s: UrlSegment[] = g.segments; // returns 2 segments 'team' and '33'
    g.children[PRIMARY_OUTLET].segments; // returns 2 segments 'user' and 'victor'
    g.children['support'].segments; // return 1 segment 'help'
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlTree>
