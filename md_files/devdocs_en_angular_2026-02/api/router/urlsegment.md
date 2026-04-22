# UrlSegment

UrlSegment



# UrlSegment

Represents a single URL segment.

## API

```
class UrlSegment {
  constructor(path: string, parameters: { [name: string]: string; }): UrlSegment;
  override path: string;
  override parameters: { [name: string]: string; };
  readonly parameterMap: ParamMap;
  toString(): string;
}
```

### constructor

`UrlSegment`

@parampath`string`

The path part of a URL segment

@paramparameters`{ [name: string]: string; }`

The matrix parameters associated with a segment

@returns`UrlSegment`

### path

`string`

The path part of a URL segment

### parameters

`{ [name: string]: string; }`

The matrix parameters associated with a segment

### parameterMap

`ParamMap`

### toString

`string`

@returns`string`

## Description

Represents a single URL segment.

A UrlSegment is a part of a URL between the two slashes. It contains a path and the matrix parameters associated with the segment.

## Usage Notes

### Example

```
@Component({templateUrl:'template.html'})
class MyComponent {
  constructor(router: Router) {
    const tree: UrlTree = router.parseUrl('/team;id=33');
    const g: UrlSegmentGroup = tree.root.children[PRIMARY_OUTLET];
    const s: UrlSegment[] = g.segments;
    s[0].path; // returns 'team'
    s[0].parameters; // returns {id: 33}
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlSegment>
